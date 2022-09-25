"""add data

Revision ID: 79b41bb9415d
Revises: 4be5b7be4369
Create Date: 2022-09-25 05:19:55.281521

"""
import email
from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm
from models.models import Person, Address, StateEnum


# revision identifiers, used by Alembic.
revision = '79b41bb9415d'
down_revision = '4be5b7be4369'
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    person = Person(name="John", email="john.smith@email.com")
    person.addresses.append(Address(number=1, street="Main Street", city="Sydney", state=StateEnum.WA))
    person.addresses.append(Address(number=2, street="Main Street", city="Sydney", state=StateEnum.ACT))

    session.add(person)

    person = Person(name="Sean", email="sean.xiang@email.com")
    person.addresses.append(Address(number=3, street="Main Street", city="Sydney", state=StateEnum.NSW))

    session.add(person)

    person = Person(name="Jane", email="jane@email.com")
    session.add(person)

    session.commit()


def downgrade() -> None:
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    session.execute("DELETE FROM association")
    session.execute("DELETE FROM address")
    session.execute("DELETE FROM person")
    session.commit()
    session.close()
