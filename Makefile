# Installation of requirements
install:
	pip install --upgrade pip && pip install -r src/requirements.txt


# Auto Code Review (best practices of coding)
code-review:
	@echo " *** 1/4: Python code formattion with black ***"
	black .
	@echo " *** 2/4: Sorting imported libraries with isort ***"
	isort src/
	@echo " *** 3/4: Checking for missing docstrings with interrogate ***"
	interrogate src/mlops_zoomcamp/pipelines src/tests/pipelines -vv --fail-under=100
	@echo " *** 4/4: Checking the style and quality code with pylint ***"
	pylint src/mlops_zoomcamp/pipelines/ src/tests/pipelines/ --fail-under=9.5