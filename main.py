import ply.lex as lex
'''CHAR', hay que borrar char de la gramatica tambien. Lo de xml no se si esta bien literal copie y pegue ese'''

tokens = (
  'TEXTO',
  'ENTERO',
  'XML',
  'ENCODING',
  'VERSION',
  'OARTICLE',
  'CARTICLE',
  'OINFO',
  'CINFO',
  'OAUTH',
  'CAUTH',
  'OFIRSTNAME',
  'CFIRSTNAME',
  'OSURNAME',
  'CSURNAME',

  #Tokens para Tablas
  'OTABLE',
  'CTABLE',
  'OTGROUP',
  'CTGROUP',
  'OTHEAD',
  'CTHEAD',
  'OTFOOT',
  'CTFOOT',
  'OTBODY',
  'CTBODY',
  'OROW',
  'CROW',
  'OENTRY',
  'CENTRY',
  'OENTRYTBL',
  'CENTRYTBL',

  #Tokens para Elementos Multimedia
  'URL',
  'LINK',
  'IMG',
  'VDO',
  'OMO',
  'CMO',
  'OVIDOBJ',
  'CVIDOBJ',
  'OIMGOBJ',
  'CIMGOBJ',
  
  # Tokens para el enfásis
	'OEMPHASIS',
	'CEMPHASIS',

# Tokens para comentarios
	'OCOMMENT',
	'CCOMMENT',

# Tokens para título
	'OTITLE',
	'CTITLE',

# Tokens para important
	'OIMPORTANT',
	'CIMPORTANT',

# Tokens para listas 
	'OITEMLIST',
	'CITEMLIST',
	'OLISTITEM',
	'CLISTITEM',
)


def t_OARTICLE(t):
  r'<article>'
  return t


def t_CARTICLE(t):
  r'</article>'
  return t


def t_XML(t):
  r'<\?xml'
  return t


def t_VERSION(t):
  r'version="\d+\.\d+"'
  return t


def t_ENCODING(t):
  r'encoding="(UTF|utf)-\d+"\?>'
  return t


def t_OINFO(t):
  r'<info>'
  return t


def t_CINFO(t):
  r'</info>'
  return t


def t_OAUTH(t):
  r'<author>'
  return t


def t_CAUTH(t):
  r'</author>'
  return t


def t_OFIRSTNAME(t):
  r'<firstname>'
  return t


def t_CFIRSTNAME(t):
  r'</firstname>'
  return t


def t_OSURNAME(t):
  r'<surname>'
  return t


def t_CSURNAME(t):
  r'</surname>'
  return t


def t_OTABLE(t):
  r'<informaltable>'
  return t


def t_CTABLE(t):
  r'</informaltable>'
  return t


def t_OTGROUP(t):
  r'<tgroup>'
  return t


def t_CTGROUP(t):
  r'</tgroup>'
  return t


def t_OTHEAD(t):
  r'<thead>'
  return t


def t_CTHEAD(t):
  r'</thead>'
  return t


def t_OTFOOT(t):
  r'<tfoot>'
  return t


def t_CTFOOT(t):
  r'</tfoot>'
  return t


def t_OTBODY(t):
  r'<tbody>'
  return t


def t_CTBODY(t):
  r'</tbody>'
  return t


def t_OROW(t):
  r'<row>'
  return t


def t_CROW(t):
  r'</row>'
  return t


def t_OENTRY(t):
  r'<entry>'
  return t


def t_CENTRY(t):
  r'</entry>'
  return t


def t_OENTRYTBL(t):
  r'<entrytbl>'
  return t


def t_CENTRYTBL(t):
  r'</entrytbl>'
  return t


def t_URL(t):
  r'(https|http|ftps|ftp)\://((\.|[A-Z]|[a-z])+(?!-)([ÁÉÍÓÚáéíóú\-\w]+|[0-9]+|%(?!2[46B]))(?<!-))(\.|[A-Z]|[a-z])+(\/[A-Za-z0-9._/]+)?(\#(\w.(?!\.))+)?'
  return t


def t_LINK(t):
  r'<link xlink:href="{URL}" />'
  return t


def t_IMG(t):
  r'<imagedata fileref="{URL}" />'
  return t


def t_VDO(t):
  r'<videodata fileref="{URL}" />'
  return t


def t_OMO(t):
  r'<mediaobject>'
  return t


def t_CMO(t):
  r'</mediaobject>'
  return t


def t_OVIDOBJ(t):
  r'<videoobject>'
  return t


def t_CVIDOBJ(t):
  r'</videoobject>'
  return t


def t_OIMGOBJ(t):
  r'<imageobject>'
  return t


def t_CIMGOBJ(t):
  r'</imageobject>'
  return t
def t_OEMPHASIS(t):
		r'<emphasis>'
		return t

def t_OEMPHASIS(t):				
  r'</emphasis>'
  return t

def t_OCOMMENT(t):
  r'<comment>'
  return t

def t_CCOMMENT(t):
  r'</comment>'
  return t

def t_OTITLE(t):
  r'<title>'
  return t

def t_CTITLE(t):
  r'</title>'
  return t

def t_OIMPORTANT(t):
  r'<important>'
  return t

def t_CIMPORTANT(t):
  r'</important>'
  return t

def t_OITEMLIST(t):
  r'<itemizedlist>'
  return t

def t_CITEMLIST(t):
  r'</itemizedlist>'
  return t

def t_OLISTITEM(t):
  r'<listitem>'
  return t

def t_CLISTITEM(t):
  r'</listitem>'
  return t

def t_TEXTO(t):
  r'([^<>]+)'


def t_ENTERO(t):
  r'\d+'
  return t


t_ignore = " \t"


def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)


# Construccion del lexer
lexer = lex.lex()
data = '''
<surname> jashasj </surname>

<?xml version="1.0" encoding="UTF-8"?>
jekjkfjkdfjksf
<author>

'''

lexer.input(data)

# Tokenize
while True:
  tok = lexer.token()
  if not tok:
    break  # No more input
  print(tok.type, tok.value, tok.lineno, tok.lexpos)
