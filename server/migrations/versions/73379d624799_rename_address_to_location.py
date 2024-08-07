"""rename address to location

Revision ID: 73379d624799
Revises: a0a089e478dc
Create Date: 2024-07-05 08:35:47.491504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73379d624799'
down_revision = 'a0a089e478dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###
