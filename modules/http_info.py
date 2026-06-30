import requests

def get_http_info(url):
    try:
       response=requests.get(url)
       if response:
          print(f"baglantı başarılı durum kodu: (connection success satstus code:) {response.status_code}")
          print(f"server ismi: (name server:){response.headers.get('Server')}")
          print(f"Content-Type: {response.headers.get('Content-Type')}")
          if response.status_code in [301, 302, 303, 307, 308]:
             yönlendirilen=response.headers.get('Location')
             print(f"yönlendirilen site: (redirect: ){yönlendirilen}")
          else:
             print("yönlendirilen site bulunmamaktadır. (no rediction.)")

          tum_basliklar=response.headers
          security_headers=[
             'Strict-Transport-Security',
             'Content-Security-Policy',
             'X-Frame-Options',
             'X-Content-Type-Options',
             'Referrer-Policy',
             'Permissions-Policy'
          ]
          for baslik in security_headers:
             deger=tum_basliklar.get(baslik)
             if deger:
                print(f"{baslik}:{deger}")
             else:
                print(f"{baslik}:Bulunamadı (not found)")

             
        

       else:
          print(f"baglantı başarısız. durum kodu: (connection failed. status code:) {response.status_code}")
        
    
       
    




    except requests.exceptions.RequestException as e :
      print(f"siteden yanıt alınamadı. {e}")