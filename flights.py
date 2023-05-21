#%%
import pandas as pd
import os

directory = 'data-analytics-files'

# for subdir, dirs, files in os.walk(rootdir):
#     for file in files:
#         print(file)

def create_df(directory):
    df_dict = {}
    for file in os.listdir(directory):
        filename = os.fsdecode(file) 
        file_path = os.path.join(directory,file)
        df_dict[filename.split(".")[0]] = pd.read_csv(file_path)
        break
    return df_dict

#%%
df_dict = create_df(directory)

#%%
#df_dict['1990'].isnull().sum()
#np_df = df_dict['1990'].dropna(subset=["phone number"])
def remove_null(df):
    null_columns = df.isna().all()
    print(len(df.columns))
    print(f'removing {len(null_columns[null_columns==True].index)} columns')
    df_clean = df.drop(columns= null_columns[null_columns==True].index)
    print(len(df_clean.columns))
    #(df_dict['1990'].isnull()).all(axis='columns').sum()
remove_null(df_dict['1990'])
#%%
np_df = df_dict['1990'].dropna(how='all')
#%%
len(np_df)
#%%
if __name__ == '__main__':
    directory = 'data-analytics-files'
    create_df(directory=directory)
    print(df_dict.keys())