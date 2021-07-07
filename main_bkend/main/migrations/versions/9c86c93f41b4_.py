"""empty message

Revision ID: 9c86c93f41b4
Revises: 0c4ae1d8e9b7
Create Date: 2021-07-07 16:41:14.378443

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9c86c93f41b4'
down_revision = '0c4ae1d8e9b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('weather_data_cities', sa.Column('city_name', sa.String(length=200), nullable=True))
    op.drop_column('weather_data_cities', 'city_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('weather_data_cities', sa.Column('city_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_column('weather_data_cities', 'city_name')
    # ### end Alembic commands ###
