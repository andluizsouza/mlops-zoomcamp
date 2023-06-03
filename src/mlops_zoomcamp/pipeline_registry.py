"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from mlops_zoomcamp.pipelines import data_eng


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """

    data_eng_pipe = data_eng.create_pipeline()

    pipelines = {
        "data_eng": data_eng_pipe,
        "__default__": data_eng_pipe,
    }

    return pipelines
