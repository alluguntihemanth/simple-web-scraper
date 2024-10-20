

import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://techcrunch.com/2024/04/30/sams-clubs-ai-powered-exit-tech-reaches-20-of-stores/"

def scrape_article(url):

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')


        title = soup.find('h1').get_text(strip=True)
        date = soup.find('time')['datetime'] if soup.find('time') else "Date not available"
        author = soup.find('a', class_='article__byline').get_text(strip=True) if soup.find('a', class_='article__byline') else "Author not found"


        content = [p.get_text(strip=True) for p in soup.find_all('p')]
        full_content = "\n".join(content)


        article_data = {
            'Title': title,
            'Publication Date': date,
            'Author': author,
            'Content': full_content
        }

        return article_data

    else:
        print(f"Failed to retrieve the article. Status code: {response.status_code}")
        return None

article_data = scrape_article(url)


if article_data:
    print("Title:", article_data['Title'])
    print("Publication Date:", article_data['Publication Date'])
    print("Author:", article_data['Author'])
    print("\nContent:\n", article_data['Content'])


    df = pd.DataFrame([article_data])
    df.to_csv('scraped_article.csv', index=False)
    print("\nArticle data saved to 'scraped_article.csv'")
