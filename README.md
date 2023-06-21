# Random-Data-Projects
Collection of random data projects

## degrom_data
Messing around with graphs and data from statcast, focused on Jacob deGrom

## desirability_rate
6/20/2023: (K+GB+Soft) - (BB+Barrel's+Hard) rate of MLB Pitchers. Can be done year by year too, just have to download the specific tables from fangraphs. Preliminary.

## desirability_rate_tbf
(K+GB+Soft) - (BB+Barrel's+Hard) + (0.04 * tbf_deviation) same as desirability_rate, but with a slight bonus or penalty for batters faced compared to the league average. This is for one year, change the 0.04 to 0.02 for 2015+. It is probably best to seperate data into starters and relievers as it is hard to compare the two due to large gap in batters faced. Now with graph. Just change the data location to the proper file, make sure CSV contains K%, BB%, GB%, Soft%, Hard%, Barrel%, and TBF (easy to do on fangraphs)

## batting_desiribility
Similar to pitching desiribility for batters. The outcomes are kinda wacky as the average is a negative. (BB+Barrle's+Hard)-(K+GB+Soft) + (0.04 * pa_deviation).

## pga
Trying to use BeautifulSoup to grab live leaderboard updates for a specific list of players. Does not work

## pitcher_performance_index
A mess of a program doing some weird pitcher calculations for my own stat. Have to manually enter the data right now.
