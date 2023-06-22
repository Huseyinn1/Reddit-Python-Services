# Python Reddit Crawler

Bu proje, Reddit içerisindeki subredditlerde paylaşılan postları anlık olarak takip eden bir Python servisidir.

## Proje Tanımı

Python Reddit Crawler, belirli subredditlerdeki postları izlemek için Reddit API'sini kullanır ve bu postları bir veritabanında saklar. Ayrıca, diğer uygulamaların bu verilere erişimini sağlamak için bir API sunar.

## Özellikler

- Kullanıcı Girişi: Kullanıcılar kimlik doğrulaması yapabilir ve takip etmek istedikleri subredditleri belirleyebilir.
- Post Takibi: Belirlenen subredditlerdeki yeni postlar anlık olarak takip edilir ve veritabanında saklanır.
- Veritabanı Depolama: Postlar, gerektiğinde erişilebilmesi için bir SQL veritabanında saklanır.
- API Erişimi: Postlar, bir API üzerinden sunularak diğer uygulamaların verilere erişmesine olanak tanır.
- Docker Desteği: Uygulama, Docker kullanılarak konteynerize edilebilir ve kolayca dağıtılabilir.


## Kurulum
1. Projeyi bilgisayarınıza indirin veya kopyalayın.
    
2. Gerekli bağımlılıkları yüklemek için aşağıdaki komutu kullanın:
    pip install -r requirements.txt

3.`reddit_crawler.py` dosyasında Reddit API kimlik bilgilerinizi ve veritabanı ayarlarınızı yapılandırın.

4. Uygulamayı başlatmak için aşağıdaki komutu kullanın:
    python main.py

## Kullanım

- API istekleri yapmak için `http://localhost:5000/posts` endpointini kullanabilirsiniz. Bu endpoint, tüm postları almanıza olanak sağlar.
- Giriş yaparak ilgi duyduğunuz subredditleri belirleyebilirsiniz.

## Kullanılan Teknolojiler

Aşağıdaki teknolojiler, Python Reddit Crawler projesinde kullanılmıştır:

- Python: Proje, Python programlama dili kullanılarak geliştirilmiştir.
- Flask: Flask web framework'ü, uygulamanın API'sini oluşturmak için kullanılmıştır.
- Reddit API: Proje, Reddit API'sini kullanarak subredditlerdeki postları takip etmektedir.
- Docker: Uygulama, Docker kullanılarak konteynerize edilmiştir.
- SQLAlchemy: Veritabanı işlemleri için ORM (Object-Relational Mapping) kütüphanesi.
- Diğer bağımlılıklar: Proje, requirements.txt dosyasında listelenen diğer bağımlılıklara sahiptir.


## Testler

Python Reddit Crawler projesi için birim testleri uygulanmıştır. Bu testler, uygulamanın işlevselliğini ve güvenilirliğini sağlamak amacıyla çeşitli senaryoları ve bileşenleri kapsar.

Testleri çalıştırmak için aşağıdaki adımları izleyin:

1. Proje bağımlılıklarının yüklü olduğundan emin olun. Bağımlılıkları aşağıdaki komutu kullanarak yükleyebilirsiniz:

    pip install -r requirements.txt
    
2. Testleri çalıştırmak için aşağıdaki komutu kullanın: 
    python test.py


-Bu komut, projedeki tüm testleri keşfedecek ve çalıştıracaktır.

3. Konsolda görüntülenen test sonuçlarını kontrol edin. Başarısız olan testler, hata nedeniyle raporlanacaktır.

İhtiyaç duyulması halinde buraya ek test yönergeleri veya talimatları ekleyebilirsiniz.

## Katkıda Bulunma

...



