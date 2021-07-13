"""create tables

Revision ID: 7884a8a8487c
Revises: 
Create Date: 2021-07-12 12:55:09.940485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7884a8a8487c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coins_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('coin', sa.String(), nullable=False),
    sa.Column('symbol', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ptax',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.Date(), nullable=False),
    sa.Column('sell_rate', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=127), nullable=False),
    sa.Column('last_name', sa.String(length=511), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password_hash', sa.String(length=511), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('coin', sa.String(), nullable=False),
    sa.Column('fiat', sa.String(), nullable=False),
    sa.Column('price_per_coin', sa.Float(), nullable=False),
    sa.Column('avg_price_brl', sa.Float(), nullable=False),
    sa.Column('avg_price_usd', sa.Float(), nullable=False),
    sa.Column('net_quantity', sa.Float(), nullable=False),
    sa.Column('quantity', sa.Float(), nullable=False),
    sa.Column('foreign_exch', sa.Boolean(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('accounting',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('sell_total', sa.String(), nullable=False),
    sa.Column('profit', sa.String(), nullable=False),
    sa.Column('tax', sa.String(), nullable=False),
    sa.Column('foreign_exch', sa.String(), nullable=False),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['transaction_id'], ['transaction.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('accounting')
    op.drop_table('transaction')
    op.drop_table('user')
    op.drop_table('ptax')
    op.drop_table('coins_list')
    # ### end Alembic commands ###