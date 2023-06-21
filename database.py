import sqlite3

def create_table():

    conn = sqlite3.connect('reddit_posts.db')
    c = conn.cursor()
    

    c.execute('''CREATE TABLE IF NOT EXISTS posts
                 (id TEXT PRIMARY KEY, title TEXT, content TEXT)''')
    conn.commit()
    conn.close()

def insert_post(post_id, title, content):

    conn = sqlite3.connect('reddit_posts.db')
    c = conn.cursor()
    
    c.execute('INSERT INTO posts VALUES (?, ?, ?)', (post_id, title, content))
    conn.commit()
    conn.close()
