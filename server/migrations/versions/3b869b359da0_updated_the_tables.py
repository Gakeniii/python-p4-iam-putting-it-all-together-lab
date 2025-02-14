"""updated the tables

Revision ID: 3b869b359da0
Revises: bd4f8a8ffb73
Create Date: 2025-01-30 18:13:45.357595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b869b359da0'
down_revision = 'bd4f8a8ffb73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.alter_column('minutes_to_complete',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('_password_hash',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('_password_hash',
               existing_type=sa.VARCHAR(),
               nullable=False)

    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('minutes_to_complete',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
