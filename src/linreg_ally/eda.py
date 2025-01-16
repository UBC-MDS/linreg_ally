# Author: Paramveer Singh
# eda.py
# 01/09/2025

import altair_ally as aly
import altair as alt
import pandas as pd

def eda_summary(train_df: pd.DataFrame, color: str = None) -> alt.ConcatChart:
    """
    Does preliminary exploratory data analysis (EDA) on dataset
    to return plots to the user

    Parameters
    ----------
    train_df : pd.DataFrame
        Training dataset
    color : str, default None
        Column name in `train_df` to be used for coloring the data

    Returns
    -------
    alt.ConcatChart
        A chart that shows the distributions of various input features

    Raises
    ------
    KeyError
        When `color` is not in the `train_df` columns
    TypeError
        When either `train_df` or `color` is not the expected type
    ValueError
        When column conversion dtype in `train_df` fails

    Examples
    --------
    >>> from linreg_ally.eda import eda_summary
    >>> summary_chart = eda_summary(train_df, color='y')
    >>> summary_chart.show()        
    """
    # Run type checks
    if not isinstance(train_df, pd.DataFrame):
        raise TypeError(f'train_df needs to be a Pandas DataFrame and not {type(train_df)}')
    if not isinstance(color, str) and color is not None:
        raise TypeError(f'color needs to be a string or None and not {type(color)}')

    return aly.dist(train_df, color=color)
