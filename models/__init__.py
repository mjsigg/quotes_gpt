from datetime import date
from pydantic import BaseModel
from typing import Optional, List, Dict

class Author(BaseModel):
    '''
    All fields are optional. We will create an Unknown class for those who can't be cited.
    '''
    quotes_bank: Optional[Dict[str, str]] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    alias: Optional[List[str]] = None
    dob: Optional[date] = None
    birthplace: Optional[str] = None

    @classmethod
    def initialize(cls, 
                   first_name: str, 
                   last_name: str, 
                   middle_name: Optional[str] = None, 
                   dob: Optional[date] = None, 
                   birthplace: Optional[str] = None) -> 'Author':
        # Initialize fields with default values if not provided
        quotes_bank = {}
        alias = []

        return cls(
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            dob=dob,
            birthplace=birthplace,
            quotes_bank=quotes_bank,
            alias=alias
        )
