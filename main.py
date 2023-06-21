import ply.lex as lex

tokens = (
  'TEXTO',
  'ENTERO',

  #Tokens para cabecera y article
  'XML',
  'ENCODING',
  'VERSION',
  'OARTICLE',
  'CARTICLE',

  #Tokens para Info
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
  'FREFU',
  'FREFA'
  'VREF',
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

  # Tokens para datos
  'OADD',
  'CADD',
  'OCR',
  'CCR',
  'OSTREET',
  'CSTREET',
  'OCITY',
  'CCITY',
  'OSTATE',
  'CSTATE',
  'OPHONE',
  'CPHONE',
  'OEMAIL',
  'CEMAIL',
  'ODATE',
  'CDATE',
  'OYEAR',
  'CYEAR',
  'OHOLDER',
  'CHOLDER',

  # Tokens para secciones
  'OSIMPSECT',
  'CSIMPSECT',
  'OSECT',
  'CSECT',

  # Tokens para parrafos
  'OPARA',
  'CPARA',
  'OSIMPARA',
  'CSIMPARA',

  # Tokens para abstract
  'OABS',
  'CABS',
)

b_title = True
file = ""


def t_OARTICLE(t):
  r'<article>'
  file.write('''<article>
  <html lang="es">
  <head>
    <meta charset="UTF-8">
    <style>
        .info {
            background: rgb(9, 184, 9);
            color: white;
            font-size: 8pt;
            width: 420px;
            margin: 0px;
            margin-bottom: auto;
        }

        .important {
            background: rgb(237, 27, 24);
            color: white;
            width: 420px;
            margin: 0px;
            margin-bottom: auto;
        }
    </style>
  </head>
  <body>''')
  return t


def t_CARTICLE(t):
  r'</article>'
  file.write("""
</article>
</body>
</html>""")
  return t


def t_XML(t):
  r'<\?xml'
  file.write("<!DOCTYPE html>")
  return t


def t_VERSION(t):
  r'version="\d+\.\d+"'
  return t


def t_ENCODING(t):
  r'encoding="(UTF|utf)-\d+"\?>'
  return t


def t_OINFO(t):
  r'<info>'
  file.write("<div class='info'></div>")
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
  r'<link '
  return t


def t_VREF(t):
  r'xlink:href="(https|http|ftps|ftp)\://((\.|[A-Z]|[a-z])+(?!-)([ÁÉÍÓÚáéíóú\-\w]+|[0-9]+|%(?!2[46B]))(?<!-))(\.|[A-Z]|[a-z])+(\/[A-Za-z0-9._/]+)?(\#(\w.(?!\.))+)?" />'
  return t


def t_IMG(t):
  r'<imagedata '
  return t


def t_VDO(t):
  r'<videodata '
  return t


def t_FREFU(t):
  r'fileref="(https|http|ftps|ftp)\://((\.|[A-Z]|[a-z])+(?!-)([ÁÉÍÓÚáéíóú\-\w]+|[0-9]+|%(?!2[46B]))(?<!-))(\.|[A-Z]|[a-z])+(\/[A-Za-z0-9._/]+)?(\#(\w.(?!\.))+)?" />'
  return t


def t_FREFA(t):
  r'([^<>]+)/>'


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


def t_CEMPHASIS(t):
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
  global b_title
  if (b_title == True):
    file.rewrite("<h1>")
  else:
    file.rewrite("<h2>")
  return t


def t_CTITLE(t):
  r'</title>'
  global b_title
  if (b_title == True):
    file.rewrite("<h1>")
  else:
    file.rewrite("<h2>")
  b_title = False
  return t


def t_OIMPORTANT(t):
  r'<important>'
  file.rewrite(
    "<div class = 'important' >")  #dejé el important entre comillas simples
  return t


def t_CIMPORTANT(t):
  r'</important>'
  file.rewrite("</div >")
  return t


def t_OITEMLIST(t):
  r'<itemizedlist>'
  file.rewrite("<ul>")
  return t


def t_CITEMLIST(t):
  r'</itemizedlist>'
  file.rewrite("</ul>")
  return t


def t_OLISTITEM(t):
  r'<listitem>'
  file.rewrite("<li>")
  return t


def t_CLISTITEM(t):
  r'</listitem>'
  file.rewrite("</li>")
  return t


def t_OADD(t):
  r'<address>'
  return t


def t_CADD(t):
  r'</address>'
  return t


def t_OCR(t):
  r'<copyright>'
  return t


def t_CCR(t):
  r'</copyright>'
  return t


def t_OSTREET(t):
  r'<street>'
  return t


def t_CSTREET(t):
  r'</street>'
  return t


def t_OCITY(t):
  r'<city>'
  return t


def t_CCITY(t):
  r'</city>'
  return t


def t_OSTATE(t):
  r'<state>'
  return t


def t_CSTATE(t):
  r'</state>'
  return t


