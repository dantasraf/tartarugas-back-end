import requests

def makePost():
    url = 'http://localhost:5000/upload'
    files = {'media': open('images/test.jpg', 'rb')}
    response = requests.post(url, files=files)
    print(response)

def makeTest():
    url = 'http://localhost:5000/'
    response = requests.post(url)
    print(response.content)

makePost()