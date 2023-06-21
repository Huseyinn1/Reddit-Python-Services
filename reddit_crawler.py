import praw
import sqlite3
import time

def crawl_posts(stop_event):
    #login işlemi
    client_id = 'client_id'
    client_secret = 'client_secret'
    username = 'username'
    password = 'password'
    
    # Takip edilecek subreddit adı
    subreddit_name = 'cybersecurity'
    
    conn = sqlite3.connect('reddit_posts.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS posts
                 (id TEXT PRIMARY KEY, title TEXT, content TEXT)''')
    conn.commit()
    
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
            new_posts = subreddit.new(limit=10)  # Son 10 postu alabiliriz isteğe bağlı olarak değiştirilebilir.
    
            # Her post için işlemleri yap
            for post in new_posts:
                
                c.execute('SELECT * FROM posts WHERE id = ?', (post.id,))
                existing_post = c.fetchone()
    
                if not existing_post:
                    
                    c.execute('INSERT INTO posts VALUES (?, ?, ?)', (post.id, post.title, post.selftext))
                    print(f'Yeni post eklendi: {post.title}')
    
            
            conn.commit()
    
            # Belirli bir süre sonra tekrar kontrol etme
            time.sleep(5)
        except Exception as e:
            print(f'Hata oluştu: {e}')
    
    
    conn.close()

