import urllib3
from bs4 import BeautifulSoup
import requests

url = "https://www.espn.com/golf/leaderboard"

# Disable SSL verification and suppress warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Define the teams and their players
teams = {
    "Brady": ["Scottie Scheffler", "Xander Schauffele", "Collin Morikawa", "Tyrrell Hatton", "Preston Summerhays (a)"], 
    "Cy": ["Jon Rahm", "Rory McIlroy", "Justin Rose", "Rickie Fowler", "Gordon Sargent (a)"], 
    "Mike": ["Cameron Smith", "Victor Hovland", "Max Homa", "Brooks Keopka", "Wenyi Ding (a)"]}

# Make the request to ESPN website without SSL verification
response = requests.get(url, verify=False)

if response.status_code == 200:
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    # Find the HTML elements that contain the player names and scores
    player_names = soup.select("#fittPageContainer > div:nth-child(3) > div > div > section:nth-child(2) > div > div > div > div.Button--group > div.competitors > div > div > div > div.Table__Scroller > table > tbody > tr:nth-child(3) > td.tl.plyr.Table__TD > a")
    scores = soup.select("#fittPageContainer > div:nth-child(3) > div > div > section:nth-child(2) > div > div > div > div.Button--group > div.competitors > div > div > div > div.Table__Scroller > table > tbody > tr:nth-child(11) > td:nth-child(4)")

    # Create a dictionary to store live scores for tracked players
    live_scores = {}

    for name, score in zip(player_names, scores):
        player_name = name.text.strip()
        player_score = int(score.text.strip())

        for team, players in teams.items():
            if player_name in players:
                if team not in live_scores:
                    live_scores[team] = []
                live_scores[team].append(player_score)

    # Calculate the team scores by dropping the worst score for each team
    team_scores = [sum(sorted(scores)[:-1]) for scores in live_scores.values()]

    # Print the team scores
    for team, score in zip(teams.keys(), team_scores):
        print(f"{team} Score: {score}")

else:
    print("Failed to retrieve HTML content from ESPN.")
