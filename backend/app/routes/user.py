from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError

from app.database import Session
from app.models import User
from app.schemas import UserPublic, UserSchema
from app.utils import handle_integrity_error

router = APIRouter(prefix='/conta', tags=['conta'])


@router.post('/', response_model=UserPublic, status_code=HTTPStatus.CREATED)
async def create_user(user: UserSchema, session: Session):
    try:
        db_user = User(
            username=user.username,
            cpf=user.cpf,
            email=user.email,
            senha=user.senha,
        )
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        return db_user

    except IntegrityError as e:
        await session.rollback()
        msg = handle_integrity_error(e)
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail=msg)

    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
