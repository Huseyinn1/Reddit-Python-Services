from flask import Flask
from reddit_crawler import crawl_posts
from database import create_table

app = Flask(__name__)


if __name__ == '__main__':
    
    create_table()

    crawl_posts(False)


    app.run()

