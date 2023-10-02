from typing import Optional

from sqlalchemy import String
from sqlalchemy import text, BIGINT, Boolean, true
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base, TimestampMixin, TableNameMixin


class Item(Base, TimestampMixin, TableNameMixin):
    item_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    item_name: Mapped[Optional[str]] = mapped_column(String(128))
    item_description: Mapped[str] = mapped_column(String(500))
    item_price: Mapped[bool] = mapped_column(Boolean, server_default=true())

    def __repr__(self):
        return f"<Item {self.item_id} {self.item_name} {self.item_price}>"
