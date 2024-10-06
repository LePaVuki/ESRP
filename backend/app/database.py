from typing import List
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


# psycopg2 creating engine to connect to postgreSQL
engine = create_engine("postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@localhost:${DB_HOST_PORT}/${POSTGRES_DB}", echo=True)

# declaring tables and metadata
class Base(DeclarativeBase):
    pass

class System(Base):
    __tablename__ = "systems"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    safety: Mapped[str] = mapped_column(String(2))
    constellation_id: Mapped[int] = mapped_column(ForeignKey("constellations.id"))

    constellations: Mapped["Constellation"] = relationship(back_populates="systems")

    def __repr__(self) -> str:
        return f"System(id={self.id!r}, name={self.name!r}, safety={self.safety!r})"

class Constellation(Base):
    __tablename__ = "constellations"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    region_id: Mapped[int] = mapped_column(ForeignKey("regions.id"))

    systems: Mapped["System"] = relationship(back_populates="constellations")
    regions: Mapped["Region"] = relationship(back_populates="constellations")

    def __repr__(self) -> str:
        return f"Constellation(id={self.id!r}, name={self.name!r})"


class Region(Base):
    __tablename__ = "regions"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    constellations: Mapped["Constellation"] = relationship(back_populates="regions")

    def __repr__(self) -> str:
         return f"Region(id={self.id!r}, name={self.name!r})"

def main():
	Base.metadata.create_all(engine)

if __name__ == '__main__':
	main()