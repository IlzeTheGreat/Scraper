import requests
from bs4 import BeautifulSoup

#Request Write a function prototyped: def request_github_trending(url) it will return the result of Request.

def request_github_trending(url):

    response = requests.get(url)

    if response.status_code == 200:  #Check if success
        html_content = response.text  #Get the content
        return html_content
    else:
        print(f"Can't access. Error code: {response.status_code}")
        return None

#Write a function prototyped: def extract(page) to find_all instances of HTML code of repository rows and return it. You should use BeautifulSoup. :-)

def extract(page):
    soup = BeautifulSoup(page, 'html.parser')
    all_rows = soup.find_all('article', class_='Box-row')

    return all_rows

#Write a function prototyped: def transform(html_repos) taking an array of all the instances of HTML code of the repository row.
#It will return an array of hash following this format: [{'developer': NAME, 'repository_name': REPOS_NAME, 'nbr_stars': NBR_STARS}, ...]

def transform(html_repos):
    result = []

    for repo in html_repos:
        soup = BeautifulSoup(str(repo), 'html.parser')

        h2_element = soup.find('h2', class_='h3 lh-condensed') #digging deeper
        a_element = h2_element.find('a') #more deeper
        href = a_element['href'] #more and more deeper
        developer = href.split('/')[1] #deep enough. [1] because developer name is the index 1 in that line
        repository_name = href.split('/')[2]

        stars = soup.find('a', href =lambda x: x and x.endswith('/stargazers'))
        nbr_stars = int(stars.text.strip().replace(',', '')) if stars else 0

        result.append({
            'developer': developer,
            'repository_name': repository_name,
            'nbr_stars': nbr_stars
        })

    return result


#Part 3: Format
#Write a function prototyped: def format(repositories_data) taking a repository array of hash and transforming it and returning it into a CSV string. Each column will be separated by , and each line by \n
#The columns will be Developer,Repository Name,Number of Stars

def format(repositories_data):
    csv_content = "Developer,Repository Name,Number of Stars\n"

    for repo in repositories_data:
        csv_row = f"{repo['developer']},{repo['repository_name']},{repo['nbr_stars']}\n"
        csv_content += csv_row

    return csv_content

#Testing the whole cycle

def main():
    url = "https://github.com/trending"
    html_content = request_github_trending(url)

    if html_content:
        repo_rows = extract(html_content)
        top_repos = repo_rows[:25]  # Top25
        structured_data = transform(top_repos)
        csv_result = format(structured_data)
        
        # Print the results
        print("Result:")
        print(csv_result)

# Requesting main
if __name__ == "__main__":
    main()