"""add time

Revision ID: 99dbc244e483
Revises: 
Create Date: 2023-10-11 18:11:41.640150

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '99dbc244e483'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('app_permission',
    sa.Column('api_id', sa.Integer(), nullable=True),
    sa.Column('permission_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['api_id'], ['api_token.id'], ),
    sa.ForeignKeyConstraint(['permission_id'], ['api_permission.id'], )
    )
    with op.batch_alter_table('userdb', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=128), nullable=False))
        batch_op.drop_column('_password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('userdb', schema=None) as batch_op:
        batch_op.add_column(sa.Column('_password', mysql.VARCHAR(length=128), nullable=False))
        batch_op.drop_column('password')

    op.drop_table('app_permission')
    # ### end Alembic commands ###
