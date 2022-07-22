"""Add user table

Revision ID: cd09da440803
Revises: e7ef5d890d2b
Create Date: 2022-07-21 09:06:47.495503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd09da440803'
down_revision = 'e7ef5d890d2b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
        sa.Column("id", sa.Integer(), nullable = False),
        sa.Column("email", sa.String(), nullable = False),
        sa.Column("password", sa.String(), nullable = False),
        sa.Column("created_at", sa.TIMESTAMP(timezone= True), server_default = sa.text('now()'), nullable = False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
