import pandas as pd
from etl import transform


def test_transform_removes_nulls():
    data = {
        "id": [1, 2],
        "customer": ["Ahmed", None]
    }

    df = pd.DataFrame(data)
    result = transform(df)

    assert result["customer"].isnull().sum() == 0