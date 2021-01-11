import requests
from bs4 import BeautifulSoup
import schedule
import time

headers = {
  "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}


def getTopicContent():
  url = "https://web.okjike.com/topic/553870e8e4b0cafb0a1bef68"
  r = requests.get(url, headers=headers)
  soup = BeautifulSoup(r.text, 'html.parser')
  data = soup.find_all('a')
  news_parent = data[6].find_parent()
  news = news_parent.find_all('span')
  result = ''
  for item in news:
      result += (item.text + '\n')
  return result



def sendBotContent(message):
    web_hook_url = '对应的企业微信Bot的URL'
    msgContent = {
        'msgtype': 'text',
        'text': {
            'content': message
        }
    }
    requests.post(web_hook_url, json=msgContent)


def planExec():
    sendBotContent(getTopicContent())



if __name__ == "__main__":
    schedule.every().day.at("10:00").do(planExec)
    while True:
        schedule.run_pending()
        time.sleep(1)
