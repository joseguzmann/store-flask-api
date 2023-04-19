"""empty message

Revision ID: 4572ecbfd9f6
Revises: ab2d9a51c4c0
Create Date: 2023-04-18 21:45:34.397885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4572ecbfd9f6'
down_revision = 'ab2d9a51c4c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###
