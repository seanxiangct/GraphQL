"""First commit

Revision ID: 4be5b7be4369
Revises: 
Create Date: 2022-09-24 10:53:31.834206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4be5b7be4369'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), sa.Identity(always=False), nullable=False),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('street', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.Enum('NSW', 'VIC', 'QLD', 'SA', 'WA', 'TAS', 'NT', 'ACT', name='stateenum'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('person',
    sa.Column('id', sa.Integer(), sa.Identity(always=False), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_person_id'), 'person', ['id'], unique=False)
    op.create_table('association',
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.Column('address_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['address_id'], ['address.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('person_id', 'address_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association')
    op.drop_index(op.f('ix_person_id'), table_name='person')
    op.drop_table('person')
    op.drop_table('address')
    op.execute('DROP TYPE stateenum')
    # ### end Alembic commands ###
