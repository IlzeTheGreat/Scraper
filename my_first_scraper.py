import requests

def request_github_trending(url):

    response = requests.get(url)

    if response.status_code == 200:  #Check if success
        html_content = response.text  #Get the content
        return html_content
    else:
        print(f"Can't access. Error code: {response.status_code}")
        return None

#Testing
html_content = request_github_trending("https://github.com/trending")
if html_content:
    print("Got content successfully!")
    print(html_content[:500])  #Print first 500 characters
