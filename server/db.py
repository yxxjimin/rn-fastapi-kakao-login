import sqlalchemy, sqlalchemy.orm
from models import Users

USERNAME = 'root'
PASSWORD = '1234'
HOST = 'localhost'
PORT = 3306
DATABASE = 'mindbut'
DB_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

class EngineConnection:
    def __init__(self):
        self.engine = sqlalchemy.create_engine(DB_URL, echo=True)
        Users.__table__.create(bind=self.engine, checkfirst=True)

    def sessionmaker(self):
        Session = sqlalchemy.orm.sessionmaker(bind=self.engine)
        session = Session()
        return session

    def connection(self):
        conn = self.engine.connect()
        return conn