import re
import pdfplumber

class PDFembedding:
    def __init__(self, pdf_path:str):
       self.pdf_path = r"{}".format(pdf_path) 

    def DefineIndex(self):
        # pyqt UI에서 input 받게 수정
        self.index = None
        pass

    def embedding(self):
        # 딕셔너리 초기화
        self.contents_dict = {section: "" for section in self.index}
        current_key = None

        # PDF 파일 열기
        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    lines = text.split('\n')
                    for line in lines:
                        line = line.strip()

                        # 현재 키가 정의된 목차 중 하나인지 확인
                        if line in self.contents_dict:
                            current_key = line  # 현재 목차 키 설정
                        elif current_key:
                            # 현재 키에 해당하는 내용 추가
                            self.contents_dict[current_key] += line + " "

    