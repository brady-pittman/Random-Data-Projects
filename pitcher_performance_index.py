import numpy as np

def calculate_ppi(era_minus, fip_minus, siera, k_percent, bb_percent, league_era_minus, league_fip_minus, league_siera, league_k_percent, league_bb_percent):
    weights = {
        'era_minus': 0.3,
        'fip_minus': 0.3,
        'siera': 0.3,
        'k_percent': 0.05,
        'bb_percent': 0.05
    }

    ppi = []
    for era, fip, si, k, bb in zip(era_minus, fip_minus, siera, k_percent, bb_percent):
        era_score = (era / league_era_minus) * 100
        fip_score = (fip / league_fip_minus) * 100
        si_score = (si / league_siera) * 100
        k_score = (k / league_k_percent) * 100
        bb_score = (league_bb_percent / bb) * 100

        ppi_value = era_score * weights['era_minus'] + fip_score * weights['fip_minus'] + si_score * weights['siera'] + k_score * weights['k_percent'] + bb_score * weights['bb_percent']
        ppi.append(ppi_value)

    return ppi

def rank_pitchers(names, ppi):
    rankings = sorted(zip(names, ppi), key=lambda x: x[1])
    return rankings

# Input the league's ERA-, FIP-, K%, BB%, and SIERA values
league_era_minus = 100
league_fip_minus = 100
league_siera = 4.06
league_k_percent = 22.3
league_bb_percent = 8.5

names = ["Jacob deGrom", "Luis Perdomo", "Miguel Castro", "Hector Neris"]
era_minus = [45, 181, 93, 127]  # Lower values indicate better performance
fip_minus = [49, 106, 116, 97]  # Lower values indicate better performance
siera = [2.78, 4.82, 5.27, 2.28]
k_percent = [32.2, 18.0, 15.2, 37.7]
bb_percent = [5.5, 10.1, 13.3, 7.9]

# Calculate individual pitchers' PPI using league stats for comparison
ppi = calculate_ppi(era_minus, fip_minus, siera, k_percent, bb_percent, league_era_minus, league_fip_minus, league_siera, league_k_percent, league_bb_percent)

# Rank the pitchers based on PPI
rankings = rank_pitchers(names, ppi)

# Print the rankings
print("2018 Pitcher Performance Index")
for(name, ppi) in rankings:
    print(f"{name} - PPI: {ppi:.2f}")
