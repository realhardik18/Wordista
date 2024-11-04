import pandas as pd

def get_nth_word(n):
    df=pd.read_csv('db.csv')
    return list(list(df.iterrows())[100])

print(get_nth_word(10))
