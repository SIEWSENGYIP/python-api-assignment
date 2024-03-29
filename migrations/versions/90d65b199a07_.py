"""empty message

Revision ID: 90d65b199a07
Revises: 
Create Date: 2019-09-11 21:52:34.654977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90d65b199a07'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('houses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sell_price', sa.Integer(), nullable=True),
    sa.Column('list_price', sa.Integer(), nullable=True),
    sa.Column('living_size', sa.Integer(), nullable=True),
    sa.Column('rooms_num', sa.Integer(), nullable=True),
    sa.Column('beds_num', sa.Integer(), nullable=True),
    sa.Column('baths_num', sa.Integer(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('acres', sa.Float(), nullable=True),
    sa.Column('taxes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('houses')
    # ### end Alembic commands ###
