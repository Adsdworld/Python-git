import nmap

# Création d'un objet nmap pour effectuer le scan
nm = nmap.PortScanner()

# Définition de l'adresse IP du réseau à scanner
ip_range = input("Entrez l'adresse IP du réseau à scanner (ex: 192.168.1.0/24): ")

# Exécution du scan
nm.scan(hosts=ip_range, arguments='-n -sP')

# Parcours des résultats du scan et affichage dans la console
for host in nm.all_hosts():
    print('Adresse IP : %s (%s)' % (host, nm[host].hostname()))
    print('Etat : %s' % nm[host].state())
