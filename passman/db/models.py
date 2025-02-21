from typing import List, Optional
from pydantic import BaseModel, Field


# @TODO : Rename to Account
class Password(BaseModel):
    id: str = Field(description="Password Identification")
    username: str = Field(default="", description="Username")
    encrypted_password: str = Field(description="Encrypted Password")
    url: Optional[str] = Field(default=None, description="URL or Service name")
    description: Optional[str] = Field(default=None, description="Description")
    created_at: int = Field(description="Creation date")


# @TODO : Rename to Profile
class Account(BaseModel):
    name: str
    master_password: str = Field(description="Hashed Master Password")
    passwords: List[Password]

    def get_password(self, id: str | int):
        if isinstance(id, int):
            return self.passwords[id]

        for password in self.passwords:
            if password.id == id:
                return password
        return None

    def remove_password(self, id: str):
        for index, password in enumerate(self.passwords):
            if password.id == id:
                del self.passwords[index]
                break
