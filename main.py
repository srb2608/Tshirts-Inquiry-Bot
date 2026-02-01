import os
import streamlit as st
import pickle
import time
import langchain
from script import Key
from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import FewShotPromptTemplate
from langchain_experimental.sql import SQLDatabaseChain
from few_shots import few_shots
from few_shots import mysql_prompt
from few_shots import PROMPT_SUFFIX
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector

os.environ['OPENAI_API_KEY']= Key
def get_few_shot_db_chain():
    llm = ChatOpenAI(temperature=0.9, max_tokens=500)
    db_user="root"
    db_password= "root"
    db_host="localhost"
    db_name= "atliq_tshirts_new"
    db = SQLDatabase.from_uri(
    f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=3
        )
    embeddings = OpenAIEmbeddings()
#print (db)
    a = []
    for i in range(5):
        to_vectorize = " ".join(map(str, few_shots[i].values()))
        a.append(to_vectorize)
    clean_metadata = [
        {k: str(v) for k, v in shot.items()}
        for shot in few_shots
    ]
    vectorstore = Chroma.from_texts(
        a,
        embedding=embeddings,
        metadatas=clean_metadata
    )
    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vectorstore,
        k=2,
    )
    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer", ],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )
    few_shot = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"]
    )
    new_chain = SQLDatabaseChain(
        llm=llm,  # your LLM
        database=db,  # your SQLDatabase object
        verbose=True,
        prompt=few_shot
    )
    return new_chain