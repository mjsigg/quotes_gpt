from pydantic import BaseModel
from models.author import Author

class PseudoDB(BaseModel):
    authors:dict[str, Author] = {}

    def add_author(self, author:Author):
        author.validate_author()
        fullname:str = author.get_author_full_name()
        if fullname not in self.authors:
            self.authors[fullname] = author
        print(fullname + " has been added!")