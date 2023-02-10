from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

DATABASE_URL = "postgresql+asyncpg://postgres:123@localhost:5432/Async"


class AsyncDB:

    def __init__(self) -> None:
        self.engine = None
        self.session = None

    def __getattr__(self, name):
        return getattr(self.session, name)

    def init(self):
        self.engine = create_async_engine(DATABASE_URL, echo=True, future=True,)
        self.session = sessionmaker(self.engine, class_=AsyncSession, expire_on_commit=False)

    async def create_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)


db = AsyncDB()
