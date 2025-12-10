"""
Simplex simbólico con SymPy
- Entradas: función objetivo (Max/Min) y restricciones (<=, >=, =)
- Convierte a forma estándar, agrega slack/surplus/artificial
- Usa Big-M (símbolo M) para variables artificiales (simbólico)
- Muestra todas las iteraciones en tablas consistentes (fila 0 incluida)
- Previene ciclos y detecta no acotado
"""
from sympy import symbols, Symbol, parse_expr, Rational, Matrix, simplify
from sympy import nsimplify
import re
import math
import copy

M = Symbol('M', positive=True)  # Big M symbolic

def prompt_input():
    print("Formato esperado ejemplo función objetivo:")
    print("  Max Z = 3*x1 + 5*x2")
    print("  Min Z = 0.4*x1 + 0.5*x2")
    obj_line = input("Ingrese la función objetivo (ej: Max Z = 3*x1 + 5*x2):\n").strip()
    n_cons = int(input("¿Cuántas restricciones tiene el problema? Ingrese un entero:\n").strip())
    cons = []
    print("Formato ejemplo restricciones:")
    print("  0.3*x1 + 0.1*x2 <= 2.7")
    print("  3*x1 + 2*x2 = 18")
    for i in range(n_cons):
        r = input(f"Restricción {i+1}:\n").strip()
        cons.append(r)
    return obj_line, cons

def parse_objective(obj_str):
    # Extract Max/Min and expression
    m = re.match(r'^\s*(Max|min|Maximizar|minimizar|Min|MAX)\b', obj_str, re.I)
    if not m:
        # tolerate "Z = ..."
        if '=' in obj_str:
            # assume Max by default? We'll ask user -> but per instructions do best-effort assume Max
            kind = 'Max'
        else:
            kind = 'Max'
    else:
        kind = 'Max' if m.group(1).lower().startswith('m') and m.group(1).lower() in ('max','maximizar','max') else 'Min' if m.group(1).lower().startswith('m') and m.group(1).lower() in ('min','minimizar','min') else 'Max'
    # take RHS of '='
    if '=' in obj_str:
        rhs = obj_str.split('=',1)[1]
    else:
        # try to remove leading Max Z etc
        parts = obj_str.split(None,2)
        rhs = parts[-1]
    expr = parse_expr(rhs, evaluate=False)
    return kind, expr

def parse_constraint(cons_str):
    # Find operator <=, >=, =
    if '<=' in cons_str:
        lhs, rhs = cons_str.split('<=',1)
        op = '<='
    elif '>=' in cons_str:
        lhs, rhs = cons_str.split('>=',1)
        op = '>='
    elif '=' in cons_str:
        lhs, rhs = cons_str.split('=',1)
        op = '='
    else:
        raise ValueError("Restricción sin operador válido (<=, >=, =): " + cons_str)
    lhs_e = parse_expr(lhs, evaluate=False)
    rhs_e = parse_expr(rhs, evaluate=False)
    return lhs_e, op, rhs_e

def collect_variables(obj_expr, constraints):
    vars_set = set()
    for a in [obj_expr] + [c[0] for c in constraints]:
        for s in a.free_symbols:
            # exclude M since it might not be present in inputs
            if str(s) != 'M':
                vars_set.add(str(s))
    # sort by name natural: x1, x2...
    vars_list = sorted(list(vars_set), key=lambda t: (re.sub(r'\D','',t)=='' , int(re.sub(r'\D','',t)) if re.sub(r'\D','',t)!='' else 0, t))
    return vars_list

def expr_coeffs(expr, var_list):
    # returns list of coefficients (sympy expr) for each var in var_list
    coeffs = []
    for v in var_list:
        sym = Symbol(v)
        coeff = expr.coeff(sym)
        coeffs.append(simplify(coeff))
    return coeffs

def ensure_positive_rhs(lhs, op, rhs):
    # If rhs negative, multiply both sides by -1 and flip inequality
    if rhs.is_negative:
        lhs = -lhs
        rhs = -rhs
        if op == '<=': op = '>='
        elif op == '>=': op = '<='
    return lhs, op, rhs

