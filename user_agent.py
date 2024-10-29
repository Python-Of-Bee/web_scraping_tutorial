import requests
from fake_useragent import UserAgent

# Background on user-agents
ua = UserAgent()

header = {'user-agent' : ua.chrome}

page = requests.get('https://www.google.com/', headers=header, timeout=3)

print(page.content)




