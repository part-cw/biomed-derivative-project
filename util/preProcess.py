# This will have any function used to clean and preprocess the dataset
import pandas as pd


def data_preprocess(real):

    real = real[real['Number of sexual partners'] != '?']
    real['Number of sexual partners'] = real['Number of sexual partners'].astype('float') 

    real = real[real['First sexual intercourse'] != '?']
    real['First sexual intercourse'] = real['First sexual intercourse'].astype('float') 

    real = real[real['Num of pregnancies'] != '?']
    real['Num of pregnancies'] = real['Num of pregnancies'].astype('float')

    real = real[real['Smokes'] != '?']
    real['Smokes'] = real['Smokes'].astype('float') 

    real['Smokes (years)'] = real['Smokes (years)'].astype('float') 

    real['Smokes (packs/year)'] = real['Smokes (packs/year)'].astype('float') 

    real = real[real['Hormonal Contraceptives'] != '?']
    real['Hormonal Contraceptives'] = real['Hormonal Contraceptives'].astype('float') 

    real['Hormonal Contraceptives (years)'] = real['Hormonal Contraceptives (years)'].astype('float') 

    real = real[real['IUD'] != '?']
    real['IUD'] = real['IUD'].astype('float') 

    real = real[real['STDs'] != '?']
    real['STDs'] = real['STDs'].astype('float') 

    real = real[real['STDs (number)'] != '?']
    real['STDs (number)'] = real['STDs (number)'].astype('float') 

    real['STDs:condylomatosis'] = real['STDs:condylomatosis'].astype('float')

    real['STDs:cervical condylomatosis'] = real['STDs:cervical condylomatosis'].astype('float') 

    real['STDs:vaginal condylomatosis'] = real['STDs:vaginal condylomatosis'].astype('float') 

    real['STDs:vulvo-perineal condylomatosis'] = real['STDs:vulvo-perineal condylomatosis'].astype('float') 

    real['STDs:syphilis'] = real['STDs:syphilis'].astype('float') 

    real['STDs:pelvic inflammatory disease'] = real['STDs:pelvic inflammatory disease'].astype('float') 

    real['STDs:genital herpes'] = real['STDs:genital herpes'].astype('float') 

    real['STDs:molluscum contagiosum'] = real['STDs:molluscum contagiosum'].astype('float') 

    real['STDs:AIDS'] = real['STDs:AIDS'].astype('float') 

    real['STDs:HIV'] = real['STDs:HIV'].astype('float') 

    real['STDs:Hepatitis B'] = real['STDs:Hepatitis B'].astype('float') 

    real['STDs:HPV'] = real['STDs:HPV'].astype('float') 

    real.drop('STDs: Time since first diagnosis', inplace=True, axis=1)

    real.drop('STDs: Time since last diagnosis', inplace=True, axis=1)

    return real


real = pd.read_csv('kag_risk_factors_cervical_cancer.csv')
real_clean = data_preprocess(real)
real_clean.to_csv('C:/Users/Artem/Desktop/General/Biomed/datasets/clean/real.csv', index=False)


syn1 = pd.read_csv('C:/Users/Artem/Desktop/General/Biomed/datasets/synData.csv')
syn1_clean = data_preprocess(syn1)
syn1_clean.to_csv('C:/Users/Artem/Desktop/General/Biomed/datasets/clean/syn1.csv', index=False)


syn2 = pd.read_csv('C:/Users/Artem/Desktop/General/Biomed/datasets/synData-2.csv')
syn2_clean = data_preprocess(syn2)
syn2_clean.to_csv('C:/Users/Artem/Desktop/General/Biomed/datasets/clean/syn2.csv', index=False)


syn3 = pd.read_csv('C:/Users/Artem/Desktop/General/Biomed/datasets/synData-3.csv')
syn3_clean = data_preprocess(syn3)
syn3_clean.to_csv('C:/Users/Artem/Desktop/General/Biomed/datasets/clean/syn3.csv', index=False)


syn4 = pd.read_csv('C:/Users/Artem/Desktop/General/Biomed/datasets/synData-4.csv')
syn4_clean = data_preprocess(syn4)
syn4_clean.to_csv('C:/Users/Artem/Desktop/General/Biomed/datasets/clean/syn4.csv', index=False)


syn9 = pd.read_csv('C:/Users/Artem/Desktop/General/Biomed/datasets/synData9.csv')
syn9_clean = data_preprocess(syn9)
syn9_clean.to_csv('C:/Users/Artem/Desktop/General/Biomed/datasets/clean/syn9.csv', index=False)