import ply.lex as lex
from sys import stdin

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
  'LINKO',
  'IMGO',
  'VDOO',
  'FREF',
  'FREFA',
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
aux_entry = 1
file = ""


def t_OARTICLE(t):
  r'<article>'
  file.write(
    "<html lang='es'> <head> <meta charset='UTF-8'> <style>. info { background: rgb(9, 184, 9); color: white; font-size: 8pt; width: 420px; margin: 0px; margin-bottom: auto;}.important {background: rgb(237, 27, 24);color: white;width: 420px;margin: 0px; margin-bottom: auto;} </style> </head> <body>"
  )
  return t


def t_CARTICLE(t):
  r'</article>'
  file.write("</body></html>")
  return t


def t_XML(t):
  r'<\?xml'
  # file.write("<!DOCTYPE html>")
  return t


def t_VERSION(t):
  r'version="\d+\.\d+"'
  return t


def t_ENCODING(t):
  r'encoding="(UTF|utf)-\d+"\?>'
  return t


def t_OINFO(t):
  r'<info>'
  file.write("<div class='info'>")
  return t


def t_CINFO(t):
  r'</info>'
  file.write("</div>")
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
  file.write("<table>")
  return t


def t_CTABLE(t):
  r'</informaltable>'
  file.write("</table>")
  return t


def t_OTGROUP(t):
  r'<tgroup>'
  return t


def t_CTGROUP(t):
  r'</tgroup>'
  return t


def t_OTHEAD(t):
  r'<thead>'
  file.write("<thead>")
  return t


def t_CTHEAD(t):
  r'</thead>'
  file.write("</thead>")
  return t


def t_OTFOOT(t):
  r'<tfoot>'
  file.write("<tfoot>")
  return t


def t_CTFOOT(t):
  r'</tfoot>'
  file.write("</tfoot>")
  return t


def t_OTBODY(t):
  r'<tbody>'
  file.write("<tbody>")
  return t


def t_CTBODY(t):
  r'</tbody>'
  file.write("</tbody>")
  return t


def t_OROW(t):
  r'<row>'
  file.write("<tr>")
  return t


def t_CROW(t):
  r'</row>'
  global aux_entry
  aux_entry += 1  #Cuento las filas de la tabla, para la 1er Fila se tendrá un contenido resaltado, las demas ya no...
  file.write("</tr>")
  return t


def t_OENTRY(t):
  r'<entry>'
  global aux_entry
  if aux_entry == 1:
    file.write("<th>")
  else:
    file.write("<td>")
  return t


def t_CENTRY(t):
  r'</entry>'
  global aux_entry
  if aux_entry == 1:
    file.write("</th>")
  else:
    file.write("</td>")
  return t


def t_OENTRYTBL(t):
  r'<entrytbl>'
  file.write("<table>")
  return t


def t_CENTRYTBL(t):
  r'</entrytbl>'
  file.write("</table>")
  return t


def t_LINKO(t):
  r'<link '
  file.write("<html:a")
  return t


def t_VREF(t):
  r'xlink:href='
  file.write(" href =")
  return t


def t_IMGO(t):
  r'<imagedata '
  file.write("<html:a")
  return t


def t_VDOO(t):
  r'<videodata '
  file.write("<html:a")
  return t


def t_FREF(t):
  r'fileref='
  file.write(" fileref=")
  return t


def t_URL(t):
  r'(https|http|ftps|ftp)\://((\.|[A-Z]|[a-z])+(?!-)([ÁÉÍÓÚáéíóú\-\w]+|[0-9]+|%(?!2[46B]))(?<!-))(\.|[A-Z]|[a-z])+(\/[A-Za-z0-9._/]+)?(\#(\w.(?!\.))+)?/>'
  file.write(t.value[:-2] + "></html:a>")
  return t


def t_FREFA(t):
  r'([^<>]+)/>'
  file.write(t.value[:-2] + "></html:a>")
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
  file.write("<strong>")
  return t


def t_CEMPHASIS(t):
  r'</emphasis>'
  file.write("</strong>")
  return t


def t_OCOMMENT(t):
  r'<comment>'
  file.write("<!--")
  return t


def t_CCOMMENT(t):
  r'</comment>'
  file.write("-->")
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
  file.rewrite("<div class = 'important' >")
  return t


def t_CIMPORTANT(t):
  r'</important>'
  file.rewrite("</div>")
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
  global b_cierre
  b_cierre = False
  return t


def t_CSECT(t):
  r'</section>'
  global b_cierre
  b_cierre = True
  return t


def t_OPARA(t):
  r'<para>'
  file.rewrite("<p>")
  return t


def t_CPARA(t):
  r'</para>'
  file.rewrite("</p>")
  return t


def t_OSIMPARA(t):
  r'<simpara>'
  file.rewrite("<p>")
  return t


def t_CSIMPARA(t):
  r'</simpara>'
  file.rewrite("</p>")
  return t


def t_OABS(t):
  r'<abstract>'
  return t


def t_CABS(t):
  r'</abstract>'
  return t


def t_TEXTO(t):
  r'([^<>]+)'
  # file.write(t.value)


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


# Construccion del lexer
lexer = lex.lex()
with open('prueba.txt', 'r') as file:
  contenido = file.read()

#data = open("prueba.txt", "w")

lexer.input(contenido)

