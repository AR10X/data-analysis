import pandas as pd
## Skipped the first 28 lines
df=pd.read_csv("WeatherData.csv",skiprows=28,parse_dates=[0],header=0)
df = df.drop_duplicates()
# df = df.loc[:,~df.columns.duplicated()]
df.drop('Date1', axis=1, inplace=True)
year = 2022
df["Date"][0] = "'" + str(year) + df['Date'][0][4:] + "'"

for i in range(1, len(df)):
    curr_month = int(df['Date'][i][5:7])
    prev_month = int(df['Date'][i-1][6:8])
    if curr_month < prev_month:
        year += 1
    df['Date'][i] = "'" + str(year) + df['Date'][i][4:]
cols = df.columns.tolist()
print(cols)
for i, col in enumerate(cols):
    if '(' in col:
        cols[i] = col + ")"
df.columns = cols 

df.to_csv('weather_dataset_v2.csv' , encoding='utf-8', index=False) 
