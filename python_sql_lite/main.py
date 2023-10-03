import openai
from IPython.display import Markdown as md

from query import select_from_table
from schema import get_schema
from db import create_connection
from keys import *

DATABASE = "./pythonsqlite.db"
openai.api_key = apikey

def main(conn):
    
    # Use Python's input function to get a question from the user
    question = input("Enter your natural language query: ")
    
    print(f"Question: {question}")

    prompt = f"""
    
    Given the following SQL Schema:{get_schema()}
    Write a SQLite query to answer this question: {question}
    
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"{prompt}"},
            # {"role": "user", "content": ""}
        ]
    )

    string = md(response['choices'][0]['message']['content']) 

    print((response['choices'][0]['message']['content']))


if __name__ == "__main__":
    conn = create_connection(DATABASE)
    main(conn)
