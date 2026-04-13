
import requests
proxies = { 'http': 'http://127.0.0.1:7897', 'https': 'http://127.0.0.1:7897' }
import requests

cookies = {
    'gg_info': '1738449518',
    'b2_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lnhjb3MudG9wIiwiaWF0IjoxNzQxODY2ODUzLCJuYmYiOjE3NDE4NjY4NTMsImV4cCI6MTc0MzA3NjQ1MywiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiMjg1NCJ9fX0.V7W6FhR2EfCF2GL-oMHBshvWM9aZBt0SB8aRRmd2jj8',
    'wordpress_logged_in_ad9ab476341152a2899f8867c2d54a2e': 'darkbfly%7C1742428453%7C1gWK1BGGCQzIv5UQjifThYFsqnYz0rynR7Ws8kLaX1s%7C01c76c97abc40f3f4c3ed2d2bb88d4b98e2702dc5e2113542a162b11e5736864',
    '__51cke__': '',
    '__tins__21928497': '%7B%22sid%22%3A%201742081552698%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201742083712683%7D',
    '__51laig__': '2',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lnhjb3MudG9wIiwiaWF0IjoxNzQxODY2ODUzLCJuYmYiOjE3NDE4NjY4NTMsImV4cCI6MTc0MzA3NjQ1MywiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiMjg1NCJ9fX0.V7W6FhR2EfCF2GL-oMHBshvWM9aZBt0SB8aRRmd2jj8',
    # 'content-length': '0',
    'origin': 'https://www.xcos.top',
    'priority': 'u=1, i',
    'referer': 'https://www.xcos.top/mission/today',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
    # 'cookie': 'gg_info=1738449518; b2_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lnhjb3MudG9wIiwiaWF0IjoxNzQxODY2ODUzLCJuYmYiOjE3NDE4NjY4NTMsImV4cCI6MTc0MzA3NjQ1MywiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiMjg1NCJ9fX0.V7W6FhR2EfCF2GL-oMHBshvWM9aZBt0SB8aRRmd2jj8; wordpress_logged_in_ad9ab476341152a2899f8867c2d54a2e=darkbfly%7C1742428453%7C1gWK1BGGCQzIv5UQjifThYFsqnYz0rynR7Ws8kLaX1s%7C01c76c97abc40f3f4c3ed2d2bb88d4b98e2702dc5e2113542a162b11e5736864; __51cke__=; __tins__21928497=%7B%22sid%22%3A%201742081552698%2C%20%22vd%22%3A%202%2C%20%22expires%22%3A%201742083712683%7D; __51laig__=2',
}

response = requests.post('https://www.xcos.top/wp-json/b2/v1/userMission', cookies=cookies, headers=headers, proxies=proxies)

print(response.json())