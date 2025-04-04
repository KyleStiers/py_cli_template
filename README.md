# Python Click App Template

This repo is boilerplate for quickly creating Python click applications. It assumes the use of [uv](https://docs.astral.sh/uv/). Click "Use this template" to create a new repo using this framework.

With your new repo pulled and ready to go:

1. Rename the `pycli` directory to whatever you want your package to be called
2. Edit the `[project]` metadata in the [pyproject.toml](pyproject.toml) file
3. Edit the `[project.scripts]` section to fit your needs. Remember the `pycli` is the core command of your CLI and the `"pycli.cli:cli"` portion is the entrypoint.

From there you're ready to `uv sync` and you should be good to go for starting dev on your CLI application!

## Packages included `pyproject.toml`

- python ^3.12
- click
- rich-click
- pyserde
- pydantic
- ruff

These are a good starting point for all python projects in my opinion. To add new dependencies use `uv add <package>` and to remove `uv remove <package>`.

## Optionals

An empty `.envrc` is kept to remind myself of integrations possible with [direnv](https://direnv.net/).

Pytest and pre-commit hooks are set up as optional dependencies and can be included with `uv sync --extra test`. To initialize pre-commit hooks, check the `.pre-commit-hooks.yaml` file, and then do `pre-commit install` to have each commit checked.

## Extra Indexes

If you need to pull things from private registries such as Artifactory check out the [uv indexes](https://docs.astral.sh/uv/configuration/indexes/) docs. You can either set up a `uv.toml` file, define them explicitly in your `pyproject.toml`, or use the many [UV environment variables](https://docs.astral.sh/uv/configuration/environment/), or pass them at installation time via `--extra-index-url`. There are probably other options as well!
