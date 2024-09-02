from pydantic import BaseModel

class SystemContextManager(BaseModel):
    system_profiles:dict[str,str] = {}
    system_instructions: dict[str,str] = {
        'generate_author': "DO NOT HALLUCINATE. You will be provided noteable individual's name, past or present.  Find the individual names and fill out the provided Author class by field.  Please add 3 unique quotes field to the individual.  If a field cannot be filled return None in that field."
    }
    
    def generate_instructions(self,
                              selected_instruction_key_name:str | None = None) -> str:
        if selected_instruction_key_name and len(selected_instruction_key_name) > 0:
            return self.system_instructions.get(selected_instruction_key_name)
        return self.system_instructions.get("generate_author")
    
def generate_role_system_content(system_instructions:str)-> dict[str,str]:
    if not system_instructions or system_instructions.strip() == "":
        raise ValueError("System instructions empty.")
    
    return {
        'role': 'system',
        'content': system_instructions
    }

def generate_role_user_content(user_query:str) -> dict[str,str]:
    if not user_query or user_query.strip() == "":
        raise ValueError("Provided query is empty.")

    return {
        'role':'user',
        'content': user_query
    }
