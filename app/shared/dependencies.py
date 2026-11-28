from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from typing import Annotated

from app.database.session import get_database_session
from app.database.unit_of_work import SQLAlchemyUnitOfWork
from app.shared.interface.unit_of_work import UnitOfWork



async def get_unit_of_work(
    session: Annotated[AsyncSession, Depends(get_database_session)]
) -> UnitOfWork:
    return SQLAlchemyUnitOfWork(session=session)