

import pandas as pd

# structure will be Read, Ref, RefStart

data = pd.read_csv('/Users/ep9k/Desktop/sandeep.test.tsv', sep='\t', header=0)
data.rename(columns={'R000042507:ENST00000368744.3-ENST00000446080.2': 'Read', 
                    'ENST00000256646.2:ENSG00000134250.13xENST00000448873.2:ENSG00000163386.16,309#971': 'Ref',
                    '75': 'ReadStart',
                    '150': 'ReadStop',
                    '3398': 'RefStart',
                    '3473': 'RefStop'}, 
          inplace=True)

# get unique values from 'Read' column
unique_read_vals = data['Read'].unique().tolist()
# print('UNIQUE READ COLUMN VALUES', unique_read_vals)

######CHANGE ME#######
#choose unique value from unique_read_vals
my_read_val = 'R000042507:ENST00000368744.3-ENST00000446080.2'

# make subset of dataframe using my_read_value
unique_read_df = data.loc[data['Read'] == my_read_val]
#get unique values of subset from 'Ref' column
# print('UNIQUE REF COLUMN VALUES BASED ON READ COLUMN CHOICE', unique_read_df['Ref'].unique().tolist())

######CHANGE ME#######
#choose unique value from 'Ref' column
my_ref_val = 'ENST00000602566.1:ENSG00000134250.13xENST00000464433.2:ENSG00000163386.16,309#1080'

#make subset of dataframe using my_ref_value
unique_ref_df = data.loc[(data['Read'] == my_read_val) & (data['Ref'] == my_ref_val)]

#get unique values from 'RefStart' column based on subset
# print('UNIQUE REFSTART COLUMN VALUES BASED ON READ AND REF COLUMN CHOICE', unique_ref_df['RefStart'].unique().tolist())

######CHANGE ME#######
#choose unique value from 'RefStart' column
my_refstart_val = 3220

#make subset of dataframe based on my_refstart_value
unique_refstart_df = data.loc[(data['Read'] == my_read_val) & (data['Ref'] == my_ref_val) & (data['RefStart'] == my_refstart_val)]

#######FINAL RESULTS######
#print 'ReadStart', 'ReadStop', 'RefStop' values in list based on these choices
results_in_list = unique_refstart_df[['ReadStart', 'ReadStop', 'RefStop']].values.tolist()
print('FINAL RESULTS')
print(results_in_list)








