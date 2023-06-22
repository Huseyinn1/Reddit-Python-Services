from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    id = Column(String, primary_key=True)
    title = Column(String)
    content = Column(String)

def create_table():
    engine = create_engine('sqlite:///reddit_posts.db')
    Base.metadata.create_all(engine)

def insert_post(post_id, title, content):
    engine = create_engine('sqlite:///reddit_posts.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    new_post = Post(id=post_id, title=title, content=content)
    session.add(new_post)
    session.commit()
    
    session.close()
