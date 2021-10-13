from bs4 import BeautifulSoup
import urllib.request

pagina = input("Ingresa la pagina: ")

contenido = urllib.request.urlopen(pagina).read()

obtener_codigo_html = BeautifulSoup(contenido, 'html.parser')

for links in obtener_codigo_html.find_all('a'):
    print(links.get('href'))
