from crawling import  fetch_papers
from database import save_papers_to_db

if __name__ == '__main__':
    # Nature에서 논문 정보를 가져오기
    papers = fetch_papers()

    # 가져온 논문 정보를 MariaDB에 저장하기
    save_papers_to_db(papers)