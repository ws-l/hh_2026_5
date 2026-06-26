#### 2일차 과제: 4번 노트의 내용을 활용하여서, 금융사 voc에서 지식 그래프를 도출하고 모든 triple의 그래프를 html로 생성해서 사번.zip으로 압축하여 다음 주 월요일 오후 6시까지 LMS에 제출해주세요.


#### DictionaryLoader
!pip install jq  
from langchain_community.document_loaders import (  
    DirectoryLoader,      
    PyPDFLoader,  
     JSONLoader,  
     Docx2txtLoader,  
     UnstructuredExcelLoader,  
     SQLDatabaseLoader,   
     WebBaseLoader,        #일반 웹페이지  
     WikipediaLoader,      #위키피디아  
     YoutubeLoader,        #유튜브 자막  
     SitemapLoader,        #사이트맵 전체 크롤  
     GitLoader,            #Git 레포 전체  
     OutlookMessageLoader, #.msg  
     SlackDirectoryLoader, #Slack 내보내기  
     TelegramChatLoader,   #Telegram JSON  
     ImageCaptionLoader,   #이미지 → 캡션 텍스트  
)  
xls_loader = DirectoryLoader(path="./voc_card", glob="**/*.xlsx", loader_cls= UnstructuredExcelLoader)  
pdf_loader = DirectoryLoader(path="./voc_card", glob="**/*.pdf", loader_cls=PyPDFLoader)  
docx_loader = DirectoryLoader(path="./voc_card", glob="**/*.docx",loader_cls=Docx2txtLoader)  
json_loader = DirectoryLoader(path="./voc_card",glob="**/*.json",loader_cls=JSONLoader,  
    loader_kwargs={"jq_schema": ".", "text_content": False})  
  
#전체 로드 및 합치기  
docs = []  
for loader in [pdf_loader, docx_loader, json_loader]:  
    docs.extend(loader.load())  

print(f"총 {len(docs)}개 문서 로드")
'''
