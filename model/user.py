from sqlalchemy import Table, Column

from sqlalchemy.sql.sqltypes import Integer, String

from config.db import engine, metadata

users = Table("tb_user", metadata,
              Column("user_cod", Integer, primary_key=True),
              Column("user_rut", Integer, nullable=False),
              Column("user_name", String(255), nullable=False),
              Column("user_last_name", String(255), nullable=False),
              Column("profile_cod", Integer, nullable=False))

metadata.create_all(engine)
