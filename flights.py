#%%
import pandas as pd
import os

directory = 'data-analytics-files'

def create_df(directory):
    df_dict = {}
    for file in os.listdir(directory):
        filename = os.fsdecode(file) 
        file_path = os.path.join(directory,file)
        df_dict[filename.split(".")[0]] = pd.read_csv(file_path)
    return df_dict

#%%
df_dict = create_df(directory)

#%%

def remove_null(df):
    '''Remove any columns which are null across all rows'''
    null_columns = df.isna().all()
    print(f'original number of columns for {df} is {len(df.columns)}')
    print(f'removing {len(null_columns[null_columns==True].index)} columns')
    df_clean = df.drop(columns= null_columns[null_columns==True].index)
    print(len(df_clean.columns))
    
    return df_clean

def replace_null_to_zero(df):
    return df.fillna(0)

# Clean the data in each dataframe
for key in df_dict:
    df_dict[key] = remove_null(df_dict[key])
    df_dict[key] = replace_null_to_zero(df_dict[key])

#%%

# Integrate all cleaned dataframes into a single file
years_list = list(df_dict.keys())
df_integrate = df_dict[years_list[0]]

for i in years_list[1:]:
    df_integrate = pd.concat([df_integrate, df_dict[i]], join='inner', ignore_index=True)

#%%
# Export concatenated df into csv
os.makedirs('combined_data', exist_ok=True)
df_integrate.to_csv('combined_data/combined_data.csv', index=False)

#%%
#%%
# if __name__ == '__main__':
#     directory = 'data-analytics-files'
#     create_df(directory=directory)
#     print(df_dict.keys())