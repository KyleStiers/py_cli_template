# Python Click App Template

This repo is boilerplate for quickly creating Python click applications. It assumes the use of [poetry](https://python-poetry.org/). Start a new repo from this template and `poetry init` and you should be good to go for starting dev on your CLI application.

It also serves as a way for me to keep an active version of my preferred tooling when starting out.

An empty `.envrc` is kept to remind myself of integrations possible with [direnv](https://direnv.net/).

Very basic pre-commit hooks are set up.

## Things to edit on new repo creation

To make this your own named CLI you will need to change

1. The source directory name (currently `pycli`), remember to conform to python package naming conventions.
2. `name` in `pyproject.toml`.
3. Entry point under `[tool.poetry.scripts]` in `pyproject.toml` in the form `name.entry_script:function_name`.

## Packages included `pyproject.toml`

- python ^3.10
- click
- rich-click
- pyserde
- pydantic
- pre-commit
- pytest
- ruff