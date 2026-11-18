"""Load and inspect datasets."""

import pandas as pd
from pathlib import Path


def data_ingestion(file_path: str):

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError("Dataset is empty.")

    print("Data ingestion completed successfully")
    print(f"Dataset shape: {df.shape}")
    print(f"Total rows: {df.shape[0]}")
    print(f"Total columns: {df.shape[1]}")

    return df


if __name__ == "__main__":

    project_root = Path(__file__).resolve().parents[1]

    dataset_path = project_root / "data" / "raw" / "concrete.csv"

    df = data_ingestion(dataset_path)

    print("\nDataset Preview:")
    print(df.head())

    print("\nDataset Information:")
    print(df.info())