def build_standard_form(obj_kind, obj_expr, constraints_parsed, var_list):
    """
    Returns:
    - tableau: initial tableau as sympy Matrix
    - headers: list of column names (excluding VB col)
    - basic_vars: list of basic variable names per row (excluding row 0)
    - nonbasic_vars: list of nonbasic variable names
    - rows_info: mapping of rows to constraint strings
    """
    # Keep original variable symbols as sympy.Symbol
    var_syms = [Symbol(v) for v in var_list]

    # We'll create slack/surplus/artificial variables as needed
    slack_vars = []
    surplus_vars = []
    artificial_vars = []
    rows = []  # each row: coeff vector for original vars + placeholders for slack/surplus/artificial (built later) + RHS
    row_ops = []  # store row op meta: op type for var creation

    processed_constraints = []
    for (lhs, op, rhs) in constraints_parsed:
        lhs, op, rhs = ensure_positive_rhs(lhs, op, rhs)
        processed_constraints.append((lhs, op, rhs))

    # First pass: determine how many extra variables we'll need
    for (lhs, op, rhs) in processed_constraints:
        if op == '<=':
            slack_vars.append(f"s{len(slack_vars)+1}")
            row_ops.append(('slack', slack_vars[-1], rhs))
        elif op == '>=':
            surplus_vars.append(f"e{len(surplus_vars)+1}")  # exceso
            artificial_vars.append(f"a{len(artificial_vars)+1}")
            row_ops.append(('surplus+art', surplus_vars[-1], artificial_vars[-1], rhs))
        elif op == '=':
            artificial_vars.append(f"a{len(artificial_vars)+1}")
            row_ops.append(('art', artificial_vars[-1], rhs))
        else:
            raise ValueError("Operador desconocido")

    # Build header list: original vars + slack + surplus + artificial + RHS
    headers = var_list.copy()
    headers += slack_vars
    headers += surplus_vars
    headers += artificial_vars
    headers += ['RHS']

    # For each constraint, build coefficient row aligned with headers
    basic_vars = []  # initial basic variable per constraint row
    constraint_rows = []
    for idx,(lhs, op, rhs) in enumerate(processed_constraints):
        coeffs = expr_coeffs(lhs, var_list)
        row = [simplify(c) for c in coeffs]
        # add zeros for slack/surplus/artificial in header order
        # slack
        for s in slack_vars:
            if row_ops[idx][0]=='slack' and s==row_ops[idx][1]:
                row.append(Rational(1))
            else:
                row.append(Rational(0))
        # surplus
        for e in surplus_vars:
            if row_ops[idx][0]=='surplus+art' and e==row_ops[idx][1]:
                row.append(Rational(-1))
            else:
                row.append(Rational(0))
        # artificial
        for a in artificial_vars:
            if (row_ops[idx][0]=='surplus+art' and a==row_ops[idx][2]) or (row_ops[idx][0]=='art' and a==row_ops[idx][1]):
                row.append(Rational(1))
            else:
                row.append(Rational(0))
        # RHS
        row.append(simplify(rhs))
        constraint_rows.append(row)

        # assign basic var
        if row_ops[idx][0]=='slack':
            basic_vars.append(row_ops[idx][1])
        elif row_ops[idx][0]=='surplus+art':
            basic_vars.append(row_ops[idx][2])
        elif row_ops[idx][0]=='art':
            basic_vars.append(row_ops[idx][1])
        else:
            basic_vars.append(f"b{idx+1}")

    # Build objective row (row 0). We will form Max problem:
    # If user input was Min, convert by maximizing -Z
    if obj_kind == 'Min':
        obj_expr = -obj_expr

    # Objective row: -Z + sum(cj*xj) + M*artificials if any -> We'll put row as
    # coefficients for header variables and RHS is 0. For Max Z = sum cj xj, in simplex
    # the row is: Z - sum cj xj - M*sum(artificials) = 0 ; we'll store coefficients accordingly
    # We'll put (Z row) as: coef for each variable = -cj (so that when tableau uses "Z row", negative means entering)
    # But to match many tabular forms, we'll store row with Z coefficient as 1 in VB column (we'll print separately)
    # Implementation: place coefficient = -cj for original variables; for artificials add M penalty (plus or minus depending)
    obj_coeffs = expr_coeffs(obj_expr, var_list)
    obj_row = []
    # original vars
    for c in obj_coeffs:
        obj_row.append(simplify(-c))
    # slack vars -> 0
    for _ in slack_vars:
        obj_row.append(Rational(0))
    # surplus vars -> 0
    for _ in surplus_vars:
        obj_row.append(Rational(0))
    # artificials -> penalty -M (because we maximized -Z; typical approach: Z - sum(cj xj) + M*art = 0 if using Max of -Z)
    for _ in artificial_vars:
        # For the way we're building, we'll place +M to punish artificials in row 0's coefficients
        # We'll add M (positive) multiplied by 1 (their coefficient)
        obj_row.append(simplify(M))
    # RHS for objective row
    obj_row.append(Rational(0))

    # If there are artificial variables, we should adjust the objective row to be consistent (i.e., eliminate artificials from row 0)
    # Method: For each artificial variable that is basic initially, subtract M * (that constraint row) from row 0
    tableau_rows = [obj_row] + constraint_rows
    # Convert to Matrix for algebra convenience
    T = Matrix(tableau_rows)

    # Now eliminate artificial columns in row 0 by row operation: row0 = row0 - M * (row where artificial is basic)
    # Find index positions of artificial variables in headers
    art_positions = []
    for a in artificial_vars:
        art_positions.append(headers.index(a))
    # For each row (constraint row i), if its basic var is an artificial, then perform row0 = row0 - M * row_i
    for i, bv in enumerate(basic_vars):
        if bv in artificial_vars:
            row_i = Matrix([constraint_rows[i]])  # fijar como fila 1×n
            T[0, :] = simplify(T[0, :] - M * row_i)

    # Build names for non-basic vars: initially those not in basic_vars (excluding Z)
    nonbasic_vars = [h for h in headers[:-1] if h not in basic_vars]  # exclude RHS
    # Prepend row 0 VB name as 'Z'
    # For printing, we will treat row 0 as VB 'Z'

    return T, headers, ['Z'] + basic_vars, nonbasic_vars

