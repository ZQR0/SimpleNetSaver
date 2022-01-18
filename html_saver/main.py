import requests

def saver(url):
    response = requests.get(url=url).text

    with open('result.hmml', mode='w', encoding='utf-8') as file:
        file.write(response)
        file.close()

url = "Your url adress"

if __name__ == '__main__':
    saver(url=url)