import openai
from models import Author
from openai import OpenAI
from dotenv import load_dotenv
import os
def main():
    load_dotenv()
    
    client = OpenAI(
        api_key=os.getenv('OPEN_API_KEY')
    )

    print("Starting app.")
    Mark_Twain = Author(first_name="Samuel", middle_name="Langhorne", last_name="Clemens", birthplace="Redding, Connecticut", dob="November 30, 1835", alias=["Mark Twain"], age=74)

    test = f'''
    INSTRUCTIONS: Please return 3 famous quotes from {Mark_Twain.alias[0]}.  Try to return one from 3 points of his life: early, middle, later.

    '''

    message = [
        {"role": "system", "content": f"{test}"}
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=message
    )

    print(response.choices[0].message.content)



    
if __name__ == "__main__":
    main()