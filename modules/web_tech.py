import builtwith
try:
 def web_tech_info(url):
    sonuc=builtwith.parse(url)
    print(f"site teknolojileri: {sonuc}")

except Exception as e:
  print("sitede backend veya frontend teknolojisi bulunamadı.")