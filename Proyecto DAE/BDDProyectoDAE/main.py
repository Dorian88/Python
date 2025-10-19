from config.database import SessionLocal
from models import Institution, Role

def quick_test():
    session = SessionLocal()

    try:
        #Se crea una institución y un rol si no existe
        if not session.query(Institution).first():
            inst = Institution(name = "Demo Institue", doamin = "demo.edu")
            session.add(inst)
            session.commit()
            print("Institución creada")
        if not session.query(Role).filter_by(name = "Admin").first():
            role = Role(name = "Admin", description = "Administrador global")
            session.add(role)
            session.commit()
            print("Role Admin creado")
    finally:
        session.close()

if __name__ == "__main__":
    quick_test()