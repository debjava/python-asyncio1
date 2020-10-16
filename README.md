![DDLAB](./images/A22.png)
# Usage of AsyncIO in Python

# Technicalities
Usage of AsyncIO in Python

## Python Version

`py -V` or `python -V`

current python version: **3.7.4**

## How to create a virtual environment using pipenv

Open the command prompt and point to the project directory

Upgrade pip with the following command
```
py -m pip install --upgrade pip
```

Set the environment to create virtual environment in current project directory

```
set PIPENV_VENV_IN_PROJECT="enabled"
```

Install pipenv with the following command

```
pip install pipenv
```

If `pipenv` is already installed, skip this step.

Create the virtual environment with the following command

```
pipenv install
```

Activate the virtual environment

```
pipenv shell
```

you can execute any of the following commands to check the installed packages or dependencies and graph

```
pip list
    OR
pip freeze
    OR
pipenv graph
```

### How to run

In Eclipse or Pycharm, run the individual files to get the result

If you want to run from the command prompt, execute the following command

```
pipenv run <file name>
```

Conclusion
==========
Learn, explore more and share with all.

![DDLAB](./images/dd-logo.png)