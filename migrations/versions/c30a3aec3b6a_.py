"""empty message

Revision ID: c30a3aec3b6a
Revises: 
Create Date: 2019-10-09 10:21:10.669346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c30a3aec3b6a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Job', 'name',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('Machine', 'enabled',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('Machine', 'name',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('Machine', 'type',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('Task', 'job_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('Task', 'name',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('Task', 'sequence',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint('task_job_id_fkey', 'Task', type_='foreignkey')
    op.alter_column('Task_queue', 'machine_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('Task_queue', 'status',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('Task_queue', 'task_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint('task_queue_task_id_fkey', 'Task_queue', type_='foreignkey')
    op.drop_constraint('task_queue_machine_id_fkey', 'Task_queue', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('task_queue_machine_id_fkey', 'Task_queue', 'Machine', ['machine_id'], ['id'])
    op.create_foreign_key('task_queue_task_id_fkey', 'Task_queue', 'Task', ['task_id'], ['id'])
    op.alter_column('Task_queue', 'task_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('Task_queue', 'status',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('Task_queue', 'machine_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_foreign_key('task_job_id_fkey', 'Task', 'Job', ['job_id'], ['id'])
    op.alter_column('Task', 'sequence',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('Task', 'name',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('Task', 'job_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('Machine', 'type',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('Machine', 'name',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('Machine', 'enabled',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('Job', 'name',
               existing_type=sa.TEXT(),
               nullable=False)
    # ### end Alembic commands ###
