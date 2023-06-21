import unittest
import sqlite3
import time
from api import app
from database import create_table, insert_post
from reddit_crawler import crawl_posts

class TestRedditCrawler(unittest.TestCase):

    def setUp(self):
        
        self.conn = sqlite3.connect('reddit_posts.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS posts (id TEXT, title TEXT, content TEXT)''')

    def tearDown(self):
        self.conn.close()
        
    def test_create_table(self):
        
        print("Create_table testi başladı")
        create_table()

        self.c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='posts'")
        result = self.c.fetchone()
        self.assertIsNotNone(result) 
        
        print("Create_table testi tamamlandı")

    def test_insert_post(self):
        # Post eklemek için insert_post() fonksiyonunu çağırma
        print("insert_post testi başladı")
        insert_post('test123', 'Test Deneme', 'Test Deneme2')

        # Veritabanından postu sorgulama
        self.c.execute("SELECT * FROM posts WHERE id = 'test123'")
        result = self.c.fetchone()
        
        # Test sonuçlarını kontrol etme
        self.assertEqual(result[1], 'Test Deneme')  # title alanını kontrol etme
        self.assertEqual(result[2], 'Test Deneme2')  # content alanını kontrol etme
        print("insert_post testi tamamlandı")

    def test_get_posts(self):
       
        print("get_posts testi başladı")
        with self.conn:
            
            self.c.execute("INSERT INTO posts VALUES (?, ?, ?)", ('test2', 'Test Deneme2', 'Test Deneme3'))
      

        # API üzerinden postları getirme
        with app.test_client() as client:
            response = client.get('/api/posts')
            data = response.get_json()

            self.assertEqual(response.status_code, 200)  
            # self.assertEqual(len(data),1)  # Dönen post sayısı kontrol edilmeli
            # self.assertEqual(data[-1]['id'], 'test123')  # İlk postun ID'si kontrol edilmeli
            print("get_posts testi tamamlandı")

    def test_crawl_posts(self):
        # crawl_posts() fonksiyonunu çağırma
        print("crawl_posts testi başladı")
        crawl_posts(True)
        time.sleep(5)
        
        self.conn.commit()  
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM posts WHERE id = 'test23'")
        
        result = self.c.fetchone()
        # Test sonuçlarını kontrol etme
        self.assertIsNotNone(result) 
        print("crawl_posts testi tamamlandı")

if __name__ == '__main__':
    unittest.main()
