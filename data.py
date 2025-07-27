import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

try:
    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    data = response.json()
    question_data = data["results"]
except requests.exceptions.RequestException as e:
    print("Error fetching quiz data:", e)
    question_data = []
