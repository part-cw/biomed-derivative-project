import numpy as np
import scipy.stats as stats
import math

def ks_test(real, syn):
    # mistake in KS TEST !!!
    # fixing
    real = np.sort(real)
    syn = np.sort(syn)
    all_data = np.sort(np.concatenate((real, syn)))
    #

    real_data_cdf = [np.round(stats.percentileofscore(real, value)/100, 1) for value in all_data]
    syn_data_cdf = [np.round(stats.percentileofscore(syn, value)/100, 1) for value in all_data]
    abs_diff = np.abs(np.subtract(real_data_cdf, syn_data_cdf))
    D_n = max(abs_diff)
    D_crit = 1.36*np.sqrt(1/len(real)+1/len(syn))

    return [D_n, D_crit]


def t_test(real, syn, alpha=0.05):
    mean1, mean2 = syn.mean(), real.mean()
    std1, std2 = syn.std(), real.std()
    n1, n2 = len(syn), len(real)
    se1, se2 = std1/math.sqrt(n1), std2/math.sqrt(n2)
    sed = math.sqrt(se1**2+se2**2)
    t_stat = (mean1-mean2)/sed   
    df = n1+n2-2
    crit = stats.t.ppf(1.0-alpha, df)
    p_val = (1- stats.t.cdf(abs(t_stat), df))*2

    return [t_stat, crit, p_val]


def X2_test(real, syn):
    observed = syn   
    real_ratios = real/len(real)
    expected = real_ratios*len(syn)
    chi_squared_stat = (((observed-expected)**2)/expected).sum()
    crit = stats.chi2.ppf(q=0.95, # 95% confidence level,
                         df=4)  # 4 degrees of freedom, number of variable catergories - 1
    p_value = 1 - stats.chi2.cdf(x=chi_squared_stat,
                                df=4)

    return [chi_squared_stat, crit, p_value]