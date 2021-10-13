import argparse
import requests
import validators
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from bs4 import Comment

parser = argparse.ArgumentParser(description="Analizador de paginas web")
parser.add_argument("-v", "--version", action='version', version='%(prog)s 1.0')
parser.add_argument("url", type=str, help="La pagina web que se analizara")

args = parser.parse_args()

url = args.url

if validators.url(url):
    result_html = requests.get(url).text
    parser_url = BeautifulSoup(result_html, 'html.parser')
    forms = (parser_url.find_all('form'))
    #print(forms)
    for form in forms:
        if((form.get('action').find('https') < 0) and (urlparse(url).scheme != 'https')):
            formulario_seguro = False
            print("Los datos de login en: " +form.get('action') + " Pueden ser capturados por un sniffer")
        else:
            print("Los datos de login en: " +form.get('action') + " Son seguros")
else:
    print("No ingresaste una pagina web, ingresa como debe ser una url completa, ejemplo https://www.taringa.net")