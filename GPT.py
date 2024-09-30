import os
import google.generativeai as genai

class GPTserver:
    def __init__(self):
        self.API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY")
        self.genai.configure(api_key=self.API_KEY)
        self.model_name = "gemini-1.5-flash"

    def DefineModel(self):
        self.model = genai.GenerativeModel(self.model_name)

    def ResponseModel(self, text):
        self.response = self.model.generate_content(f"{text} 한국말로 요약해줘")
        

