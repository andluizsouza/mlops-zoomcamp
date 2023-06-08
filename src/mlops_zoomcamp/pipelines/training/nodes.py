"""
This is a boilerplate pipeline 'training'
generated using Kedro 0.18.9
"""

import json

import mlflow
import optuna
import pandas as pd
from optuna.samplers import TPESampler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


def tune_model_params(
    x_train: pd.DataFrame,
    x_val: pd.DataFrame,
    y_train: pd.Series,
    y_val: pd.Series,
    params: dict,
):

    num_trials = params["num_trials"]

    def objective(trial):
        params = {
            "n_estimators": trial.suggest_int("n_estimators", 10, 50, 1),
            "max_depth": trial.suggest_int("max_depth", 1, 20, 1),
            "min_samples_split": trial.suggest_int("min_samples_split", 2, 10, 1),
            "min_samples_leaf": trial.suggest_int("min_samples_leaf", 1, 4, 1),
            "random_state": 42,
            "n_jobs": -1,
        }

        rf_model = RandomForestRegressor(**params)
        rf_model.fit(x_train, y_train)
        y_pred = rf_model.predict(x_val)
        rmse = mean_squared_error(y_val, y_pred, squared=False)

        return rmse

    sampler = TPESampler(seed=42)
    study = optuna.create_study(direction="minimize", sampler=sampler)
    study.optimize(objective, n_trials=num_trials)

    # Best trial
    print(f"Best value (RMSE): {study.best_trial.value}")
    print(f"Best hyperparameters: {json.dumps(study.best_trial.params, indent=2)}")

    return
