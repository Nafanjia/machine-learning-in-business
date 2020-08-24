import requests

data = {
    "ID": 1,
    "LicAge": 68,
    "RecordBeg": "2006-10-01",
    "RecordEnd": "",
    "VehAge": "",
    "Gender": "Female",
    "MariStat": "Alone",
    "SocioCateg": "CSP50",
    "VehUsage": "Private",
    "DrivAge": 44,
    "HasKmLimit": 0,
    "BonusMalus": 56,
    "OutUseNb": 0,
    "RiskArea": 10
}


def send_json(data):
    url = 'http://127.0.0.1:5000/predict'
    headers = {'content-type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    return response


if __name__ == '__main__':
    response = send_json(data)
    print(response.json())
