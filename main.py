from pydoc import cli
from models import author
from models.author import Author
from models.psuedo_db import PseudoDB
from openai import OpenAI
from dotenv import load_dotenv
from managers.context_managers import SystemContextManager, generate_role_system_content, generate_role_user_content
from services.model_calls import generate_author


import os
def main():
    load_dotenv()
    
    client = OpenAI(
        api_key=os.getenv('OPEN_API_KEY')
    )

    file_path:str = './data'
    if not os.path.exists(file_path):
        raise ValueError("Paht doesn't exist")
    
    print("Starting app.")

    db:PseudoDB = PseudoDB()

    system_context_manager = SystemContextManager()
    system_instructions:str = system_context_manager.generate_instructions()
    system_content = generate_role_system_content(system_instructions)

    current_user_input = "Do you know Robert Frost?"
    user_input_content = generate_role_user_content(user_query=current_user_input)

    new_author:Author = generate_author(user_input_content, 
                                        system_content, 
                                        client)
    if new_author:
        db.add_author(new_author)
        
        get_rob:Author = db.authors.get('Robert Frost')
        
        print(f"Hello, it's me, {get_rob.get_author_full_name()}! ")
        get_rob.print_quotes()
        

        

    
    
if __name__ == "__main__":
    main()