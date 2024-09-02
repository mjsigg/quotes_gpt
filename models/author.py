from datetime import date
from pydantic import AfterValidator, BaseModel, field_validator
from typing import Optional, List, Dict

class Author(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    alias: Optional[List[str]] = None
    quotes:list[str]
    
    def validate_author(self):
        if not self.first_name and not self.middle_name and not self.alias:
            raise ValueError("All identifiers of class are empty.")
        
    def get_author_full_name(self):
        return (f'{self.first_name} {self.last_name}')

    def print_quotes(self):
        for quote in self.quotes:
            print(quote)