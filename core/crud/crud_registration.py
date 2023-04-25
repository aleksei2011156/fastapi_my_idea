from sqlalchemy.orm import Session
from ..schemas import Registration
from ..models import Users
from ..settings import RegistrationUtils

def get_user_by_email(db: Session, email: str) -> None:
    """
    Check user in DataBase

    Args:
        db (Session): Session with DataBase
        email (str): user email

    Returns:
        _type_: Object sqlalchemy user email or None
    """    
    return db.query(Users).filter(Users.email == email).first()


def create_user(db: Session, user: Registration) -> Users:
    db_user: Users = Users(login=user.login, email=user.email, password=RegistrationUtils.hash_lib(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    

