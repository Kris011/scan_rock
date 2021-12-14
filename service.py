import os
import requests
os.system('clear')
print("""\033[1;34m"
╶▄▄╶╶╶╶▄▄╶╶╶╶▄▄▄╶╶╶▐╶▄╶╶╶╶╶╶▄▄▄╶╶╶╶╶╶╶╶╶╶▄▄╶╶╶▄╶╶▄╶╶
▐█╶▀╶╶▐█╶▌╶╶▐█╶▀█╶╶█▌▐█╶╶╶╶╶▀▄╶█╶╶╶╶╶╶╶╶▐█╶▌╶╶█▌▄▌╶╶
▄▀▀▀█▄██╶▄▄╶▄█▀▀█╶▐█▐▐▌╶╶╶╶╶▐▀▀▄╶╶╶▄█▀▄╶██╶▄▄╶▐▀▀▄╶╶
▐█▄╶▐█▐███▌╶▐█╶╶▐▌██▐█▌╶╶╶╶╶▐█╶█▌╶▐█▌╶▐▌▐███▌╶▐█╶█▌╶
╶▀▀▀▀╶╶▀▀▀╶╶╶▀╶╶▀╶▀▀╶█╶╶╶╶╶╶╶▀╶╶▀╶╶▀█▄▀╶╶▀▀▀╶╶╶▀╶╶▀╶
--Creado por Hector Diaz >:)
--Github https://github.com/Kris011
    (Recomendado ultilizarlo en un lugar visible por ejemplo en Desktop o en una carpeta)
\033[0m""")
vv = input("Dominio: ")
domain = vv
file = open("subdomains.txt")
content = file.read()
subdomains = content.splitlines()
discovered_subdomains = []
for subdomain in subdomains:
    url = f"http://{subdomain}.{domain}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("[-] Subdominio Descubierto:", url)
        discovered_subdomains.append(url)
with open ("subdominios_descubiertos.txt", "w") as f:
    for subdomain in discovered_subdomains:
        print(subdomain, file=f)
