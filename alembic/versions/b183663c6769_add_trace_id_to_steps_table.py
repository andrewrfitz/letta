"""add trace id to steps table

Revision ID: b183663c6769
Revises: fdcdafdb11cf
Create Date: 2025-02-26 14:38:06.095556

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b183663c6769"
down_revision: Union[str, None] = "fdcdafdb11cf"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("steps", sa.Column("trace_id", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("steps", "trace_id")
    # ### end Alembic commands ###
