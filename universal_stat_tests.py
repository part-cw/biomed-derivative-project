from scipy import stats  
import pandas as pd


def ks_test(real_ds, syn_ds):
    cols = real_ds.columns 
    ks_tests = []

    for col in cols:
        real_ = real_ds[col]
        syn_ = syn_ds[col]
        try:
            s_ = stats.kstest(real_, syn_)
            ks_tests.append([col, s_[0], s_[1]])
        except Exception as e:
            print(f'{e} occurred in column {col}')

    return ks_tests


def t_test(real_ds, syn_ds):
    cols = real_ds.columns # what type?
    t_tests = []

    for col in cols:
        real_ = real_ds[col]
        syn_ = syn_ds[col]
        try:
            s_ = stats.ttest_ind(real_, syn_)
            t_tests.append([col, s_[0], s_[1]])
        except Exception as e:
            print(f'{e} occurred in column {col}')

    return t_tests