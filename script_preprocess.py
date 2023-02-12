import pandas as pd

df = pd.read_excel("weather_dataset_stage1.xls", skiprows=28)
#subtask2
df = df.drop_duplicates()
df = df.loc[:,~df.columns.duplicated()]
df.drop('Date1', axis=1, inplace=True)


# Fixing the year of Date & Date1 column subtask 1
year = 2022
df['Date'][0] = "'" + str(year) + df['Date'][0][4:] + "'"
for i in range(1, len(df)):
    curr_month = int(df['Date'][i][5:7])
    prev_month = int(df['Date'][i-1][6:8])
    if curr_month < prev_month:
        year += 1
    df['Date'][i] = "'" + str(year) + df['Date'][i][4:]
    print(year)


# Fixng labels subtask3
cols = df.columns.tolist()
for i, col in enumerate(cols):
    if '(' in col:
        cols[i] = col + ")"
df.columns = cols

print(df.columns)

df.to_excel('weather_dataset_v2.xlsx', index=False)

df.to_csv('weather_dataset_v2.csv', encoding='utf-8', index=False)