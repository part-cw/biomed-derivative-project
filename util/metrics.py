# This is where we have all related to the tests we’re using. (k-test, ks-test, kulback-liebler test, etc.)

from scipy import stats  
import pandas as pd
import math


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


def kl_divergence(p, q):
	return sum(p[i] * math.log2(p[i]/q[i]) for i in range(len(p)))

def kl_divergence_test(real_ds, syn_ds):
    cols = real_ds.columns
    kl_divs = []

    for col in cols:
        real_prob_ = (real_ds[col]+math.pow(10, -9))/(real_ds[col].sum()+len(real_ds)*math.pow(10, -9))
        syn_prob_ = (syn_ds[col]+math.pow(10, -9))/(syn_ds[col].sum()+len(real_ds)*math.pow(10, -9))
        try:
            score = kl_divergence(real_prob_, syn_prob_)
            kl_divs.append([col, score])
        except Exception as e:
            print(f'{e} occurred in column {col}')

    return kl_divs