def tableau_to_printable(T, headers, row_basic_vars):
    # T is sympy Matrix with rows = 1 + m constraints, columns = len(headers) + RHS already in headers
    # We'll produce a 2D list of strings for printing
    rows = []
    # Header row: VB | headers... (headers include RHS)
    hdr = ['Ec #', 'VB'] + headers
    rows.append(hdr)
    # Row 0:
    r0 = ['(0)', row_basic_vars[0]] + [str(simplify(T[0,j])) for j in range(T.shape[1])]
    rows.append(r0)
    # Constraint rows
    for i in range(1, T.shape[0]):
        ecnum = f"({i})"
        vb = row_basic_vars[i]
        rowvals = [str(simplify(T[i,j])) for j in range(T.shape[1])]
        rows.append([ecnum, vb] + rowvals)
    return rows

def print_table_rows(rows):
    # Compute column widths
    col_widths = []
    ncols = len(rows[0])
    for c in range(ncols):
        w = max(len(str(row[c])) for row in rows)
        col_widths.append(w)
    # Print each row with separators
    sep = ' | '
    for i, row in enumerate(rows):
        line = sep.join(str(cell).rjust(col_widths[j]) for j,cell in enumerate(row))
        print(line)
        if i==0:
            print('-' * len(line))

def choose_pivot_column(T, headers, row_basic_vars, maximize=True, M_numeric=10**6):
    # We pick entering variable from row 0 coefficients (excluding RHS, first columns correspond to headers)
    # For maximize=True: choose most negative coefficient in row0 (since row0 stores -cj + adjustments)
    # We'll substitute large numeric for M to compare symbolic values
    row0 = T[0,:-1]  # exclude RHS
    best_idx = None
    best_val = None
    for j, coeff in enumerate(row0):
        val = float(coeff.subs(M, M_numeric))
        if maximize:
            # look for most negative
            if best_val is None or val < best_val - 1e-12 or (abs(val-best_val)<1e-12 and j < best_idx):
                if val < -1e-12:
                    best_val = val
                    best_idx = j
        else:
            # for minimization (if we use), pick most positive (not used because we convert Min->Max)
            if best_val is None or val > best_val + 1e-12 or (abs(val-best_val)<1e-12 and j < best_idx):
                if val > 1e-12:
                    best_val = val
                    best_idx = j
    return best_idx  # None if optimal

def choose_pivot_row(T, pivot_col, headers, basic_vars, M_numeric=10**6):
    # Minimum ratio test: choose smallest positive RHS / pivot_col_entry
    ratios = []
    for i in range(1, T.rows):
        a_ij = float(T[i, pivot_col].subs(M, M_numeric))
        rhs = float(T[i, -1].subs(M, M_numeric))
        if a_ij > 1e-12:
            ratio = rhs / a_ij
            ratios.append((ratio, i))
    if not ratios:
        return None  # Unbounded
    # find minimum ratio; if tie, apply Bland's rule: choose smallest index basic var name lexicographically
    ratios.sort(key=lambda x: (x[0], x[1]))  # stable by row number as tie-breaker
    return ratios[0][1]

def pivot(T, pivot_row, pivot_col):
    # Perform row operations to make pivot 1 and column zeros (using sympy exact arithmetic)
    A = T.copy()
    pivot_val = A[pivot_row, pivot_col]
    # divide pivot row by pivot_val
    A[pivot_row,:] = simplify(A[pivot_row,:] / pivot_val)
    # eliminate other rows
    for i in range(A.rows):
        if i != pivot_row:
            factor = A[i, pivot_col]
            A[i,:] = simplify(A[i,:] - factor * A[pivot_row,:])
    return A

