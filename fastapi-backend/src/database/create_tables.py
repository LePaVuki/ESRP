from src.database.orm import engine
from src.database.orm import Base


def main():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
