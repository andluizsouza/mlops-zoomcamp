"""
This is a boilerplate pipeline 'training'
generated using Kedro 0.18.9
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import tune_model_params


def create_pipeline(**kwargs) -> Pipeline:

    return pipeline(
        [
            node(
                func=tune_model_params,
                inputs=["x_train", "x_val", "y_train", "y_val", "params:tuning"],
                outputs=None,
                name="tune_model",
            )
        ]
    )
