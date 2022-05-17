# This is where the code to generate a histogram, a cumulative, etc. is stored.
import numpy as np 
import matplotlib.pyplot as plt
import string
import os


def plot_cumsum(real, fake, real_name=None, fake_name=None, cols=None, save=True, show=True):
    if cols is None:
        cols = list(real.columns)
    else:
        cols = cols


    for col in cols:
        #print(real[col].dtypes)
        if not (real[col].dtypes == np.int64 or real[col].dtypes == np.float64):
            print(f'The type of {col} isn\'t int or float')
            continue

        # calculating cummulative sums
        real_ = real[col].sort_values()
        real_.reset_index(drop=True, inplace=True)
        real_cummsum = real_.cumsum()

        fake_ = fake[col].sort_values()
        fake_.reset_index(drop=True, inplace=True)
        fake_cummsum = fake_.cumsum()
        fake_cummsum = fake_cummsum[:len(real_cummsum)]

        # plotting

        x1 = [i for i in range(len(real_cummsum))]
        x2 = [i for i in range(len(fake_cummsum))]

        plt.figure(figsize=(6, 6))
        plt.title(col)
        plt.scatter(x1, real_cummsum, alpha=0.5)
        plt.scatter(x2, fake_cummsum, alpha=0.5)
        plt.legend(labels=[f'{real_name} {col}', f'{fake_name} {col}'])

        if save:
            if real_name is None or fake_name is None:
                print('Add real_name and fake_name parameters to save plots')
            col_name = col.translate(str.maketrans('', '', string.punctuation))
            
            
            path='plots/'+real_name+'_'+fake_name+'_cumsums'
            if os.path.isdir(path) == False:
                print(os.path.isfile(path))
                os.mkdir(path)
            
            plt.savefig(f'{path}/{col_name}.png')

        if show:
            plt.show()



def plot_histograms(real, fake, real_name=None, fake_name=None, cols=None, save=True, show=True):
    if cols is None:
        cols = list(real.columns)
    else:
        cols = cols


    for col in cols:
        #print(real[col].dtypes)
        if not (real[col].dtypes == np.int64 or real[col].dtypes == np.float64):
            print(f'The type of {col} isn\'t int or float')
            continue

        real_ = real[col]

        fake_ = fake[col]

        # plotting

        plt.figure(figsize=(8, 8))
        plt.hist(real_, alpha=0.8, density=True)
        plt.hist(fake_, alpha=0.5, density=True)
        plt.legend(labels=[f'{real_name} {col}', f'{fake_name} {col}'])

        if save:
            if real_name is None or fake_name is None:
                print('Add real_name and fake_name parameters to save plots')
            col_name = col.translate(str.maketrans('', '', string.punctuation))
            
            
            path='plots/'+real_name+'_'+fake_name+'_histograms'
            if os.path.isdir(path) == False:
                print(os.path.isfile(path))
                os.mkdir(path)
            
            plt.savefig(f'{path}/{col_name}.png')

        if show:
            plt.show()