def t_OPHONE(t):
  r'<phone>'
  return t


def t_CPHONE(t):
  r'</phone>'
  return t


def t_OEMAIL(t):
  r'<email>'
  return t


def t_CEMAIL(t):
  r'</email>'
  return t


def t_ODATE(t):
  r'<date>'
  return t


def t_CDATE(t):
  r'</date>'
  return t


def t_OYEAR(t):
  r'<year>'
  return t


def t_CYEAR(t):
  r'</year>'
  return t


def t_OHOLDER(t):
  r'<holder>'
  return t


def t_CHOLDER(t):
  r'</holder>'
  return t


def t_OSIMPSECT(t):
  r'<simplesect>'
  return t


def t_CSIMPSECT(t):
  r'</simplesect>'
  return t


def t_OSECT(t):
  r'<section>'
  return t


def t_CSECT(t):
  r'</section>'
  return t


def t_OPARA(t):
  r'<para>'
  return t


def t_CPARA(t):
  r'</para>'
  return t


def t_OSIMPARA(t):
  r'<simpara>'
  return t


def t_CSIMPARA(t):
  r'</simpara>'
  return t


def t_OABS(t):
  r'<abstract>'
  return t


def t_CABS(t):
  r'</abstract>'
  return t


def t_TEXTO(t):
  r'([^<>]+)'
  file.write(t.value)


def t_ENTERO(t):
  r'\d+'
  file.write(t.value)
  return t


t_ignore = " \t"


def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)


# CONSTRUCCION DEL PARSER


def p_sigma(p):
  '''sigma: XML VERISON ENCODING OARTICLE IN_ART_SECT CARTICLE | OARTICLE IN_ART_SECT CARTICLE'''


def p_in_art(p):
  '''IN_ART_SECT: INFO TITLE CUERPO SECTION | INFO CUERPO | TITLE CUERPO | INFO TITLE CUERPO | INFO CUERPO SECTION | TITLE CUERPO SECTION'''


def p_cuerpo(p):
  '''CUERPO: ITEMLIST | IMPORTANT | PARA | SIMPARA | ADD | MO |TABLE
| COMMENT | ABS | ITEMLIST CUERPO | IMPORTANT CUERPO|PARA CUERPO|
SIMPARA CUERPO| ADD CUERPO| MO CUERPO|TABLE CUERPO| COMMENT
CUERPO| ABS CUERPO'''


def p_cuerpo2(p):
  '''CUERPO2: TEXTO | EMPHASIS | LINK | EMAIL | AUTH | COMMENT
|TEXTO IN_PARA| EMPHASIS CUERPO2| LINK CUERPO2| EMAIL CUERPO2|
AUTH CUERPO2| COMMENT CUERPO2'''


def p_cuerpo3(p):
  '''CUERPO3: TEXTO| EMPHASIS | LINK | COMMENT | TEXTO CUERPO3 |
EMPHASIS CUERPO3 | LINK CUERPO3 | COMMENT CUERPO3'''


def p_inf(p):
  '''INFO: OINFO IN_INFO CINFO'''


def p_in_inf(p):
  '''IN_INFO: MO | ABS | ADD | AUTH | DATE | CR | TITLE | MO IN_INFO
| ABS IN_INFO | ADD IN_INFO | AUTH IN_INFO | DATE IN_INFO | CR
IN_INFO | TITLE IN_INFO'''


def p_em(p):
  '''EMPHASIS: OEMPHASIS CUERPO2 CEMPHASIS'''


def p_com(p):
  '''COMMENT: OCOMMENT CUERPO2 CCOMMENT'''


def p_title(p):
  '''TITLE: OTITLE IN_TITLE CTITLE'''


def p_in_title(p):
  '''IN_TITLE: #texto 
    | EMPHASIS 
    | LINK 
    | EMAIL 
    | #texto IN_TITLE 
    | EMPHASIS IN_TITLE 
    | LINK IN_TITLE
    | EMAIL IN_TITLE '''


def p_itemized(p):
  '''ITEMLIST: OITEMLIST LIST_ITEM CITEMLIST'''


def p_li(p):
  '''LIST_ITEM: OLISTITEM CUERPO CLISTITEM
    | OLISTITEM CUERPO CLISTITEM LIST_ITEM'''


def p_imp(p):
  '''IMPORTANT: OIMPORTANT TITLE CUERPO CIMPORTANT
    | OIMPORTANT CUERPO CIMPORTANT'''


# Construccion del lexer
lexer = lex.lex()
data = '''
<?xml version="1.0" encoding="UTF-8"?>
<firstname>L¿juandjniuh09089</firstname>
<surname> Suarez </surname>
<author></author>

<imagedata fileref="imagenes/boton.gif"/>
'''

lexer.input(data)

# Tokenización
while True:
  tok = lexer.token()
  if not tok:
    break  # No hay más entradas
  print(tok.type, tok.value, tok.lineno, tok.lexpos)
