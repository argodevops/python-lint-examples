# Python Lint Example

The example project installs `pre-commit`, `black` and `pylint` to demonstrate how to apply formatting and linting to a `git` commit.

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

## pylint

Pylint is a static code analyser for Python.

Run `pylint *.py`

https://pypi.org/project/pylint/