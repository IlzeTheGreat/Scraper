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

# Testing both functions

url = "https://github.com/trending"
page_content = request_github_trending(url)

if page_content:
    all_rows = extract(page_content)
    print(f"Found {len(all_rows)} repositories:")
    for i, repo in enumerate(all_rows[:1], start=1):
        print(f"\nRepository {i}:\n", repo.prettify())

#Write a function prototyped: def transform(html_repos) taking an array of all the instances of HTML code of the repository row.
#It will return an array of hash following this format: [{'developer': NAME, 'repository_name': REPOS_NAME, 'nbr_stars': NBR_STARS}, ...]

def transform(html_repos):
    result = []
    soup = BeautifulSoup(str(repo), 'html.parser')

    h2_element = soup.find('h2', class_='h3 lh-condensed')
    a_element = h2_element.find('a')
    href = a_element['href']
    developer = href.split('/')[1] #because developer name is the index 1 in that line
    repository_name = href.split('/')[2]

    stars = soup.find('a', href =lambda x: x and x.endswith('/stargazers'))
    nbr_stars = int(stars.text.strip().replace(',', '')) if stars else 0

    result.append({
        'developer': developer,
        'repository_name': repository_name,
        'nbr_stars': nbr_stars
    })

    return result

#Testing
html_content = request_github_trending("https://github.com/trending")
if html_content:
    repo_rows = extract(html_content)
    structured_data = transform(repo_rows)
    for repo in structured_data:
        print(repo)


#Part 3: Format
#Write a function prototyped: def format(repositories_data) taking a repository array of hash and transforming it and returning it into a CSV string. Each column will be separated by , and each line by \n
#The columns will be Developer,Repository Name,Number of Stars