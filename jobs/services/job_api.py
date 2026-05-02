import requests


def job_api():
    url = "https://remoteok.com/api"
    res = requests.get(url)
    return  res.json()