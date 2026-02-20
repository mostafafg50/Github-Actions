import pandas as pd
from sqlalchemy import create_engine
import os


def extract():
    df = pd.read_csv("./customers.csv")
    return df


def transform(df):
    df = df.dropna(subset=["customer"])
    df = df.drop_duplicates()
    return df


def load(df):
    output_path = os.getenv("OUTPUT_PATH", "output/raw_customers.csv")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)


def run_etl():
    df = extract()
    df = transform(df)
    load(df)


if __name__ == "__main__":
    run_etl()