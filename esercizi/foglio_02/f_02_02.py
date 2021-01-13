import re

pattern = '^[RDTAC]?x?[a-h][1-8]$'

def check_chess_syntax(text):
  # Check stringa
  if not isinstance(text,str):
    raise Exception("L'input non è una stringa!")
    
  # Check validità dell'espressione
  if text!="0-0" and text!="0-0-0" and re.match(pattern,text) is None: 
    raise Exception("L'input non è una mossa valida!")


# TEST
for text in [
    # VALID SAMPLES
    'a2','xc5','0-0','Tg8','Rxb7',
    # INVALID SAMPLES
    'a9','Ga2','sbricci','']:
  try:
    check_chess_syntax(text)
  except:
    print("'{}' is INVALID".format(text))
  else:
    print("'{}' is a valid move".format(text))

# Solo i primi cinque input devono risultare validi
