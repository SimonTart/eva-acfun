"""add table comments

Revision ID: 9e328ab68d0f
Revises: 8aa5765c5cf1
Create Date: 2017-10-11 00:01:56.851538+08:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e328ab68d0f'
down_revision = 'd6e4de61c58f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
        sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
        sa.Column('content', sa.Text(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('post_date', sa.DateTime(), nullable=True),
        sa.Column('quoteId', sa.Integer(), nullable=True),
        sa.Column('is_delete', sa.Boolean(), nullable=False),
        sa.Column('is_up_delete', sa.Boolean(), nullable=False),
        sa.Column('article_id', sa.Integer(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###