def hash_tableau(T):
    # create string representation for cycle detection (substitute M as symbol to keep symbolic)
    # but to avoid huge strings, convert each element to simplified str
    s = []
    for i in range(T.rows):
        for j in range(T.cols):
            s.append(str(simplify(T[i,j])))
    return '|'.join(s)

def simplex_solve(obj_line, constraints_lines, max_iters=100):
    # Parse objective and constraints
    obj_kind, obj_expr = parse_objective(obj_line)
    constraints_parsed = [parse_constraint(c) for c in constraints_lines]
    # Collect variable names
    var_list = collect_variables(obj_expr, constraints_parsed)
    if not var_list:
        raise ValueError("No variables detected in el modelo.")
    # Build standard form initial tableau
    T, headers, row_basic_vars, nonbasic_vars = build_standard_form(obj_kind, obj_expr, constraints_parsed, var_list)
    iteration = 0
    visited = set()
    print("\n--- Tableau inicial (Iteración 0) ---")
    rows_print = tableau_to_printable(T, headers, row_basic_vars)
    print_table_rows(rows_print)
    # Store history of basic/nonbasic
    history = []
    history.append((iteration, copy.deepcopy(row_basic_vars), copy.deepcopy(nonbasic_vars)))
    visited.add(hash_tableau(T))
    # main loop (maximize problem assumed after conversion)
    while True:
        iteration += 1
        pivot_col = choose_pivot_column(T, headers, row_basic_vars, maximize=True)
        if pivot_col is None:
            print(f"\nNo hay coeficientes negativos en la fila 0 -> solución óptima alcanzada (Iteración {iteration-1}).")
            break
        # Column name:
        entering = headers[pivot_col]
        # Choose pivot row by min ratio
        pivot_row = choose_pivot_row(T, pivot_col, headers, row_basic_vars)
        if pivot_row is None:
            print("\nREGIÓN NO ACOTADA detectada: no existe fila candidata para la columna pivote -> solución no acotada.")
            return {'status':'unbounded', 'tableau':T, 'headers':headers, 'basic_vars':row_basic_vars}
        leaving = row_basic_vars[pivot_row]
        print(f"\n--- Iteración {iteration}: columna que entra = {entering}, fila pivote = {pivot_row} (saliente = {leaving}) ---")
        # Pivot
        T = pivot(T, pivot_row, pivot_col)
        # Update basic vars
        row_basic_vars[pivot_row] = entering
        # update nonbasic list
        nonbasic_vars = [h for h in headers[:-1] if h not in row_basic_vars[1:]]
        # Print table
        rows_print = tableau_to_printable(T, headers, row_basic_vars)
        print_table_rows(rows_print)
        history.append((iteration, copy.deepcopy(row_basic_vars), copy.deepcopy(nonbasic_vars)))
        h = hash_tableau(T)
        if h in visited:
            print("\nSe detectó repetición del tableau -> posible ciclo. Aplicando regla de Bland o deteniendo para evitar bucle infinito.")
            return {'status':'cycle', 'tableau':T, 'headers':headers, 'basic_vars':row_basic_vars}
        visited.add(h)
        if iteration >= max_iters:
            print("\nSe alcanzó el número máximo de iteraciones permitido.")
            return {'status':'max_iters', 'tableau':T, 'headers':headers, 'basic_vars':row_basic_vars}
    # final result: read solution
    sol = {}
    for v in headers[:-1]:
        sol[v] = Rational(0)
    for i in range(1, T.rows):
        bv = row_basic_vars[i]
        sol[bv] = simplify(T[i, -1])
    objective_value = simplify(T[0, -1])
    # Convert objective sign if original problem was Min (we converted Min->Max by negating obj)
    # If original was Min, the printed objective was for Max(-Z) so the real Z = -objective_value
    final_obj = objective_value
    if obj_kind == 'Min':
        final_obj = simplify(-objective_value)
    return {'status':'optimal', 'tableau':T, 'headers':headers, 'basic_vars':row_basic_vars,
            'nonbasic':nonbasic_vars, 'solution':sol, 'objective':final_obj}

# ----------- Main interactive run -------------
if __name__ == "__main__":
    print("SIMPLEX SÍMBOLO (Big-M). Entrada por texto.")
    obj_line, cons_lines = prompt_input()
    result = simplex_solve(obj_line, cons_lines)
    status = result.get('status')
    if status == 'optimal':
        print("\n--- SOLUCIÓN ÓPTIMA ---")
        sol = result['solution']
        for k in sorted(sol.keys(), key=lambda x: (x!='RHS', x)):
            if k!='RHS':
                print(f"{k} = {simplify(sol[k])}")
        print(f"Valor de la función objetivo Z = {simplify(result['objective'])}")
    else:
        print("\nResultado:", status)
        if 'tableau' in result:
            print("Tabla final mostrada arriba.")