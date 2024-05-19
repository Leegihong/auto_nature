import requests
from bs4 import BeautifulSoup

def fetch_abstract(link):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(link, headers=headers)
    if response.status_code != 200:
        print(f"{link}에서 초록을 불러오는 데 실패했습니다.")
        return ""
    soup = BeautifulSoup(response.content, 'html.parser')
    # Nature 사이트 구조에 따라 조정 필요
    abstract_section = soup.find('div', class_='c-article-section__content')
    if abstract_section:
        return abstract_section.get_text(strip=True)
    else:
        return "초록이 없습니다."

def fetch_papers():
    url = "https://www.nature.com/nature/articles"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("웹 페이지를 불러오는 데 실패했습니다.")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')
    papers = []

    for article in articles:
        title = article.find('h3', class_='c-card__title').get_text(strip=True)
        link = article.find('a')['href']
        if not link.startswith('http'):
            link = f"https://www.nature.com{link}"
        
        # 각 논문의 상세 페이지로부터 초록 추출
        abstract = fetch_abstract(link)
        
        papers.append({"title": title, "link": link, "abstract": abstract})

    return papers

