from models.author import Author
from openai import OpenAI


def generate_author(generated_user_content:dict, 
                    generated_system_content:dict, 
                    client:OpenAI) -> Author:
        
        messages = [
             generated_system_content,
             generated_user_content,
        ]

        print(messages)

        response = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=messages,
            response_format=Author
        )

        new_author:Author = response.choices[0].message.parsed
        return new_author
    
    

    

