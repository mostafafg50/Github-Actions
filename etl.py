import pandas as pd
from sqlalchemy import create_engine
import os


def extract():
    df = pd.read_csv("data/customers.csv")
    return df


def transform(df):
    df = df.dropna(subset=["customer"])
    df = df.drop_duplicates()
    return df


def load(df):
    db_url = os.getenv("DATABASE_URL")
    engine = create_engine(db_url)
    df.to_sql(
        "raw_customers",
        engine,
        if_exists="replace",
        index=False
    )


def run_etl():
    df = extract()
    df = transform(df)
    load(df)


if __name__ == "__main__":
    run_etl()