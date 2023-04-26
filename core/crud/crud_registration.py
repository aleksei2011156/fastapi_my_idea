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
    """
    Function create User in Data Base

    Args:
        db (Session): session with db
        user (Registration): models user(login:str, email:str, password:str, password_repeat:str)

    Returns:
        Users: ...
    """
        
    db_user: Users = Users(login=user.login, email=user.email, password=RegistrationUtils.hash_lib(user.password_repeat))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    

