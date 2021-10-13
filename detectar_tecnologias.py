import requests
import re

from pip._vendor.distlib.compat import raw_input

pagina = raw_input("Que pagina quieres verificar?")

resultado = requests.get('https://' + pagina)

usa_ssl = requests.get('https://' + pagina).status_code
if (usa_ssl == 200):
    print("la pagina: ",pagina +" Usa https")
usa_javascript = resultado.text.find('<script>') > -1
print("Esta pagina usa javascript: ",usa_javascript)

usa_css = resultado.text.find('stylesheet') > -1
print("Esta pagina usa css: ", usa_css)

