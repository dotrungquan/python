import dns.resolver
from prettytable import PrettyTable

def get_dns_records(domain):
    records = {
        'A': [],
        'NS': [],
        'MX': [],
        'TXT': [],
        'CNAME': []
    }

    try:
        answers = dns.resolver.resolve(domain, 'A')
        records['A'] = [str(rdata) for rdata in answers]
    except dns.resolver.NoAnswer:
        pass

    try:
        answers = dns.resolver.resolve(domain, 'NS')
        records['NS'] = [str(rdata) for rdata in answers]
    except dns.resolver.NoAnswer:
        pass

    try:
        answers = dns.resolver.resolve(domain, 'MX')
        records['MX'] = [str(rdata) for rdata in answers]
    except dns.resolver.NoAnswer:
        pass

    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        records['TXT'] = [str(rdata) for rdata in answers]
    except dns.resolver.NoAnswer:
        pass

    try:
        answers = dns.resolver.resolve(domain, 'CNAME')
        records['CNAME'] = [str(rdata) for rdata in answers]
    except dns.resolver.NoAnswer:
        pass

    return records

def print_dns_records(domain):
    records = get_dns_records(domain)

    table = PrettyTable()
    table.field_names = ['A', 'NS', 'MX', 'TXT', 'CNAME']

    max_length = max([len(records[key]) for key in records])

    for i in range(max_length):
        row = [records['A'][i] if i < len(records['A']) else '',
               records['NS'][i] if i < len(records['NS']) else '',
               records['MX'][i] if i < len(records['MX']) else '',
               records['TXT'][i] if i < len(records['TXT']) else '',
               records['CNAME'][i] if i < len(records['CNAME']) else '']
        table.add_row(row)

    print(table)

# Nhập domain từ người dùng
domain = input("Nhập domain: ")
print_dns_records(domain)
