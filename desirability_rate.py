import pandas as pd 

data = pd.read_csv('C:\\Users\\602353\\Downloads\\FanGraphs Leaderboard (2015+).csv')

data_no_nan = data.dropna()

data_no_team = data_no_nan.drop(['Team', 'playerid', 'mlbamid'], axis=1)

data_no_team['K%'] = pd.to_numeric(data_no_team['K%'].str.replace('%',''))
data_no_team['BB%'] = pd.to_numeric(data_no_team['BB%'].str.replace('%',''))
data_no_team['GB%'] = pd.to_numeric(data_no_team['GB%'].str.replace('%',''))
data_no_team['Barrel%'] = pd.to_numeric(data_no_team['Barrel%'].str.replace('%',''))
data_no_team['Hard%'] = pd.to_numeric(data_no_team['Hard%'].str.replace('%',''))
data_no_team['Soft%'] = pd.to_numeric(data_no_team['Soft%'].str.replace('%',''))

data_no_team['Desirability Rate'] = data_no_team['K%'] + data_no_team['GB%'] + data_no_team['Soft%'] - data_no_team['Hard%'] - data_no_team['BB%'] - data_no_team['Barrel%']

data_sorted = data_no_team.sort_values(by='Desirability Rate', ascending=False)

average_rate = data_no_team['Desirability Rate'].mean().round(1)

print(data_no_team.loc[data_no_team['Name'] == 'Chris Sale', ['Name', 'Desirability Rate']])
print()

print('Average Desirability Rate: {}'.format(average_rate))
print()

pd.set_option('display.max_columns', 2)

print(data_sorted.head())
