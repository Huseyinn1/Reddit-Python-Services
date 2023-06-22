import praw
import time
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    id = Column(String, primary_key=True)
    title = Column(String)
    content = Column(String)

def crawl_posts(stop_event):
    # Login bilgileri
    client_id = 'client_id'
    client_secret = 'client_secret'
    username = 'username'
    password = 'password'
    
    # Takip edilecek subreddit adı
    subreddit_name = 'cybersecurity'
    
    # Veritabanı bağlantısı ve oturum oluşturma
    engine = create_engine('sqlite:///reddit_posts.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Reddit'e bağlanma
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         username=username,
                         password=password,
                         user_agent='my_user_agent')
    
    # Sürekli olarak yeni postları kontrol etme
    while not stop_event :
        try:
            subreddit = reddit.subreddit(subreddit_name)
            new_posts = subreddit.new(limit=10)  # Son 10 postu alabiliriz, isteğe bağlı olarak değiştirilebilir.
    
            # Her post için işlemleri yap
            for post in new_posts:
                existing_post = session.query(Post).filter_by(id=post.id).first()
    
                if not existing_post:
                    new_post = Post(id=post.id, title=post.title, content=post.selftext)
                    session.add(new_post)
                    session.commit()
                    print(f'Yeni post eklendi: {post.title}')
    
            # Belirli bir süre sonra tekrar kontrol etme
            time.sleep(5)
        except Exception as e:
            print(f'Hata oluştu: {e}')
            session.rollback()
    
    session.close()