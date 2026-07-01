import argparse
from modules.html_report import html_reporter
from modules.dns_scanner import get_dns_records
from modules.whois import get_whois_info
from modules.http_info import get_http_info
from modules.web_tech import web_tech_info
from modules.port_scanner import get_ports
from datetime import datetime
parser = argparse.ArgumentParser(description="Sectypy aracına hoşgeldiniz")
parser.add_argument("site", help="Hedef site URL'si")
args = parser.parse_args()
hedef_site=args.site
if not hedef_site.startswith("http"):
    http_url = f"https://{hedef_site}"
else:
    http_url = hedef_site
dns_sonuclari=get_dns_records(hedef_site)
whois_sonuclari=get_whois_info(hedef_site)
http_sonuclari=get_http_info(http_url)
webtech_sonuclari=web_tech_info(http_url)
port_sonuclari=get_ports(hedef_site)
html_reporter(hedef_site,whois_sonuclari,port_sonuclari,webtech_sonuclari,http_sonuclari)