# Tokenización
while True:
  tok = lexer.token()
  if not tok:
    break  # No hay más entradas
  print(tok.type, tok.value, tok.lineno, tok.lexpos)

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
  '''IN_TITLE: TEXTO 
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


def p_add(p):
  '''ADD: OADD IN_ADD CADD'''


def p_inn_add(p):
  '''IN_ADD: TEXTO | STREET | CITY | STATE | PHONE | EMAIL             
    | #texto IN_ADD | STREET IN_ADD | CITY IN_ADD |STATE IN_ADD | PHONE IN_ADD | EMAIL IN_ADD |'''


def p_cr(p):
  '''CR: OCR IN_YEAR IN_HOLDER CCR 
    | OCR IN_YEAR  CCR'''


def p_in_year(p):
  '''IN_YEAR: YEAR | YEAR IN_YEAR'''


def p_in_holder(p):
  '''IN_HOlDER: HOLDER | HOLDER IN_HOLDER'''


def p_street(p):
  '''STREET: OSTREET CUERPO3 CSTREET'''


def p_city(p):
  '''CITY: OCITY CUERPO3 CCITY'''


def p_state(p):
  '''STATE: OSTATE CUERPO3 CSTATE'''


def p_phone(p):
  '''PHONE: OPHONE CUERPO3 CPHONE'''


def p_email(p):
  '''EMAIL: OEMAIL CUERPO3 OEMAIL'''


def p_date(p):
  '''DATE: ODATE CUERPO3 CDATE'''


def p_year(p):
  '''YEAR: OYEAR CUERPO3 CYEAR'''


def p_holder(p):
  '''HOLDER: OHOLDER CUERPO3 CHOLDER'''


def p_section(p):
  '''SECTION:  SECT | SIMPSECT'''


def p_simpsect(p):
  '''SIMPSECT: OSIMPSECT IN_SIMPSECT CSIMPSECT | 
    OSIMPSECT IN_SIMPSECT CSIMPSECT SIMPSECT'''


def p_sect(p):
  '''SECT: OSECT IN_ART_SECT CSECT | 
    OSECT IN_ART_SECT CSECT SECT'''


def p_paragraph(p):
  '''PARAGRAPH: PARA PARAGRAPH | 
    SIMPARA PARAGRAPH |
    PARA | SIMPARA'''


def p_para(p):
  '''PARA: OPARA IN_PARA CPARA'''


def p_in_para(p):
  '''IN_PARA:  ITEMLIST | IMPORTANT | ADD | MO | TABLE | TEXTO |EMPHASIS | LINK | EMAIL | AUTH | COMMENT | 
    TEXTO IN_PARA | EMPHASIS IN_PARA | LINK IN_PARA | EMAIL IN_PARA | AUTH IN_PARA | COMMENT IN_PARA | ITEMLIST IN_PARA | IMPORTANT IN_PARA | ADD IN_PARA | MO IN_PARA | TABLE IN_PARA '''


def p_simpara(p):
  '''SIMPARA: OSIMPARA CUERPO2 CSIMPARA'''


def p_abs(p):
  '''ABS: OABS TITLE PARAGRAPH CABS | OABS PARAGRAPH CABS'''


#TABLAS
def p_table(p):
  '''TABLE: OTABLE TABLE_MO TGROUP CTABLE'''


def p_table_mo(p):
  '''TABLE_MO: MO TABLE_MO|MO'''


def p_tgroup(p):
  '''TGROUP: OTGROUP TBODY CTGROUP TGROUP|OTGROUP THEAD TBODY CTGROUP TGROUP|OTGROUP TFOOT TBODY CTGROUP TGROUP
      |OTGROUP TBODY CTGROUP| OTGROUP THEAD TBODY CTGROUP|OTGROUP TFOOT TBODY CTGROUP| OTGROUP THEAD TFOOT TBODY CTGROUP'''


def p_thead(p):
  '''THEAD: OTHEAD FILA CTHEAD'''


def p_tfoot(p):
  '''TFOOT: OTFOOT FILA CTFOOT'''


def p_tbody(p):
  '''TBODY: OTBODY FILA CTBODY'''


def p_fila(p):
  '''FILA: OROW ENTRY CROW|OROW ENTRYTBL CROW|OROW ENTRY CROW FILA|OROW ENTRYTBL CROW FILA'''


def p_entry(p):
  '''ENTRY: OENTRY IN_ENTRY CENTRY'''


def p_in_entry(p):
  '''IN_ENTRY: TEXTO|ITEMLIST|IMPORTANT|PARA|SIMPARA|MO|COMMENT|ABT| TEXTO ENTRY| ITEMLIST ENTRY| IMPORTANT ENTRY|
            PARA ENTRY| SIMPARA ENTRY|MO ENTRY| COMMENT ENTRY|ABT ENTRY'''


def p_entrytbl(p):
  '''ENTRYTBL: OENTRYTBL TBODY CENTRYTBL| OENTRYTBL THEAD TBODY CENTRYTBL'''


#MULTIMEDIA
def p_link(p):
  '''LINK: LINKO VREF URL'''


def p_img(p):
  '''IMG: IMGO FREF FREFA '''


def p_vdo(p):
  '''VDO: VDOO FREF FREFA'''


def p_mo(p):
  '''MO: OMO INFO IN_MO CMO| OMO IN_MO CMO'''


def p_in_mo(p):
  '''IN_MO: VDOBJECT | IMGOBJECT |VDOBJECT IN_MO| IMGOBJECT IN_MO'''


def p_vdobject(p):
  '''VDOBJECT: OVIDOBJ INFO VDO CVIDOBJ |OVIDOBJ VDO CVIDOBJ'''


def p_imgobject(p):
  '''IMGOBJECT: OIMGOBJ INFO IMG CIMGOBJ |OIMGOBJ IMG CIMGOBJ'''
