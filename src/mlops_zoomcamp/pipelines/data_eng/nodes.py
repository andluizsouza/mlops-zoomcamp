"""
This is a boilerplate pipeline 'data_eng'
generated using Kedro 0.18.9
"""

from typing import List

import pandas as pd
from sklearn.feature_extraction import DictVectorizer


def get_sample(df_in: pd.DataFrame, params) -> pd.DataFrame:

    frac = params["frac"]

    df_out = df_in.sample(frac=frac, random_state=42)

    return df_out


def calc_duration(df_in: pd.DataFrame, params: dict) -> pd.DataFrame:

    df_out = df_in.copy()
    df_out[params["duration_col"]] = (
        df_out[params["dropoff_col"]] - df_out[params["pickup_col"]]
    )
    df_out[params["duration_col"]] = (
        df_out[params["duration_col"]].dt.total_seconds() / 60.0
    )

    index_non_outlier = (df_out[params["duration_col"]] >= 1.0) & (
        df_out[params["duration_col"]] <= 60.0
    )
    df_out = df_out[index_non_outlier]

    return df_out


def set_categorical_features(df_in: pd.DataFrame, params: dict) -> pd.DataFrame:

    df_out = df_in.copy()
    df_out[params["categorical_features"]] = df_out[
        params["categorical_features"]
    ].astype(str)

    df_out[params["agg_categorical_feature"]] = (
        df_out[params["categorical_features"][0]]
        + "_"
        + df_out[params["categorical_features"][1]]
    )

    return df_out


def create_train_set(df_in: pd.DataFrame, params: dict):

    dv = DictVectorizer()

    categorical_col = [params["agg_categorical_feature"]]
    numerical_col = [params["numerical_col"]]
    dicts = df_in[categorical_col + numerical_col].to_dict(orient="records")
    x_set = dv.fit_transform(dicts)

    y_set = df_in[params["target_col"]]

    return x_set, y_set, dv


def create_val_test_sets(df_in: pd.DataFrame, params: dict, dv: DictVectorizer):

    categorical_col = [params["agg_categorical_feature"]]
    numerical_col = [params["numerical_col"]]
    dicts = df_in[categorical_col + numerical_col].to_dict(orient="records")
    x_set = dv.transform(dicts)

    y_set = df_in[params["target_col"]]

    return x_set, y_set
