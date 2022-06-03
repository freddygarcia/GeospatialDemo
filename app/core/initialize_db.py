from app.api.models import Base
from .db import engine, SessionLocal
import geopandas as gpd
import logging


def initialize_db():

    logging.info("Initializing database...")

    session = SessionLocal()

    logging.info("Creating database tables...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    session.commit()
    session.close()

    logging.info("Loading demo data...")

    # Read shapefile using GeoPandas
    gdf = gpd.read_file("data/grocery-store-locations-2-1.geo")
    # set coordianate system
    gdf.set_crs(epsg=4326, inplace=True)
    # Import shapefile to databse
    gdf.to_postgis(name="groceries", con=engine, schema="public",
                   if_exists="append")

    engine.connect().execute("""
        SELECT
            setval('"groceries_OBJECTID_seq"', COALESCE((
                SELECT MAX("OBJECTID")+1 FROM groceries
            ), 1), false);
        commit;
    """)

    logging.info("Database initialization complete.")


if __name__ == "__main__":
    initialize_db()
