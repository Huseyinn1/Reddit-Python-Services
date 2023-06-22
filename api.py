from flask import Flask, jsonify
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    id = Column(String, primary_key=True)
    title = Column(String)
    content = Column(String)

def get_posts():
    engine = create_engine('sqlite:///reddit_posts.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    posts = session.query(Post).all()

    post_list = []
    for post in posts:
        post_dict = {
            'id': post.id,
            'title': post.title,
            'content': post.content
        }
        post_list.append(post_dict)

    session.close()

    return jsonify(post_list)

@app.route('/api/posts')
def api_get_posts():
    return get_posts()

if __name__ == '__main__':
   app.run()

