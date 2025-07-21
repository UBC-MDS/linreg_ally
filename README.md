# linreg_ally

[![Documentation Status](https://readthedocs.org/projects/linreg-ally/badge/?version=latest)](https://linreg-ally.readthedocs.io/en/latest/?badge=latest) [![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-31111/) [![codecov](https://codecov.io/gh/UBC-MDS/linreg_ally/graph/badge.svg?token=JfomN9gPnY)](https://codecov.io/gh/UBC-MDS/linreg_ally)

## Overview of linreg_ally package:

This project delivers a Python package designed to help users determine if Ordinary Least Squares (“OLS”) regression is an appropriate model for their data. The package automates key steps, including performing OLS regression, data formatting checks, assumption validation, and multicollinearity detection, ensuring the data meets the prerequisites for a reliable model. By simplifying these essential tasks and providing clear diagnostics, the package empowers users to confidently assess the feasibility of linear regression and build accurate predictive models.

## Functions in linreg_ally package:

1.  `eda_summary`: This function uses the training set to check whether the data is formatted correctly to even run a linear regression model and returns a chart that shows the distribution of various features.

2.  `check_multicollinearity`: This function detects multicollinearity in the training dataset by computing the variance inflation factor (‘VIF’) and pairwise Pearson Correlation for each numeric feature.

3.  `run_linear_regression`: This function performs linear regression with preprocessing using sklearn and outputs evaluation scoring metrics.

4.  `qq_and_residuals_plot`: This function tests the normality of residuals and homoscedasticity assumptions for a linear regression model by creating the Q-Q and Residuals vs Fitted Values plots, respectively.

## How package fits in Python Ecosystem

linreg_ally provides an alternative to existing packages like [StatAssume](https://pypi.org/project/statsassume/), which automates model fitting, assumptions checking, and dashboard generation in a single function, and [lrasm](https://pypi.org/project/lrasm/), which provides specific functions that test certain key assumptions in OLS regression. linreg_ally differentiates itself by providing intuitive, user-friendly functions that guide users through every stage of training an OLS regression model – starting from explanatory data analysis and data preprocessing, progressing to model fitting and evaluating key assumptions in OLS regression.

## 🛠️ Setup Instructions

1.  **Clone the Project**

``` bash
git clone git@github.com:UBC-MDS/linreg_ally.git
cd linreg_ally
```

2.  **Install Dependencies**

``` bash
poetry install
```

3.  **Activate the Poetry Environment**

    Get the path to your virtual environment:

    ``` bash
    poetry env info --path
    ```

    Then activate it manually (replace the path with the output above):

    ``` bash
    source /Users/merarisantana/Library/Caches/pypoetry/virtualenvs/linreg-ally-xyz123-py3.11/bin/activate
    ```

4.  **Launch Jupyter Notebook**

    ``` bash
    jupyter notebook
    ```

    ## 📦 Importing the Package

    In a notebook cell, import the required functions:

    ``` bash
    import linreg_ally
    from linreg_ally.eda import eda_summary
    from linreg_ally.multicollinearity import check_multicollinearity
    from linreg_ally.models import run_linear_regression
    from linreg_ally.plotting import qq_and_residuals_plot
    from sklearn.model_selection import train_test_split
    ```

    For individual function usage, visit our [read the docs page](https://linreg-ally.readthedocs.io/en/latest/example.html) to see individual function usage.

## ✅ Running Tests

To run the tests, run the following commands from the root directory of this repo:

``` bash
pytest tests/
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

linreg_ally was created by Paramveer Singh, Merari Santana-Carbajal, Cheng Zhang, and Alex Wong. It is licensed under the terms of the MIT license.

## Credits

linreg_ally was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
