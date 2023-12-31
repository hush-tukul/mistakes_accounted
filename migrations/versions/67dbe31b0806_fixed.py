"""Fixed

Revision ID: 67dbe31b0806
Revises: 
Create Date: 2023-10-01 16:08:05.958697

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '67dbe31b0806'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('item_id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('item_name', sa.String(length=128), nullable=True),
    sa.Column('item_description', sa.String(length=500), nullable=False),
    sa.Column('item_price', sa.Boolean(), server_default=sa.text('true'), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('item_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('full_name', sa.String(length=128), nullable=False),
    sa.Column('active', sa.Boolean(), server_default=sa.text('true'), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('items')
    # ### end Alembic commands ###
