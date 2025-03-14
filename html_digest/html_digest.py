import requests
from bs4 import BeautifulSoup
import re

def input_processing():
    url_file = input("Path to URL's file: ")
    with open(url_file, "r", encoding="utf-8") as file:
        subdirs = file.read().splitlines()
    return subdirs

def parser(subdirs):
    responses = []
    for subdir in subdirs:
        response = requests.get(subdir)
        soup = BeautifulSoup(response.text,"html.parser")
        data = soup.prettify()
        responses.append(f"Subdir: {subdir}\nStatus Code: {response.status_code}\nData:{data}\n")
    return responses

def grep(pattern, data):
    results = []
    matches = re.findall(pattern, data, re.DOTALL)
    for match in matches:
        results.append(match.strip())
    return results

def grep_comments(responses):
    banner = """
----------------------------------------------------------------------------------------------------
HTML COMMENTS
----------------------------------------------------------------------------------------------------
    """
    print(banner)
    for response in responses:
        print("----------------------------------")
        lines = response.splitlines()
        print(lines[0])
        print(lines[1])
        print("Comments:\n")
        comments = grep(r'<!--([\s\S]*?)-->', response)
        for comment in comments:
            print(f'{comment}\n')
        print("-----------------------------------")
def main():
    subdirs = input_processing()
    data = parser(subdirs)
    grep_comments(data)

if __name__ == "__main__":
    main()
