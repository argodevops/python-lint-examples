# Python Lint Example

The example project installs `pre-commit`, `black` and `pylint` to demonstrate how to apply formatting and linting to a `git` commit.

Contains example Python scripts which can be adapted and may be useful.

* run_simulation.py - runs a simulation command based on an environment and type of simulation command, orginanlly written for running Gatling load simulations

## Pre-requisites

Run ` $ pip install -r requirements.txt`

## pre-commit

Runs hooks on every commit to automatically point out issues in code.

Run ` $ pre-commit install` to setup the git hook scripts

https://pre-commit.com/

## black

Black is the uncompromising Python code formatter.

Run `black *.py`

https://pypi.org/project/black/

## ruff

Pylint is a static code analyser for Python.

Run `ruff *.py`

https://github.com/astral-sh/ruff