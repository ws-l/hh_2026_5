import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage
from langchain_ollama import ChatOllama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.vectorstores import Chroma as LC_Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
import json

#--------------------------------------------------------------------------#

import json
import glob

# 모든 json 파일 읽기
json_files = glob.glob('./voc_card/*.json')

data_list = []
for file in json_files:
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        data_list.append(data[0])

print(f"총 {len(data_list)}개 파일 로드")
print(data_list[0])  # 첫 번째 확인

reports = data_list[:50]

#--------------------------------------------------------------------------#
lc_embeddings = HuggingFaceEmbeddings(model_name="jhgan/ko-sroberta-multitask")
lc_documents = [
    Document(page_content=r["consulting_content"], metadata={"report_id": r["source_id"]})
    for r in reports
]
lc_vectorstore = LC_Chroma.from_documents(
    documents=lc_documents,
    embedding=lc_embeddings,
    collection_name="lc_voc_card_ollama",
)
retriever = lc_vectorstore.as_retriever(search_kwargs={"k": 3})
print("벡터스토어 재구성 완료")
#--------------------------------------------------------------------------#

duckduckgo = DuckDuckGoSearchRun()
@tool
def search_reports(query: str) -> str:
    """카드사 민원에 대한 내용입니다."""
    docs = retriever.invoke(query)
    if not docs:
        return "관련 보고서 없음"
    results = []
    for doc in docs:
        results.append(f"[{doc.metadata['report_id']}] {doc.page_content[:300]}")
    return "\n\n".join(results)

@tool
def search_internet(query: str) -> str:
    """인터넷에서 최신 정보를 검색합니다. 최신 카드사 관련 뉴스에 사용하세요."""
    return duckduckgo.invoke(query)

tools = [search_reports, search_internet]

#--------------------------------------------------------------------------#
# Agent :  keep_alive: -1
# 모델 초기화 (세션당 1회)
if "llm" not in st.session_state:
    st.session_state.llm = ChatOllama(model="qwen2.5:3b", temperature=0.2, timeout=120)


agent = create_react_agent(
    model=st.session_state.llm,
    tools=tools,
    prompt=(
        "당신은 신용카드 전문가입니다.\n"
        "- 민원 관련 질문 → search_reports 사용\n"
        "- 최신 뉴스는 → search_internet 사용\n"
        "- 필요시 두 Tool을 모두 사용해 종합 답변하세요."
    ),
)
#--------------------------------------------------------------------------#

st.title("엔진 진단 챗봇")
#--------------------------------------------------------------------------#

# 대화 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []
#--------------------------------------------------------------------------#

# 이전 대화 출력
for msg in st.session_state.messages:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.write(msg.content)
#--------------------------------------------------------------------------#

if prompt := st.chat_input("질문을 입력하세요"):        #월루스 연산자, 할당 표현식
    # 사용자 메시지 추가 및 출력
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.write(prompt)

    # LLM 호출 (전체 대화 기록 전달 → 멀티턴)
    with st.chat_message("assistant"):
        with st.spinner("생각 중..."):
            result = agent.invoke({"messages": [{"role": "user", "content": prompt}]})
            response = result["messages"][-1].content ###
            st.write(response)

    # 응답 저장
    st.session_state.messages.append(AIMessage(content=response))