#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import sys

baseUrl = "https://github.com/search"

def query(keyword, page):
    r = requests.get(baseUrl + "?q=" + keyword + "&p=" + str(page) + "&type=Issues")
    soup = BeautifulSoup(r.text, 'html.parser')

    itemList = soup.find_all('div', class_="issue-list-item")

    for item in itemList:
        repoName = item.find_all('div')[0].find_all('div')[0].find_all('a')[0].text
        issue = item.find_all('div')[0].find_all('div')[1].find_all('a')[0]
        issueTitle = issue.text
        issueUrl = "https://github.com" + issue.attrs['href']
        issueContentList = item.find_all('div')[0].find_all('p')
        issueContent = ''
        if len(issueContentList) > 0:
            issueContent = issueContentList[0].text


        print("------------------")
        print("仓库名: " + repoName)
        print("Issue标题: " + issueTitle)
        print("Issue内容: " + issueContent)
        print("Issue地址: " + issueUrl)
        print("------------------")


if __name__ == "__main__":
    query(sys.argv[1], sys.argv[2])
