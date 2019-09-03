"""add language to posts

Revision ID: 26820ac88c17
Revises: 8a3c1aeac5e0
Create Date: 2019-08-28 10:17:30.804717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26820ac88c17'
down_revision = '8a3c1aeac5e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
