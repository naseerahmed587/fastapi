"""Add last few columns to posts table

Revision ID: 9d3027043fd2
Revises: 0e3aa9b990b5
Create Date: 2022-07-21 10:05:26.698189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d3027043fd2'
down_revision = '0e3aa9b990b5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(table_name='posts', column=sa.Column("published", sa.Boolean(), nullable = False, server_default = 'TRUE'),)
    op.add_column(table_name='posts', column=sa.Column('created_at', sa.TIMESTAMP(timezone= True), nullable = False, server_default = sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column(table_name='posts', column_name='published')
    op.drop_column(table_name='posts', column_name='created_at')
    pass
