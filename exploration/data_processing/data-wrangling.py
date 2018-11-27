# import necessary packages
import pandas as pd
import os

# import raw data
raw_data = pd.read_csv('../data/student-mat.csv')

# convert binary variables to 0 & 1
mymap = {'school': {'MS': 0, 'GP': 1},
         'sex': {'M': 0, 'F': 1},
         'address': {'U': 0, 'R': 1},
         'famsize': {'LE3': 0, 'GT3': 1},
         'Pstatus': {'A': 0, 'T': 1},
         'schoolsup': {'no': 0, 'yes': 1},
         'famsup': {'no': 0, 'yes': 1},
         'paid': {'no': 0, 'yes': 1},
         'activities': {'no': 0, 'yes': 1},
         'nursery': {'no': 0, 'yes': 1},
         'higher': {'no': 0, 'yes': 1},
         'internet': {'no': 0, 'yes': 1},
         'romantic': {'no': 0, 'yes': 1}}

for col, mapping in mymap.items():
    raw_data[col] = raw_data[col].map(mapping)

    assert raw_data[col].max() == 1 and raw_data[col].min() == 0
    assert len(raw_data[col]) == 395

# engineer the improved variable
period1 = raw_data.G1
period2 = raw_data.G2
print(type(period1), type(period2))

improved_list = []

for n in period1 - period2:
    if n >= 0:
        improved_list.append(0)
    else:
        improved_list.append(1)

raw_data['improved'] = improved_list

assert raw_data['improved'].max() == 1 and raw_data['improved'].min() == 0
assert len(raw_data['improved']) == 395

# Remove missing target variable entries
cleaned_data = raw_data[~(raw_data['G3']==0)]

assert 0 not in cleaned_data['G3'].values
assert len(cleaned_data) == (395 - len(raw_data[raw_data['G3']==0]))

# export cleaned data to directory
cleaned_data.to_csv('cleaned-data.csv')

assert os.path.exists('./cleaned-data.csv')
