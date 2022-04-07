# This will have any function used to clean and preprocess the dataset
import pandas as pd

real = pd.read_csv('kag_risk_factors_cervical_cancer.csv')

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

real.to_csv('real_data.csv', index=False)