"""add content column to posts table

Revision ID: cd6bf168137b
Revises: 3a973ebd7ffb
Create Date: 2023-04-23 22:11:51.976957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd6bf168137b'
down_revision = '3a973ebd7ffb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
