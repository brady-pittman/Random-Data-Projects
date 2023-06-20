import pandas as pd 

data = pd.read_csv('C:\\Users\\602353\\Downloads\\FanGraphs Leaderboard (1).csv')

data_no_nan = data.dropna()

data_no_team = data_no_nan.drop(['Team', 'playerid', 'mlbamid'], axis=1)

data_no_team['K%'] = pd.to_numeric(data_no_team['K%'].str.replace('%',''))
data_no_team['BB%'] = pd.to_numeric(data_no_team['BB%'].str.replace('%',''))
data_no_team['GB%'] = pd.to_numeric(data_no_team['GB%'].str.replace('%',''))
data_no_team['Barrel%'] = pd.to_numeric(data_no_team['Barrel%'].str.replace('%',''))

data_no_team['Desirability Rate'] = data_no_team['K%'] + data_no_team['GB%'] - data_no_team['BB%'] - data_no_team['Barrel%']

data_sorted = data_no_team.sort_values(by='Desirability Rate', ascending=False)

average_rate = data_no_team['Desirability Rate'].mean()

print('Average Desirability Rate: {}'.format(average_rate))

print(data_sorted.head())
