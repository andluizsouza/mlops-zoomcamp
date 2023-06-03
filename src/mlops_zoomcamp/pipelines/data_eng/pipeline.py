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
            inputs=["train_dataset_raw", "params:data_preprocess"],
            outputs="train_dataset_inter",
            name="calc_duration_train",
        ),
        node(
            func=calc_duration,
            inputs=["val_dataset_raw", "params:data_preprocess"],
            outputs="val_dataset_inter",
            name="calc_duration_val",
        ),
        node(
            func=calc_duration,
            inputs=["test_dataset_raw", "params:data_preprocess"],
            outputs="test_dataset_inter",
            name="test_duration_test",
        ),
        node(
            func=set_categorical_features,
            inputs=["train_dataset_inter", "params:data_preprocess"],
            outputs="train_dataset_primary",
            name="set_categorical_train",
        ),
        node(
            func=set_categorical_features,
            inputs=["val_dataset_inter", "params:data_preprocess"],
            outputs="val_dataset_primary",
            name="set_categorical_val",
        ),
        node(
            func=set_categorical_features,
            inputs=["test_dataset_inter", "params:data_preprocess"],
            outputs="test_dataset_primary",
            name="set_categorical_test",
        ),
        node(
            func=create_train_set,
            inputs=["train_dataset_primary", "params:data_preprocess"],
            outputs=["x_train", "y_train", "dv"],
            name="create_train_set",
        ),
        node(
            func=create_val_test_sets,
            inputs=["val_dataset_primary", "params:data_preprocess"],
            outputs=["x_val", "y_val"],
            name="create_val_set",
        ),
        node(
            func=create_val_test_sets,
            inputs=["test_dataset_primary", "params:data_preprocess"],
            outputs=["x_test", "y_test"],
            name="create_test_set",
        ),
    ])
