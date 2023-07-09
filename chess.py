import requests
import json

def get_player_games(username):
    response = requests.get(f'https://api.chess.com/pub/player/{username}/games/archives')
    data = response.json()
    
    # Get the URL of the most recent month of games
    recent_games_url = data['archives'][-1]
    response = requests.get(recent_games_url)
    games = response.json()
    
    return games

username = input("Enter the Chess.com username: ")
games = get_player_games(username)

# Print the results
for game in games['games']:
    print(f"URL: {game['url']}")
    print(f"White: {game['white']['username']}, Rating: {game['white']['rating']}")
    print(f"Black: {game['black']['username']}, Rating: {game['black']['rating']}")
    result = game['pgn'].split('Result')[1].split()[0].replace('"', '')
    print(f"Result: {result}")
    print("\n")
