"""new fields in User model for profile

Revision ID: 432a3972795f
Revises: aef6d198a587
Create Date: 2022-10-18 14:10:08.387224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '432a3972795f'
down_revision = 'aef6d198a587'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###