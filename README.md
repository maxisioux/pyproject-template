# Python Sample Project

The repository is actually empty, only configuration can be used to execute any project you want.

This python sample project template provides a simplified starting point for your next project. Using [poetry](https://python-poetry.org/docs/) for dependency management can ensure that you have the right tools to obtain it. The automatic linking with Ruff maintains code quality, while the included testing framework (Pytest) and VS code configuration accelerate development. Encode faster through this pre configured setting, save valuable time, and ensure a solid foundation for your Python project.

## Installing a python sample project

This tutorial will guide you through the steps of creating a basic project fork using basic configuration in Python and configuring it in a local environment.

## Provide the option "Use this template" in the upper right corner

Clicking this button will allow you to use the repository as the basis for launching your repository. Then clone it to the local machine

```bash
git clone https://github.com/codemaxi520/python-sample-project.git
cd python-sample-project
```

## Configure virtual environment

To work in a virtual environment, we will use [miniconda](https://docs.anaconda.com/free/miniconda/index.html).

```bash
# 先这样安装才能全局使用poetry
pip3 install poetry
poetry --version # Poetry (version 1.8.2)
# 用conda创建虚拟python环境
conda create -n my_env python=3.10 -y
# 激活环境
conda activate my_env
# 安装当前需要的依赖
poetry install --no-root
```

## **Install Dependencies**

This project uses poetry to handle dependency relationships. By using `poetry install --no-root`, it is possible to avoid installing projects in editable mode, which means that the current project will not be installed as a dependency.

Using `--no-root` during project development is very useful as it avoids adding the current project as an editable dependency, which may lead to version issues or conflicts with installed dependencies.

```bash
poetry install --no-root
```

# Files in the project

## .github/workflows/linter.yml
The `.github/workflows/linter.yml` file contains the configuration of the github operation workflow. This workflow will run in the 'Push' and 'Pull-Request' events.

### File purpose:

-**Workflow Name:** `Ruff`
-**Activation events:** `Push` and `Pull-Request`

### Workflow description:

- **Assignment:** Define a task named "ruff".
- **Runtime:** Specify the runtime environment as "Ubuntu Latest".
- **Steps:** are the steps that must be followed for this job.
- Action/ checkout@v3 `This operation is used to clone a repository in the runtime environment.
- `Chartboost/ruff-action@v1`: Use an operation called "run action" provided by the "ChartBoost" repository. This operation executes a flashlight to check for any issues in the code and apply corrections if possible.
- **Parameters used:**
- `Check`: Instruct the flashlight to check the code.
- "-- fix only": Automatically apply corrections only when safe.
- "-- unsafe fixes": Make corrections that are not completely safe but deemed appropriate.
- "-- Show Fixes": displays the correction of the application.

### The purpose of workflow:

This workflow uses the 'run action' action to execute a flashlight in the code. Check the code for any issues with the flashlight and apply automatic corrections if possible. This helps to maintain code cleanliness and consistency in the repository.

## .vscode/extension.json
The. vscode/extension.json file contains extension suggestions for Visual Studio code, which are considered useful for this specific project.
### File Description:

-Suggestion: This is a recommended list of extensions for Visual Studio code.
-Each element in the list is a unique name for the available extensions in the VS Code market.

### File purpose:
This file provides extension suggestions to help developers working on this project improve their experience using Visual Studio code. The listed extensions can be used for tasks such as code formatting, spell checking, support for different languages, and other functions that may be related to project development.

## .vscode/settings.json
The. vscode/settings. json file contains Visual Studio code specific configurations suitable for using Python projects and some related tools.

### File purpose:

This file defines Python specific configuration preferences for Visual Studio code. Configuration includes specific settings for automatic formatting, use of linking and spell checking tools, and code and document analysis. These configurations can help maintain code cleanliness and improve efficiency during project development.

## Environmental examples
The file `.env.example` displays an example of how to build environment variables for a project, although these variables are not currently actively used. It serves as a guide on how to configure environment variables in Python projects.

As a good security practice, sensitive values such as passwords or database access paths should not be directly included in the source code or repository. On the contrary, it is recommended to securely store these environment variables using a file named '. env'.

This file `.env` has been omitted in version control (for example, adding it to the file `.gitignore`) to avoid exposing sensitive information in the public repository.

### The purpose of the file `.env.example`:
Although the project currently does not require the use of environment variables, this file can serve as a guide for future development. Students can use this example as a reference to configure the required environmental variables for different environments (development, testing, production) in the future stages of the project. This promotes good security practices and separates sensitive configurations from source code.

## .gitignore
The. gitignore file is essential in any project controlled by git. Allow you to specify files and directories that Git must ignore and should not be tracked or included in the repository.

### The purpose of the file `.gitignore` is:
The. gitIgnore file ensures that certain files and directories are not accidentally included in version control, which helps maintain the cleanliness and organization of the repository. This is particularly useful for automatically generated files, local environment dependencies, and other files that are not important to the repository itself.

## License
A license determines how others use, modify, and share your work. The MIT license is one of the popular choices in the open source world.

### The purpose of an open source license is:

The license in open source projects specifies the terms and conditions under which the software can be used, modified, redistributed, or even re licensed by other developers. They define the rights and limitations applicable to the software.

Especially the MIT license is known for its tolerance. It allows users to modify, distribute, and use software for any purpose, including commercial projects, provided that copyright and original license statements are included in the code.

### Suggestions and remedial measures:

Website [Select License](https://choosealicense.com/)It is an excellent source for exploring and understanding available open source licenses. It provides detailed information about various licenses, including their terms, limitations, and recommendations on when and how to use them.

The MIT Select License page provides a clear understanding of what the license allows and how it affects your project.

The recommendation for a MIT license is a joint decision of those who wish for its code to be widely used and modified by other developers, while maintaining considerable flexibility in usage and distribution.

## Pyproject.toml
The `pyproject.toml` file contains project configuration, including dependencies, development tools, and configuration specific to Linter, code formatter, and static validation types.

### File Description:

-`tool.poetry`: Use poetry to configure project dependencies.
-`tool.ruff`: Set the `ruff` of the flashlight to check and maintain code.
-`tool.black`: black code formatting program settings.
-`tool.mypy`: Configuration of `mypy` type static validator.

### File purpose:

This file is crucial for project configuration. Define dependencies, development tools, and configurations specific to Linter, code formatter, and static validation. It helps to keep the code clean, consistent, and error free.

The current configuration in `pyproject.toml`
Let's analyze certain specific parts of the `pyproject.toml` file to better understand its functionality:

#### `[Tools.poetry]` section:
poetry is a dependency management and packaging tool for Python projects. The `pyproject.toml` file is crucial for its operation as it contains the information needed to manage project dependencies and configurations. Your [official document](https://python-poetry.org/docs/)

```toml
[tool.poetry]
name = "python-sample-project"
version = "0.1.0"
description = "python-sample-project"
authors = ["Sioux <codemaxi@163.com>"]
readme = "README.md"
license="MIT"
repository = "https://github.com/codemaxi520/python-sample-project.git"
documentation = "https://github.com/codemaxi520/python-sample-project/blob/master/README.md"
packages = [{include = "root_package_name"}]
```

- `name`: Project name.
- `version`: The current version of the project.
- `description`: A brief description of the project.
- `authors`: List of project authors.
- `license`: The license for distributing projects.
- `readme`: The name of the associated readme file.
- `repository`: The URL of the project repository.
- `documentation`: The URL of the document related to the project.
- `packages`: The root source code dir

#### Partial `[tool.poetry.dependency]` and `[tool.poetry.group.dev.dependency]`:

These sections contain project dependencies categorized by category.

- `[tool.poetry.dependencies]`: Contains the main dependencies of the project.
- `[tool.poetry.group.dev.dependencies]`: Contains development dependencies used during project development.


#### `[Build System]` section:
```toml
[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

- `requires`: List of dependency relationships required to build the system (in this case, poetry).
- `build-backend`: poetry is used to build the backend of a project.

### The purpose of the poem in `pyproject.toml` is:

- **Dependency Management**: Manage project dependencies (third-party libraries, development tools, etc.) specified in the `Dependencies` and `group.dev.dependencies` sections.
- **Project Management**: Provide relevant project information, such as name, version, description, author, license, etc.
- **Project Packaging**: Helps package projects for distribution and release.

poetry simplifies dependency management and Python project management, providing a unified and efficient approach.

#### Partial '[Tools.ruff]':

Ruff is a linking tool in Python that helps keep code clean, consistent, and error free. It is used to identify and correct style issues, coding conventions, common errors, and possible improvements in Python code. Your [official document](https://docs.astral.sh/ruff/linter/)

```toml
[tool.ruff]
lint.ignore = ["B008", "RUF012"]
line-length = 100
lint.select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    "C",   # flake8-comprehensions
    "B",   # flake8-bugbear
    "SIM", # flake8-simplify
    "TCH", # flake8-type-checking
    "TID", # flake8-tidy-imports
    "Q",   # flake8-quotes
    "UP",  # pyupgrade
    "PT",  # flake8-pytest-style
    "RUF", # Ruff-specific rules
]
```

- `lint.ignore`: A list of rules to be ignored by lantern circles during code validation.
- `line-length`: The maximum allowed line length.
- `lint.select`: A set of rules or validation categories that will be activated for RUFF.

#### Partial `[tools.black]`:

`black` is a Python code formatter. Its main goal is to ensure consistency in Python code style. It is used to automatically format code based on a set of predefined rules, which helps maintain a consistent and readable style throughout the entire project. Your [official document](https://black.readthedocs.io/en/stable/)

```toml
[tool.black]
line-length = 100
target-version = ['py311']
```

- `line-length`: Set the maximum allowed line length for `black`.
- `target-version`: Define the Python version targeted by the Black formatter.

#### Partial `[tool.mypy]`:

`mypy` is a static type validation tool for Python. Allow adding type comments in the code and verifying that variables and functions are used correctly based on these types. It helps identify type errors before code execution. Your [official document](https://mypy.readthedocs.io/en/stable/)

```toml
[tool.mypy]
python_version = "3.11"
strict = true
check_untyped_defs = false
explicit_package_bases = true
warn_unused_ignores = false
exclude = ["tests"]
```

- `python_version`: specifies the Python version that uses `mypy` for type checking.
- `strict`: Enable mypy's strict mode, where type checking is more stringent.
- `check_untyped_defs`: Define whether to check for definitions without a type.
- `explicit_package_bases`: Forces specifying package bases in a class.
- `warn_unused_ignores`: Control whether warnings about ignored types should be displayed.
- `exclude`: A list of directories or files excluded from the `mypy` type check.

These parts are crucial for configuring development tools such as Ruff, Black, and `mypy`. Everyone has defined specific rules, behaviors, and settings to ensure code consistency and quality.

# Using poetry to modify dependency relationships:

To add new dependencies to a project, you can use the 'poetry Add' command. This will add dependencies to the 'pyproject.toml' file.

## Main units:

```bash
poetry add name_package
```

This will add `name_package` as the primary dependency in the `[tool.poetry.dependencies]` block of `pyproject.toml`.

## Development stocks:

```bash
poetry add name_package --group dev
```

This will add `name_package` as a development dependency in the `[tool.poetry.group.dev.dependencies]` block of `pyproject.toml`.

## Delete dependency:

To remove dependencies from the project, you can use the `poetry remove` command.

### Delete main dependencies:

```bash
poetry remove name_package
```
This will remove `name_package` from the main dependencies in `pyproject.toml`.

### Delete development dependency:

```bash
poetry remove --dev name_package
```

This will remove `name_package` from the development dependencies in `pyproject.toml`.

## Update dependencies:

To update dependencies, you can use the `poetry update` command.

## Update all dependencies:

```bash
poetry updates
```

This will update all dependencies to their latest compatible version and adjust the `pyproject.toml` file accordingly.

These commands enable you to effectively manage project dependencies, add new dependencies, delete unwanted dependencies, and update to the latest compatible version.
