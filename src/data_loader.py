import pandas as pd
from ucimlrepo import fetch_ucirepo

def _flatten_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Flatten multi-index columns if needed."""
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [
            "_".join([str(x) for x in col if str(x) != "nan"])
            for col in df.columns.values
        ]
    return df


def load_from_file(path: str) -> pd.DataFrame:
    """
    Load Credit Default dataset from file (Excel or CSV).
    Automatically handles multi-header files and flattens columns.
    """
    if path.endswith(".xls") or path.endswith(".xlsx"):
        df = pd.read_excel(path, header=[0, 1])
    else:
        try:
            df = pd.read_csv(path, header=[0, 1])
        except Exception:
            df = pd.read_csv(path)

    return _flatten_columns(df)


def load_from_ucimlrepo() -> pd.DataFrame:
    """
    Load Credit Default dataset from UCI ML Repo via ucimlrepo package.
    """
    dataset = fetch_ucirepo(id=350)
    X = dataset.data.features
    y = dataset.data.targets
    df = pd.concat([X, y], axis=1)
    df.columns = [
        "X1_LIMIT_BAL", "X2_SEX", "X3_EDUCATION", "X4_MARRIAGE", "X5_AGE",
        "X6_PAY_0", "X7_PAY_2", "X8_PAY_3", "X9_PAY_4", "X10_PAY_5", "X11_PAY_6",
        "X12_BILL_AMT1", "X13_BILL_AMT2", "X14_BILL_AMT3", "X15_BILL_AMT4",
        "X16_BILL_AMT5", "X17_BILL_AMT6",
        "X18_PAY_AMT1", "X19_PAY_AMT2", "X20_PAY_AMT3", "X21_PAY_AMT4",
        "X22_PAY_AMT5", "X23_PAY_AMT6",
        "Y_default payment next month"
    ]
    return (df)
