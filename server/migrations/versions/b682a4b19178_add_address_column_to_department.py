"""Add address Column to Department

Revision ID: b682a4b19178
Revises: f6e2866cf84f
Create Date: 2024-07-05 08:24:07.259547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b682a4b19178'
down_revision = 'f6e2866cf84f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('department', sa.Column('address', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('department', 'address')
    # ### end Alembic commands ###
