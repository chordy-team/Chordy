"""users table

Revision ID: 7997e934d59a
Revises: 
Create Date: 2019-03-29 12:42:20.724115

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7997e934d59a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('`keys`',
    sa.Column('kid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('kid'),
    sa.UniqueConstraint('name')
    )
    op.create_table('posts',
    sa.Column('pid', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=1000), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('progid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['uid'], ['users.uid'], ),
    sa.PrimaryKeyConstraint('pid')
    )
    op.drop_index('fk_progid_idx', table_name='Posts')
    op.drop_index('fk_uid_idx', table_name='Posts')
    op.drop_index('pid_UNIQUE', table_name='Posts')
    op.drop_table('Posts')
    op.drop_index('kid_UNIQUE', table_name='keys')
    op.drop_index('name_UNIQUE', table_name='keys')
    op.drop_table('keys')
    op.alter_column('chords', 'image',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.alter_column('chords', 'name',
               existing_type=mysql.VARCHAR(length=10),
               nullable=True)
    op.drop_index('cid_UNIQUE', table_name='chords')
    op.drop_index('fk_cid_idx', table_name='keychords')
    op.drop_constraint(u'fk_kid', 'keychords', type_='foreignkey')
    op.create_foreign_key(None, 'keychords', '`keys`', ['kid'], ['kid'])
    op.alter_column('progressions', 'c1',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('progressions', 'c2',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('progressions', 'c3',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('progressions', 'c4',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('progressions', 'uid',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.drop_index('fk_c1_idx', table_name='progressions')
    op.drop_index('fk_c2_idx', table_name='progressions')
    op.drop_index('fk_c3_idx', table_name='progressions')
    op.drop_index('fk_c4_idx', table_name='progressions')
    op.drop_index('fk_uid_idx', table_name='progressions')
    op.drop_index('progid_UNIQUE', table_name='progressions')
    op.alter_column('users', 'email',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.alter_column('users', 'password',
               existing_type=mysql.VARCHAR(length=45),
               nullable=True)
    op.alter_column('users', 'username',
               existing_type=mysql.VARCHAR(length=45),
               nullable=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.drop_index('uid_UNIQUE', table_name='users')
    op.drop_index('username_UNIQUE', table_name='users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('username_UNIQUE', 'users', ['username'], unique=True)
    op.create_index('uid_UNIQUE', 'users', ['uid'], unique=True)
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.alter_column('users', 'username',
               existing_type=mysql.VARCHAR(length=45),
               nullable=False)
    op.alter_column('users', 'password',
               existing_type=mysql.VARCHAR(length=45),
               nullable=False)
    op.alter_column('users', 'email',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.create_index('progid_UNIQUE', 'progressions', ['progid'], unique=True)
    op.create_index('fk_uid_idx', 'progressions', ['uid'], unique=False)
    op.create_index('fk_c4_idx', 'progressions', ['c4'], unique=False)
    op.create_index('fk_c3_idx', 'progressions', ['c3'], unique=False)
    op.create_index('fk_c2_idx', 'progressions', ['c2'], unique=False)
    op.create_index('fk_c1_idx', 'progressions', ['c1'], unique=False)
    op.alter_column('progressions', 'uid',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('progressions', 'c4',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('progressions', 'c3',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('progressions', 'c2',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('progressions', 'c1',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.drop_constraint(None, 'keychords', type_='foreignkey')
    op.create_foreign_key(u'fk_kid', 'keychords', 'keys', ['kid'], ['kid'])
    op.create_index('fk_cid_idx', 'keychords', ['cid'], unique=False)
    op.create_index('cid_UNIQUE', 'chords', ['cid'], unique=True)
    op.alter_column('chords', 'name',
               existing_type=mysql.VARCHAR(length=10),
               nullable=False)
    op.alter_column('chords', 'image',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.create_table('keys',
    sa.Column('kid', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=10), nullable=False),
    sa.PrimaryKeyConstraint('kid'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_index('name_UNIQUE', 'keys', ['name'], unique=True)
    op.create_index('kid_UNIQUE', 'keys', ['kid'], unique=True)
    op.create_table('Posts',
    sa.Column('pid', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('content', mysql.VARCHAR(length=1000), nullable=True),
    sa.Column('date', mysql.DATETIME(), nullable=True),
    sa.Column('uid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('progid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['progid'], [u'progressions.progid'], name=u'fk_progid'),
    sa.ForeignKeyConstraint(['uid'], [u'users.uid'], name=u'fk_uid2'),
    sa.PrimaryKeyConstraint('pid'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_index('pid_UNIQUE', 'Posts', ['pid'], unique=True)
    op.create_index('fk_uid_idx', 'Posts', ['uid'], unique=False)
    op.create_index('fk_progid_idx', 'Posts', ['progid'], unique=False)
    op.drop_table('posts')
    op.drop_table('`keys`')
    # ### end Alembic commands ###