"""
This is a boilerplate pipeline 'data_eng'
generated using Kedro 0.18.9
"""

from kedro.pipeline import Pipeline, node, pipeline


from .nodes import (
    calc_duration,
    set_categorical_features,
    create_train_set,
    create_val_test_sets,
)


def create_pipeline() -> Pipeline:
    """
    Create a kedro pipeline connecting nodes
    Returns:
        Pipeline: built kedro pipeline
    """


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=calc_duration,
            inputs=["train_raw", "params:data_preprocess"],
            outputs="train_inter",
            name="calc_duration_train",
        )
    ])
