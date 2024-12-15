from typing import AsyncGenerataor

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)

from core.config import settings


class DBHelper:
    def __init__(self, url: str, echo: bool = False, echo_pool: bool = False, pool_size: int = 5, max_overflow: int = 10) -> None:
        self.engine: AsyncEngine = create_async_engine(url=url, echo=echo, echo_pool=echo_pool, pool_size=pool_size, max_overflow=max_overflow)
        self.session_factory : async_sessionmaker[AsyncSession] = async_sessionmaker(bind=self.engine, autoflush=False, autocommit=False, expire_on_commit=False)
        
         
    async def session_getter(self) -> AsyncGenerataor[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session
            
    
    async def dispose(self):
        await self.engine.dispose()
        
        
db_helper = DBHelper(
    url=settings.db.db_url,
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)