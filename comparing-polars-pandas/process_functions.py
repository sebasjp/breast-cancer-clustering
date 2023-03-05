import pandas as pd
import polars as pl


def read_file(path: str, use_polars: bool):
    if use_polars:
        return pl.read_parquet(path)
    else:
        return pd.read_parquet(path)


def compute_mean(df, use_polars: bool):

    if use_polars:
        _ = df.select(pl.all().mean())
    else:
        _ = df.mean()
    
    return _


def compute_groupby(df, use_polars: bool):
    if use_polars:
        _ = df.groupby("id").agg(pl.all().mean())
    else:
        _ = df.groupby(["id"]).mean()
    
    return _


def compute_sort_values(df, use_polars: bool):
    if use_polars:
        _ = df.sort(pl.col("id"))
    else:
        _ = df.sort_values("id")
    
    return _


def compute_moving(df, use_polars: bool):
    if use_polars:
        _ = (
            df
            .with_columns(
                pl.col("target")
                .rolling_mean(3)
                .alias("moving")
            )
        )
    else:
        _ = df.reset_index(drop=True)
        _['moving'] = (
            _.groupby('id')
            .rolling(3)['target']
            .mean()
            .reset_index(drop=True)
        )
    
    return _