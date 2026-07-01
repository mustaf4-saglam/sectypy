
```
# SectyPy - Web Security Scanner

SectyPy, bir hedef domain üzerindeki açık portları, web teknolojilerini, HTTP güvenlik başlıklarını ve WHOIS bilgilerini analiz edip şık bir HTML raporu sunan kapsamlı bir bilgi toplama aracıdır.

## 🚀 Kurulum Adımları

Projeyi kendi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

**1. Projeyi Klonlayın**
```bash
git clone [https://github.com/SENIN_KULLANICI_ADIN/sectypy.git](https://github.com/SENIN_KULLANICI_ADIN/sectypy.git)
cd sectypy

```

**2. Sanal Ortam (Virtual Environment) Oluşturun ve Aktif Edin**
Projeyi izole bir ortamda çalıştırmak en iyi uygulamadır.

* **Linux / macOS için:**

```bash
python3 -m venv venv
source venv/bin/activate

```

* **Windows için:**

```cmd
python -m venv venv
venv\Scripts\activate

```

**3. Gerekli Kütüphaneleri Kurun**

```bash
pip install -r requirements.txt

```

## 🛠️ Kullanım

SectyPy'ı kullanmak oldukça basittir. Sanal ortamınız (`venv`) aktifken terminal veya komut istemcisi üzerinden ana dosyayı çalıştırmanız yeterlidir. Hedef olarak çıplak bir domain veya `https://` içeren tam bir URL verebilirsiniz; SectyPy bunu otomatik olarak algılayıp düzenler.

**Temel Kullanım:**

```bash
python main.py example.com

```

**URL ile Kullanım:**

```bash
python main.py [https://owasp.org](https://owasp.org)

```

### 📊 Neler Taranır?

Komutu çalıştırdığınızda SectyPy hedef üzerinde arka planda şu analizleri gerçekleştirir:

* **DNS Çözümleme:** Hedefin bağlı olduğu güncel IP adres(ler)ini tespit eder.
* **WHOIS Sorgusu:** Domain kayıt tarihi, bitiş tarihi, Name Server (NS) ve Registrar bilgilerini çeker.
* **Port Taraması:** Sistemde açık olabilecek en popüler 50 kritik TCP portunu hızlıca tarar.
* **Web Teknolojileri:** Hedef sitenin altyapısında çalışan CDN, framework ve sunucu teknolojilerini tespit eder (Örn: Cloudflare, Apache, jQuery).
* **HTTP Güvenlik Başlıkları:** Sitenin güvenlik yapılandırmasını analiz ederek eksik veya yapılandırılmış başlıkları (X-Frame-Options, CSP, HSTS vb.) listeler.

### 📄 Çıktı ve Raporlama

Tarama başarıyla tamamlandığında aracın bulunduğu dizinde, karanlık temalı (Dark Mode) ve modern bir arayüze sahip özel bir HTML raporu oluşturulur.

Örnek çıktı dosyası: `example.com_html_report.html`

Oluşturulan bu `.html` dosyasını üzerine çift tıklayarak herhangi bir web tarayıcısında (Chrome, Firefox, Safari vb.) açabilir ve tüm analiz sonuçlarını tek bir şık ekranda inceleyebilirsiniz.

```

```
