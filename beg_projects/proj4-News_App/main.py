import requests

querey=input("Enter your intrest:")
api="aea620acb8f64fa188369bab8b062a22"

url=f"https://newsapi.org/v2/everything?q={querey}&from=2025-11-23&sortBy=publishedAt&apiKey=aea620acb8f64fa188369bab8b062a22"

print(url)

r=requests.get(url)
data=r.json()

articles = data["articles"]

for index,article in enumerate(articles):
    print(f"{index+1}.{article["title"]}")
    print(f"url:{article["url"]}")
    print("\n***************************************\n")