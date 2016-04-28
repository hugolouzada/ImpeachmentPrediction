from unicodedata import normalize
import re

#from http://wiki.python.org.br/RemovedorDeAcentos
def remover_acentos(txt):
  return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')

def remove_ponctuations(txt):
    return re.sub(r'[^0-9a-zA-Z_\s]','',txt)

def sanitizeString(txt):
    return remove_ponctuations(remover_acentos(txt))

txt = '[ACENTUAÇÃO] ç: áàãâä! éèêë? íì&#297;îï, óòõôö; úù&#361;ûü.'
print(txt)
print(sanitizeString(txt))
print(remover_acentos(txt))
print(remove_ponctuations(txt))
