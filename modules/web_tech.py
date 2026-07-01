import builtwith
def web_tech_info(url):
    try:
      
     sonuc=builtwith.parse(url)
     print(f"site teknolojileri: {sonuc}")
     return sonuc
    except Exception as e:
     print("sitede backend veya frontend teknolojisi bulunamadı.")
     return 0
    