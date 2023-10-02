from typing import Optional

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert

from infrastructure.database.models import Item
from infrastructure.database.repo.base import BaseRepo


class ItemRepo(BaseRepo):
    async def get_or_create_item(
        self,
        item_id: int,
        item_name: str,
        item_description: str,
        item_price: str,
    ):
        insert_stmt = (
            insert(Item)
            .values(
                item_id=item_id,
                item_name=item_name,
                item_description=item_description,
                item_price=item_price,
            )
            .on_conflict_do_update(
                index_elements=[Item.item_id],
                set_=dict(
                    item_name=item_name,
                    item_description=item_description,
                    item_price=item_price,
                ),
            )
            .returning(Item)
        )
        result = await self.session.execute(insert_stmt)

        await self.session.commit()
        return result.scalar_one()



