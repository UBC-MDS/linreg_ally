# Author: Paramveer Singh
# test_eda.py
# 15 January 2025

import pytest
import altair as alt
import pandas as pd
from vega_datasets import data
from linreg_ally.eda import eda_summary

@pytest.fixture
def iris_data():
    """
    Returns good data for expected use case
    """
    return data.iris()

@pytest.fixture
def mismatched_type():
    """
    Returns test data with a binary variable as type int instead of categorical
    """
    mismatched_type = pd.DataFrame({
        'x': [i/10 for i in range(10)],
        'y': [2*i/10 for i in range(10)],
        'binary': [0, 1, 0, 0, 0, 1, 0, 1, 1, 1]
    })

    # Ensure type is int instead of object or categorical
    mismatched_type['binary'] = mismatched_type['binary'].astype(int)

    return mismatched_type

@pytest.fixture
def empty_df():
    """
    Returns empty DataFrame with no data inside
    """
    return pd.DataFrame({
        'x': [],
        'y': [],
        'species': []
    })

@pytest.fixture
def not_df():
    """
    Returns a dictionary instead of a DataFrame
    """
    return {
        'x': [1, 2, 3, 4],
        'y': [1, 2, 4, 5]
    }

def test_good_data_no_color(iris_data):
    """
    Test expected use case when given no `color` parameter
    """
    # Store result
    plot = eda_summary(iris_data)

    # Assert output type
    assert isinstance(plot, alt.ConcatChart), 'Function does not return correct type!'

    # Assert x's are correct
    feature_names = iris_data.columns.tolist()
    feature_names.remove('species')

    feats_used = []
    for i in range(len(plot.concat)):
        feats_used.append(plot.concat[i].layer[0].encoding.x.shorthand)

    assert set(feature_names) == set(feats_used), 'All x variables are not used!'

def test_good_data_color(iris_data):
    """
    Test expected use case when `color` parameter is given
    """
    # Store result
    plot = eda_summary(iris_data, color='species')

    # Assert output type
    assert isinstance(plot, alt.ConcatChart), 'Function does not return correct type!'

    # Assert x's are correct
    feature_names = iris_data.columns.tolist()
    feature_names.remove('species')

    feats_used = []
    for i in range(len(plot.concat)):
        feats_used.append(plot.concat[i].layer[0].encoding.x.shorthand)

    assert set(feature_names) == set(
        feats_used), 'All x variables are not used!'

    # Assert color is `species`
    assert (plot
            .concat[0]
            .layer[0]
            .encoding
            .color
            .shorthand == 'species'), 'The wrong column is used for coloring!'

def test_incorrect_feat_type(mismatched_type):
    """
    Tests edge case for when the `color` parameter refers
    to a non-object or non-categorical feature
    """
    # Store result
    plot = eda_summary(mismatched_type, color='binary')

    # Assert output type
    assert isinstance(plot, alt.ConcatChart), 'Function does not return correct type!'

    # Assert color is 'binary'
    assert (plot
            .concat[0]
            .layer[0]
            .encoding
            .color
            .shorthand == 'binary'), 'The wrong column is used for coloring!'

    # Assert color is nominal type
    assert (plot.to_dict()['concat'][0]['layer'][0]['encoding']['color']
            ['type'] == 'nominal'), 'Column dtype conversion failed!'


def test_nonexistent_name(mismatched_type):
    """
    Tests edge case for when the `color` parameter does
    not exist in the DataFrame
    """
    with pytest.raises(KeyError):
        eda_summary(mismatched_type, 'Binary')

def test_empty_df(empty_df):
    """
    Tests edge case for when the DataFrame is empty but has column names
    """
    # Store results
    plot = eda_summary(empty_df, 'species')

    # Assert output type is correct
    assert isinstance(plot,
                      (alt.Chart, alt.ConcatChart)), 'Function did not return correct type!'

def test_not_df(not_df):
    """
    Tests error case for when the input is not a DataFrame
    """
    with pytest.raises(TypeError):
        eda_summary(not_df)

def test_not_str(iris_data):
    """
    Tests error case for when the input `color` parameter is not a string
    """
    with pytest.raises(TypeError):
        eda_summary(iris_data, ['species'])
