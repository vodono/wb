from base import Session
from sqlalchemy import func

from category import Category
from comment import Comment
from event import Event
from language import Language
from location import Location
from message import Message
from user import User

session = Session()

print('List of users with filters selected:')

filtered_users_list = session.query(
    User,
).outerjoin(
    Language,
    User.language,
).outerjoin(
    Comment,
    User.recipient_comments,
).filter(
    User.city == 'Kyiv',
    Language.title == 'language_2',
).order_by(
    User.first_name
).all()

for user in filtered_users_list[:]:
    print(user)


# import ipdb
# ipdb.set_trace()

session.close()
