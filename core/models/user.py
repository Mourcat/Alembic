from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class User(Base):
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    father_name: Mapped[str] = mapped_column()
    service_id: Mapped[int] = mapped_column(unique=True)