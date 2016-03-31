"""empty message

Revision ID: f7e7e152b014
Revises: 4a1e66408a83
Create Date: 2016-03-31 21:17:50.926645

"""

# revision identifiers, used by Alembic.
revision = 'f7e7e152b014'
down_revision = '4a1e66408a83'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lost',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('serial_code', sa.String(length=255), nullable=False),
    sa.Column('asset_name', sa.String(length=255), nullable=False),
    sa.Column('lost', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lost')
    ### end Alembic commands ###
