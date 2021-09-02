import requests
print(requests.__version__)

requests.get("http://www.google.com/")
print(requests.get("https://raw.githubusercontent.com/seliayeu/cmput404-lab1/main/lab1.py").text)
