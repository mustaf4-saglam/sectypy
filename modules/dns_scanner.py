import dns.resolver
def get_dns_records(domain):
    print(f"Scanning {domain}...")
    try:
        cevap = dns.resolver.resolve(domain, 'A')
        for rdata in cevap:
            print(rdata)

        return rdata

    except dns.resolver.NXDOMAIN:
        print("Domain not found")
    except dns.resolver.Timeout:
        print("Request timed out")
        return 0
