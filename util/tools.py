# This will have any function (you had to create) used to generate synthetic data. Maybe this script won’t be necessary at this stage.

import pandas as pd  
from sdv.tabular import CTGAN, GaussianCopula, CopulaGAN, TVAE
from synthpop import Synthpop


def gen_CTGAN(dataset, n_samples = 0):
    if n_samples == 0:
        n_samples = len(dataset)
    ctgan = CTGAN()
    ctgan.fit(dataset)
    synthetic_data = ctgan.sample(n_samples)
    synthetic_data.to_csv(f'syntheticData/ctgan_{n_samples}.csv', index=False)


def gen_GaussianCopula(dataset, n_samples = 0):
    if n_samples == 0:
        n_samples = len(dataset)
    gauscop = GaussianCopula()
    gauscop.fit(dataset)
    synthetic_data = gauscop.sample(n_samples)
    synthetic_data.to_csv(f'syntheticData/gauscop_{n_samples}.csv', index=False)


def gen_TVAE(dataset, n_samples = 0):
    if n_samples == 0:
        n_samples = len(dataset)
    tvae = TVAE()
    tvae.fit(dataset)
    synthetic_data = tvae.sample(n_samples)
    synthetic_data.to_csv(f'syntheticData/tvae_{n_samples}.csv', index=False)


def gen_SynthPop(dataset, n_samples = 0):
    if n_samples == 0:
        n_samples = len(dataset)

    my_data_types = {}
    for column in dataset.columns:
	    my_data_types[column] = 'float'
        
    spop = Synthpop()
    spop.fit(dataset, dtypes=my_data_types)
    synthetic_data = spop.generate(n_samples)
    synthetic_data.to_csv(f'syntheticData/synthpop_{n_samples}.csv', index=False)
