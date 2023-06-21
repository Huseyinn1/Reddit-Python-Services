from flask import Flask, jsonify
import sqlite3


app = Flask(__name__)

@app.route('/api/posts')
def get_posts():
    
    conn = sqlite3.connect('reddit_posts.db')
    c = conn.cursor()
    
    c.execute('SELECT * FROM posts')
    rows = c.fetchall()
    
    posts = []
    for row in rows:
        post = {
            'id': row[0],
            'title': row[1],
            'content': row[2]
        }
        posts.append(post)
    
    conn.close()
    
    return jsonify(posts)

if __name__ == '__main__':
    app.run()
