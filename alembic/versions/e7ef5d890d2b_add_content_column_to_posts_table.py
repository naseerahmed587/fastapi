"""add content column to posts table

Revision ID: e7ef5d890d2b
Revises: fde3676f8628
Create Date: 2022-07-20 22:34:08.856675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7ef5d890d2b'
down_revision = 'fde3676f8628'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts', 
        sa.Column('content', sa.String(), nullable = False)
    )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
