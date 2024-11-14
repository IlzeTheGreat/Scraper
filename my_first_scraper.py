import requests
#import BeautifulSoup4

url = "https://github.com/trending"

response = requests.get(url)

if response.status_code == 200: #check if successful
    html_content = response.text #get the content
    print(html_content)  
else:
    print(f"Can't access. Status code: {response.status_code}")