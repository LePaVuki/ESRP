from .orm import engine
from .orm import Region
from sqlalchemy.orm import Session


def main():
    with Session(engine) as session:
        spongebob = Region(
            name="spongebob",
            fullname="Spongebob Squarepants",
            addresses=[Address(email_address="spongebob@sqlalchemy.org")],
        )

        session.add_all([spongebob, sandy, patrick])

        session.commit()


if __name__ == "__main__":
    main()
