# This is where we have all related to the tests we’re using. (k-test, ks-test, kulback-liebler test, etc.)

from scipy import stats  
import pandas as pd


def ks_test(real_ds, syn_ds):
    cols = real_ds.columns() 
    ks_tests = []

    for col in cols:
        real_ = real_ds[col]
        syn_ = syn_ds[col]
        try:
            ks_tests.append({col: stats.kstest(real_, syn_)})
        except Exception as e:
            print(f'{e} occurred in column {col}')

    return ks_tests


def t_test(real_ds, syn_ds):
    cols = real_ds.columns() 
    t_tests = []

    for col in cols:
        real_ = real_ds[col]
        syn_ = syn_ds[col]
        try:
            t_tests.append({col: stats.ttest_ind(real_, syn_)})
        except Exception as e:
            print(f'{e} occurred in column {col}')

    return t_tests