"""Add created_at to Note

Revision ID: 8c8f2cbd42d6
Revises: 
Create Date: 2024-10-29 00:14:55.934486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c8f2cbd42d6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('note', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('note', schema=None) as batch_op:
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
