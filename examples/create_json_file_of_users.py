from pydantic import BaseModel
from jsoner import Jsoner


class User(BaseModel):
    username: str
    password: str
    confirm: bool


"""
    the so-called imaginary data that you get, for example, when parsing a website
"""
users = [User(username="feg2005", password="hash", confirm=True),
         User(username="mynamedima", password="hash", confirm=True),
         User(username="dunder", password="hash", confirm=False),
         User(username="supercreator", password="hash", confirm=True),
         User(username="superman", password="hash", confirm=True),
         User(username="person22", password="hash", confirm=False),
         User(username="coolcat", password="hash", confirm=True),
         User(username="lifer", password="hash", confirm=True),
         User(username="musicalyman", password="hash", confirm=False)
]


jsn = Jsoner(models=[User], filename="users.json")


for usr in users:
    jsn.append(usr)

jsn.save(indent=4)