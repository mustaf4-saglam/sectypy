import argparse
from modules.dns_scanner import get_dns_records
from modules.whois import get_whois_info
from modules.http_info import get_http_info
from modules.web_tech import web_tech_info
from datetime import datetime
parser = argparse.ArgumentParser(description="Sectypy aracına hoşgeldiniz")
parser.add_argument("site", help="Hedef site URL'si")
args = parser.parse_args()
get_dns_records(args.site)
get_whois_info(args.site)
get_http_info(args.site)
web_tech_info(args.site)