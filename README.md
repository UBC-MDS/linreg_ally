# linreg_ally

[![Documentation Status](https://readthedocs.org/projects/linreg-ally/badge/?version=latest)](https://linreg-ally.readthedocs.io/en/latest/?badge=latest)

## Overview of linreg_ally package:	 

This project delivers a Python package designed to help users determine if Ordinary Least Squares (“OLS”) regression is an appropriate model for their data. The package automates key steps, including performing OLS regression, data formatting checks, assumption validation, and multicollinearity detection, ensuring the data meets the prerequisites for a reliable model. By simplifying these essential tasks and providing clear diagnostics, the package empowers users to confidently assess the feasibility of linear regression and build accurate predictive models. 

## Functions in linreg_ally package: 

1. `eda_summary`: This function uses the training set to check whether the data is formatted correctly to even run a linear regression model and returns a chart that shows the distribution of various features. 

2. `check_multicollinearity`: This function detects multicollinearity in the training dataset by computing the variance inflation factor (‘VIF’) and pairwise Pearson Correlation for each numeric feature.  

3. `run_linear_regression`: This function performs linear regression with preprocessing using sklearn and outputs evaluation scoring metrics. 

4. `qq_and_residuals_plot`: This function tests the normality of residuals and homoscedasticity assumptions for a linear regression model by creating the Q-Q and Residuals vs Fitted Values plots, respectively. 


## How package fits in Python Ecosystem 

linreg_ally provides an alternative to existing packages like [StatAssume](https://pypi.org/project/statsassume/), which automates model fitting, assumptions checking, and dashboard generation in a single function, and [lrasm](https://pypi.org/project/lrasm/), which provides specific functions that test certain key assumptions in OLS regression. linreg_ally differentiates itself by providing intuitive, user-friendly functions that guide users through every stage of training an OLS regression model – starting from explanatory data analysis and data preprocessing, progressing to model fitting and evaluating key assumptions in OLS regression. 

## Installation

```bash
$ pip install linreg_ally
```

## Usage

Visit our [read the docs page](https://linreg-ally.readthedocs.io/en/latest/example.html) to see individual function usage.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`linreg_ally` was created by Paramveer Singh, Merari Santana-Carbajal, Cheng Zhang, Alex Wong. It is licensed under the terms of the MIT license.

## Credits

`linreg_ally` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
