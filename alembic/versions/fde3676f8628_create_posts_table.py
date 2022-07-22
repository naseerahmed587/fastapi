"""create posts table

Revision ID: fde3676f8628
Revises: 
Create Date: 2022-07-20 22:15:55.014786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fde3676f8628'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'posts', 
        sa.Column('id', sa.Integer(), nullable = False, primary_key = True),
        sa.Column('title',sa.String(), nullable = False)
    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
