import requests

headers = {
    'Authorization': 'PTzITvHNyQMPV1eucEOjDwD1Wf2DGtgmWkuGKTEP5V42HloJJdBBXMRqABfv'
}

response = requests.get("https://api.sportmonks.com/v3/football/fixtures/18535517?api_token=", headers=headers)
print(response.json())
