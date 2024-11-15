import requests
from bs4 import BeautifulSoup

def request_github_trending(url):

    response = requests.get(url)

    if response.status_code == 200:  #Check if success
        html_content = response.text  #Get the content
        return html_content
    else:
        print(f"Can't access. Error code: {response.status_code}")
        return None

#Testing
"""
html_content = request_github_trending("https://github.com/trending")
if html_content:
    print("Got content successfully!")
    print(html_content[:100])  #Print first 100 characters
"""

#Write a function prototyped: def extract(page) to find_all instances of HTML code of repository rows and return it. You should use BeautifulSoup. :-)

def extract(page):
    soup = BeautifulSoup(page, 'html.parser')
    all_rows = soup.find_all('article', class_='Box-row')
    return all_rows

# Testējam abas funkcijas
url = "https://github.com/trending"
page_content = request_github_trending(url)

#Testing
"""
if page_content:
    all_rows = extract(page_content)
    print(f"Found {len(all_rows)} repositories:")
    for i, repo in enumerate(all_rows[:5], start=1):
        print(f"\nRepository {i}:\n", repo.prettify())
"""

#Write a function prototyped: def transform(html_repos) taking an array of all the instances of HTML code of the repository row.
#It will return an array of hash following this format: [{'developer': NAME, 'repository_name': REPOS_NAME, 'nbr_stars': NBR_STARS}, ...]

