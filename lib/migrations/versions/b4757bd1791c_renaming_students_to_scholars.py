"""Renaming students to scholars

Revision ID: b4757bd1791c
Revises: 791279dd0760
Create Date: 2025-05-24 10:01:35.743154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4757bd1791c'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
