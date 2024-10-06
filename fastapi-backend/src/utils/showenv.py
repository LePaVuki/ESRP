from os import environ

def main():
    db_host = environ["DB_HOST"]
    db_port = environ["DB_PORT"]
    db_user = environ["POSTGRES_USER"]
    db_pass = environ["POSTGRES_PASSWORD"]
    db_name = environ["POSTGRES_DB"]

    print(db_host)
    print(db_port)
    print(db_user)
    print(db_pass)
    print(db_name)

if __name__ == "__main__":
    main()