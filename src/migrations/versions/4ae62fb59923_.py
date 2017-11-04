"""empty message

Revision ID: 4ae62fb59923
Revises: 5a442edeae8d
Create Date: 2017-11-04 19:44:17.026445

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ae62fb59923'
down_revision = '5a442edeae8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    drugs_table = op.create_table('drugs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('category', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    op.bulk_insert(
        drugs_table,
        [
            {'id':1, 'name':'Heroin', 'category':'Street'},
            {'id':2, 'name':'Methadone', 'category':'Street'},
            {'id':3, 'name':'Methadone', 'category':'Prescription'},
            {'id':4, 'name':'Cocaine', 'category':'Street'},
            {'id':5, 'name':'Crack', 'category':'Street'},
            {'id':6, 'name':'Benzodiazepine', 'category':'Street'},
            {'id':7, 'name':'Benzodiazepine', 'category':'Prescription'},
            {'id':8, 'name':'Alcohol', 'category':'Street'},
            {'id':9, 'name':'Clonodine', 'category':'Street'},
            {'id':10, 'name':'Clonodine', 'category':'Prescription'},
            {'id':11, 'name':'Speed', 'category':'Street'},
            {'id':12, 'name':'Speed', 'category':'Prescription'},
            {'id':13, 'name':'PCP', 'category':'Street'},
            {'id':14, 'name':'Unknown', 'category':'Street'},
            {'id':15, 'name':'Unknown', 'category':'Prescription'}
        ]
    )

    locations_table = op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    op.bulk_insert(
        locations_table,
        [
            {'id':1, 'name':'Stocking and 5th'},
            {'id':2, 'name':'Boston Square'},
            {'id':3, 'name':'Burton and Division'},
            {'id':4, 'name':'401 Hall'},
            {'id':5, 'name':'Heartside'},
            {'id':6, 'name':'Muskegon Outreach'},
            {'id':7, 'name':'Muskegon - MySpace'},
            {'id':8, 'name':'Programa Puenté'},
        ]
    )

    op.create_table('syringe_access',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('new_client', sa.Boolean(), nullable=True),
    sa.Column('safe_crack_supplies', sa.Boolean(), nullable=True),
    sa.Column('num_overdose_kits', sa.Integer(), nullable=True),
    sa.Column('seconday_syringe_exchange', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    syringes_table = op.create_table('syringes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    op.bulk_insert(
        syringes_table,
        [
            {'id':1, 'name':'1cc 27g 1/2"'},
            {'id':2, 'name':'1cc 28g 1/2"'},
            {'id':3, 'name':'1cc 30g 5/16"'},
            {'id':4, 'name':'3cc 25g 1/2"'},
            {'id':5, 'name':'1/2cc 28g 1/2"'},
            {'id':6, 'name':'Other syringes'}
        ]
    )

    op.create_table('overdose_reversals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('county', sa.String(), nullable=True),
    sa.Column('site', sa.String(), nullable=True),
    sa.Column('date_of_overdose', sa.Date(), nullable=True),
    sa.Column('time_before_naloxone', sa.Integer(), nullable=True),
    sa.Column('naloxone_amount', sa.Integer(), nullable=True),
    sa.Column('num_intra_nasal_doses', sa.Integer(), nullable=True),
    sa.Column('route', sa.String(), nullable=True),
    sa.Column('performed_rescue_breathing', sa.Boolean(), nullable=True),
    sa.Column('used_barrier', sa.Boolean(), nullable=True),
    sa.Column('overdose_returned_time', sa.Integer(), nullable=True),
    sa.Column('police_called', sa.Boolean(), nullable=True),
    sa.Column('employee_initials', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('participant_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('intake_data', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('syringe_access_syringes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('syringe_access_id', sa.Integer(), nullable=False),
    sa.Column('syringe_id', sa.Integer(), nullable=False),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['syringe_access_id'], ['syringe_access.id'], ),
    sa.ForeignKeyConstraint(['syringe_id'], ['syringes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('overdose_reversal_drugs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reversal_id', sa.Integer(), nullable=False),
    sa.Column('drug_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['drug_id'], ['drugs.id'], ),
    sa.ForeignKeyConstraint(['reversal_id'], ['overdose_reversals.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('overdose_reversal_drugs')
    op.drop_table('syringe_access_syringes')
    op.drop_table('participant_info')
    op.drop_table('overdose_reversals')
    op.drop_table('syringes')
    op.drop_table('syringe_access')
    op.drop_table('locations')
    op.drop_table('drugs')
    # ### end Alembic commands ###
