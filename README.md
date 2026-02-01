This is an end-to-end LLM-based application built using OpenAI and LangChain that enables natural language interaction with a MySQL database. The system allows users to ask questions in plain English, which are automatically translated into SQL queries, executed on the database, and returned as human-readable answers. To optimize LLM response accuracy I implemented few-shot prompting, enabling reliable natural-language-to-SQL generation.

<img width="1866" height="765" alt="Tshirts bot" src="https://github.com/user-attachments/assets/26187514-22b1-4aa2-bd8c-83c20e98ab31" />

Key Highlights
●	Inventory, sales and discounts data is stored in a MySQL database
●	OpenAI
●	OpenAI face embeddings
●	Streamlit for UI
●	Langchain framework
●	Chromadb as a vector store
●	Few shot learning
●	Semantic Search
In the UI, store manager will ask questions in a natural language and it will produce the answers
