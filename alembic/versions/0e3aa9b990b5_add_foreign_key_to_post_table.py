"""add foreign-key to Post table

Revision ID: 0e3aa9b990b5
Revises: cd09da440803
Create Date: 2022-07-21 09:39:45.942298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e3aa9b990b5'
down_revision = 'cd09da440803'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key(constraint_name='posts_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column(table_name='posts', column_name='owner_id')
    pass
