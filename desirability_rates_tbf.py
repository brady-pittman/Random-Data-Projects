import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mplcursors

plt.style.use('ggplot')

data = pd.read_csv('C:\\Users\\602353\\Downloads\\FanGraphs Leaderboard (TBF).csv')
data_no_nan = data.dropna()
data_no_team = data_no_nan.drop(['Team', 'playerid', 'mlbamid'], axis=1)
data_no_team['K%'] = pd.to_numeric(data_no_team['K%'].str.replace('%',''))
data_no_team['BB%'] = pd.to_numeric(data_no_team['BB%'].str.replace('%',''))
data_no_team['GB%'] = pd.to_numeric(data_no_team['GB%'].str.replace('%',''))
data_no_team['Barrel%'] = pd.to_numeric(data_no_team['Barrel%'].str.replace('%',''))
data_no_team['Hard%'] = pd.to_numeric(data_no_team['Hard%'].str.replace('%',''))
data_no_team['Soft%'] = pd.to_numeric(data_no_team['Soft%'].str.replace('%',''))
league_average_tbf = data_no_team['TBF'].mean()
tbf_deviation = data_no_team['TBF'] - league_average_tbf
data_no_team['Desirability Rate'] = (data_no_team['K%'] + data_no_team['GB%'] + data_no_team['Soft%']) - (data_no_team['BB%'] + data_no_team['Barrel%'] + data_no_team['Hard%']) + (0.04 * tbf_deviation).round(1)
average_rate = data_no_team['Desirability Rate'].mean().round(1)

fig, ax = plt.subplots(figsize=(10, 8))
scatter = ax.scatter(data_no_team['Desirability Rate'], data_no_team['TBF'], alpha=0.6, c='royalblue', edgecolors='gray')

z = np.polyfit(data_no_team['Desirability Rate'], data_no_team['TBF'], 1)
p = np.poly1d(z)
plt.plot(data_no_team['Desirability Rate'], p(data_no_team['Desirability Rate']), "r--", linewidth=1)

ax.set_xlabel('Desirability Index', fontsize=12)
ax.set_ylabel('Total Batters Faced', fontsize=12)
ax.set_title('TBF vs. Desirability Index', fontsize=14)
ax.grid(True, linestyle='--', alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis='both', which='both', labelsize=10)

top_3 = data_no_team.nlargest(3, 'Desirability Rate')
bottom_3 = data_no_team.nsmallest(3, 'Desirability Rate')

for i, player in top_3.iterrows():
    ax.annotate(player['Name'], (player['Desirability Rate'], player['TBF']), xytext=(10, -10),
                textcoords='offset points', color='green', fontsize=10)

for i, player in bottom_3.iterrows():
    ax.annotate(player['Name'], (player['Desirability Rate'], player['TBF']), xytext=(10, -10),
                textcoords='offset points', color='darkorange', fontsize=10)

cursor = mplcursors.cursor(hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(f"{data_no_team.loc[sel.target.index]['Name']} - {data_no_team.loc[sel.target.index]['Desirability Rate']:.1f}"))

ax.scatter(average_rate, league_average_tbf, color='gold', marker='o', s=100, edgecolors='black', label='Average')
ax.annotate(f'Average: {average_rate}', (average_rate, league_average_tbf), xytext=(10, -10), textcoords='offset points',
             color='black', fontsize=12)

ax.legend(loc='upper left', fontsize=10)

ax.set_xlim([data_no_team['Desirability Rate'].min() - 1, data_no_team['Desirability Rate'].max() + 1])
ax.set_ylim([data_no_team['TBF'].min() - 100, data_no_team['TBF'].max() + 100])

plt.tight_layout()
plt.show()

