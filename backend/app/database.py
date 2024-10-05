from sqlalchemy import create_engine

# psycopg2 connection to postgreSQL
engine = create_engine("postgresql+psycopg2://${POSTGRES_USER}:tiger@localhost/mydatabase", echo=True)