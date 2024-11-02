"""rename department

Revision ID: 044e6a79200b
Revises: 050631b18897
Create Date: 2024-11-01 20:19:38.478822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '044e6a79200b'
down_revision = '050631b18897'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
