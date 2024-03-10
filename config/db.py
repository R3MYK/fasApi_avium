from sqlalchemy import create_engine, MetaData
#Url paraconección con bases de datos
engine = create_engine("mysql+pymysql://root@localhost:3306/avium")

conn = engine.connect()

metadata = MetaData()