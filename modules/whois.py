import whois
def get_whois_info(domain):
    try:
        domain_info = whois.whois(domain)
        print(f"Domain: {domain_info.domain_name}")
        print(f"Registrar: {domain_info.registrar}")
        if type(domain_info.creation_date) == list:
            print(f"Creation Date: domain_info.creation_date[0].strftime('%Y-%m-%d %H:%M:%S')")
            c_date=domain_info.creation_date[0].strftime('%Y-%m-%d %H:%M:%S')
        else:
            print(f"creation date: {domain_info.creation_date.strftime('%Y-%m-%d %H:%M:%S')}")
            c_date=domain_info.creation_date.strftime('%Y-%m-%d %H:%M:%S')
        if type(domain_info.expiration_date) == list:
            print(f"Expiration Date: {domain_info.expiration_date[0].strftime('%Y-%m-%d %H:%M:%S')}")
            e_date={domain_info.expiration_date[0].strftime('%Y-%m-%d %H:%M:%S')}
        else:
            print(f"Expiration Date: {domain_info.expiration_date.strftime('%Y-%m-%d %H:%M:%S')}")
            e_date=domain_info.expiration_date.strftime('%Y-%m-%d %H:%M:%S')
        print(f"Name Servers: {domain_info.name_servers}")
        return {
        'registrar': domain_info.registrar,
        'creation_date': c_date,
        'expiration_date': e_date,
        'name_servers': domain_info.name_servers
        }
    
    except Exception as e:
        print(f"Error retrieving.")
    