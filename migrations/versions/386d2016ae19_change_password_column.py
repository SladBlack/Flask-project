"""Change password column

Revision ID: 386d2016ae19
Revises: b96b6f4dd8ea
Create Date: 2021-10-05 21:57:12.417695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '386d2016ae19'
down_revision = 'b96b6f4dd8ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=128), nullable=True))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
    op.drop_column('users', 'password')
    # ### end Alembic commands ###