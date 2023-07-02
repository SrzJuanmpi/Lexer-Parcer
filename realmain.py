import ply.lex as lex
import ply.yacc as yacc
import sys

valido = True
html = ""

tokens = (
  "TEXTO",
  # Tokens para cabecera y article
  "XML",
  "ENCODING",
  "VERSION",
  "OARTICLE",
  "CARTICLE",
  # Tokens para Info
  "OINFO",
  "CINFO",
  "OAUTH",
  "CAUTH",
  "OFIRSTNAME",
  "CFIRSTNAME",
  "OSURNAME",
  "CSURNAME",
  # Tokens para Tablas
  "OTABLE",
  "CTABLE",
  "OTGROUP",
  "CTGROUP",
  "OTHEAD",
  "CTHEAD",
  "OTFOOT",
  "CTFOOT",
  "OTBODY",
  "CTBODY",
  "OROW",
  "CROW",
  "OENTRY",
  "CENTRY",
  "OENTRYTBL",
  "CENTRYTBL",
  # Tokens para Elementos Multimedia
  "LINKO",
  "IMGO",
  "VDOO",
  "FREF",
  "FREFA",
  "VREF",
  "OMO",
  "CMO",
  "OVIDOBJ",
  "CVIDOBJ",
  "OIMGOBJ",
  "CIMGOBJ",
  # Tokens para el enfásis
  "OEMPHASIS",
  "CEMPHASIS",
  # Tokens para comentarios
  "OCOMMENT",
  "CCOMMENT",
  # Tokens para título
  "OTITLE",
  "CTITLE",
  # Tokens para important
  "OIMPORTANT",
  "CIMPORTANT",
  # Tokens para listas
  "OITEMLIST",
  "CITEMLIST",
  "OLISTITEM",
  "CLISTITEM",
  # Tokens para datos
  "OADD",
  "CADD",
  "OCR",
  "CCR",
  "OSTREET",
  "CSTREET",
  "OCITY",
  "CCITY",
  "OSTATE",
  "CSTATE",
  "OPHONE",
  "CPHONE",
  "OEMAIL",
  "CEMAIL",
  "ODATE",
  "CDATE",
  "OYEAR",
  "CYEAR",
  "OHOLDER",
  "CHOLDER",
  # Tokens para secciones
  "OSIMPSECT",
  "CSIMPSECT",
  "OSECT",
  "CSECT",
  # Tokens para parrafos
  "OPARA",
  "CPARA",
  "OSIMPARA",
  "CSIMPARA",
  # Tokens para abstract
  "OABS",
  "CABS",
)

b_title = True
aux_entry = 1
file = ""


def t_OARTICLE(t):
  r"<article>"
  global html
  html += "<H1>"
  return t


def t_CARTICLE(t):
  r"</article>"
  global html
  html += "</H1>"
  return t


def t_XML(t):
  r"<\?xml"
  return t


def t_VERSION(t):
  r'version="\d+\.\d+"'
  return t


def t_ENCODING(t):
  r'encoding="(UTF|utf)-\d+"\?>'
  return t


def t_OINFO(t):
  r"<info>"
  global html
  html += '<div style="background-color: green; color: white; font-size: 8pt;">'
  return t


def t_CINFO(t):
  r"</info>"
  global html
  html += '</div>'
  return t


def t_OAUTH(t):
  r"<author>"
  return t


def t_CAUTH(t):
  r"</author>"
  return t


def t_OFIRSTNAME(t):
  r"<firstname>"
  return t


def t_CFIRSTNAME(t):
  r"</firstname>"
  return t


def t_OSURNAME(t):
  r"<surname>"
  return t


def t_CSURNAME(t):
  r"</surname>"
  return t


def t_OTABLE(t):
  r"<informaltable>"

  return t


def t_CTABLE(t):
  r"</informaltable>"
  return t


def t_OTGROUP(t):
  r"<tgroup>"
  return t


def t_CTGROUP(t):
  r"</tgroup>"
  return t


def t_OTHEAD(t):
  r"<thead>"

  return t


def t_CTHEAD(t):
  r"</thead>"

  return t


def t_OTFOOT(t):
  r"<tfoot>"

  return t


def t_CTFOOT(t):
  r"</tfoot>"

  return t


def t_OTBODY(t):
  r"<tbody>"

  return t


def t_CTBODY(t):
  r"</tbody>"

  return t


def t_OROW(t):
  r"<row>"

  return t


def t_CROW(t):
  r"</row>"

  return t


def t_OENTRY(t):
  r"<entry>"

  return t


def t_CENTRY(t):
  r"</entry>"

  return t


def t_OENTRYTBL(t):
  r"<entrytbl>"

  return t


def t_CENTRYTBL(t):
  r"</entrytbl>"

  return t


def t_LINKO(t):
  r'<link\s*xlink:href="((?:http|https|ftp|ftps)://[^"]+)"/>'

  return t


def t_IMGO(t):
  r"<imagedata"

  return t


def t_VDOO(t):
  r"<videodata"

  return t


def t_FREF(t):
  r"fileref="

  return t


def t_FREFA(t):
  r"([^<>]+)/>"
  return t


def t_OMO(t):
  r"<mediaobject>"
  return t


def t_CMO(t):
  r"</mediaobject>"
  return t


def t_OVIDOBJ(t):
  r"<videoobject>"
  return t


def t_CVIDOBJ(t):
  r"</videoobject>"
  return t


def t_OIMGOBJ(t):
  r"<imageobject>"
  return t


def t_CIMGOBJ(t):
  r"</imageobject>"
  return t


def t_OEMPHASIS(t):
  r"<emphasis>"
  return t


def t_CEMPHASIS(t):
  r"</emphasis>"
  return t


def t_OCOMMENT(t):
  r"<comment>"
  return t


def t_CCOMMENT(t):
  r"</comment>"
  return t


def t_OTITLE(t):
  r"<title>"
  return t


def t_CTITLE(t):
  r"</title>"
  return t


def t_OIMPORTANT(t):
  r"<important>"
  return t


def t_CIMPORTANT(t):
  r"</important>"

  return t


def t_OITEMLIST(t):
  r"<itemizedlist>"

  return t


def t_CITEMLIST(t):
  r"</itemizedlist>"

  return t


def t_OLISTITEM(t):
  r"<listitem>"
  return t


def t_CLISTITEM(t):
  r"</listitem>"
  return t


def t_OADD(t):
  r"<address>"
  return t


def t_CADD(t):
  r"</address>"
  return t


def t_OCR(t):
  r"<copyright>"
  return t


def t_CCR(t):
  r"</copyright>"
  return t


def t_OSTREET(t):
  r"<street>"
  return t


def t_CSTREET(t):
  r"</street>"
  return t


def t_OCITY(t):
  r"<city>"
  return t


def t_CCITY(t):
  r"</city>"
  return t


def t_OSTATE(t):
  r"<state>"
  return t


def t_CSTATE(t):
  r"</state>"
  return t


def t_OPHONE(t):
  r"<phone>"
  return t


def t_CPHONE(t):
  r"</phone>"
  return t


def t_OEMAIL(t):
  r"<email>"
  return t


def t_CEMAIL(t):
  r"</email>"
  return t


def t_ODATE(t):
  r"<date>"
  return t


def t_CDATE(t):
  r"</date>"
  return t


def t_OYEAR(t):
  r"<year>"
  return t


def t_CYEAR(t):
  r"</year>"
  return t


def t_OHOLDER(t):
  r"<holder>"
  return t


def t_CHOLDER(t):
  r"</holder>"
  return t


def t_OSIMPSECT(t):
  r"<simplesect>"
  return t


def t_CSIMPSECT(t):
  r"</simplesect>"
  return t


def t_OSECT(t):
  r"<section>"
  return t


def t_CSECT(t):
  r"</section>"

  return t


def t_OPARA(t):
  r"<para>"
  global html
  html += "<p>"
  return t


def t_CPARA(t):
  r"</para>"
  global html
  html += "</p>"
  return t


def t_OSIMPARA(t):
  r"<simpara>"
  global html
  html += "<p>"
  return t


def t_CSIMPARA(t):
  r"</simpara>"
  global html
  html += "</p>"
  return t


def t_OABS(t):
  r"<abstract>"
  return t


def t_CABS(t):
  r"</abstract>"
  return t


def t_TEXTO(t):
  r'([a-zA-ZÑñ]+|[0-9]+|á|é|í|ó|ú|Á|É|Í|Ó|Ú|\-|_|\#|&|\(|\)|\?|\¿|!|¡|\,|\=|\.|/+|"|;|:|\ +|@ )+'
  global html
  html += t.value
  return t


t_ignore = ' \t' ' \n'


def t_error(t):
  if t:
    line, column = find_line_column2(t.lexer.lexdata, t)
    print(
      "Error de sintaxis en la entrada: token '{0}', línea {1}, posición {2}".
      format(t.value, line, column))
  t.lexer.skip(1)


def find_line_column2(input_text, token):
  last_cr = input_text.rfind('\n', 0, token.lexpos)
  if last_cr < 0:
    last_cr = 0
  line = input_text.count('\n', 0, token.lexpos) + 1
  column = (token.lexpos - last_cr)
  return line, column


# Construccion del lexer
lexer = lex.lex()


def get_tokens():
  filename = input("Ingrese el nombre del archivo de texto: ")
  try:
    with open(filename, 'r', encoding='utf-8') as file:
      data = file.read()
      lexer.input(data)
      for token in lexer:
        print("Token:", token.type)
        print("Contenido:", token.value)
  except FileNotFoundError:
    print("Archivo no encontrado.")


#get_tokens()

# Tokenización

# CONSTRUCCION DEL PARSER


def p_E(p):
  """E : XMLVERSION ARTICULO """


pass


def p_ARTICULO(p):
  """ARTICULO : OARTICLE IN_ART_SECT CARTICLE """


pass


def p_XMLVERSION(p):
  """XMLVERSION : XML VERSION ENCODING"""


pass


def p_empty(p):
  '''
    empty :
    '''
  pass


def p_IN_ART_SECT(p):
  '''IN_ART_SECT : INFO TITLE CUERPO SECTION
    | INFO CUERPO
    | TITLE CUERPO
    | INFO TITLE CUERPO
    | INFO CUERPO SECTION
    | TITLE CUERPO SECTION'''


def p_cuerpo(p):
  """CUERPO : ITEMLIST
    | IMPORTANT
    | PARA
    | SIMPARA
    | ADD
    | MO
    | TABLE
    | COMMENT
    | ABS
    | ITEMLIST CUERPO
    | IMPORTANT CUERPO
    | PARA CUERPO
    | SIMPARA CUERPO
    | ADD CUERPO
    | MO CUERPO
    | TABLE CUERPO
    | COMMENT CUERPO
    | ABS CUERPO"""


def p_cuerpo2(p):
  """CUERPO2 : TEXTO
    | EMPHASIS
    | LINK
    | EMAIL
    | AUTH
    | COMMENT
    | TEXTO IN_PARA
    | EMPHASIS CUERPO2
    | LINK CUERPO2
    | EMAIL CUERPO2
    | AUTH CUERPO2
    | COMMENT CUERPO2"""


def p_cuerpo3(p):
  """CUERPO3 : TEXTO
    | EMPHASIS
    | LINK
    | COMMENT
    | TEXTO CUERPO3
    | EMPHASIS CUERPO3
    | LINK CUERPO3
    | COMMENT CUERPO3"""


def p_inf(p):
  """INFO : OINFO IN_INFO CINFO"""


def p_in_inf(p):
  """IN_INFO : MO
    | ABS
    | ADD
    | AUTH
    | DATE
    | CR
    | TITLE
    | MO IN_INFO
    | ABS IN_INFO
    | ADD IN_INFO
    | AUTH IN_INFO
    | DATE IN_INFO
    | CR IN_INFO
    | TITLE IN_INFO"""


def p_author(p):
  '''AUTH : OAUTH IN_AUTH CAUTH'''


def p_in_auth(p):
  '''IN_AUTH : FN
  | SN'''


def p_fn(p):
  '''FN : OFIRSTNAME CUERPO3 CFIRSTNAME
  | OFIRSTNAME CUERPO3 CFIRSTNAME IN_AUTH'''


def p_sn(p):
  '''SN : OSURNAME CUERPO3 CSURNAME
  | OSURNAME CUERPO3 CSURNAME IN_AUTH'''


def p_em(p):
  """EMPHASIS : OEMPHASIS CUERPO2 CEMPHASIS"""


def p_com(p):
  """COMMENT : OCOMMENT CUERPO2 CCOMMENT"""


def p_title(p):
  """TITLE : OTITLE IN_TITLE CTITLE"""


def p_in_title(p):
  """IN_TITLE : TEXTO
    | EMPHASIS
    | LINK
    | EMAIL
    | TEXTO IN_TITLE
    | EMPHASIS IN_TITLE
    | LINK IN_TITLE
    | EMAIL IN_TITLE"""


def p_itemized(p):
  """ITEMLIST : OITEMLIST LIST_ITEM CITEMLIST"""


def p_li(p):
  """LIST_ITEM : OLISTITEM CUERPO CLISTITEM
    | OLISTITEM CUERPO CLISTITEM LIST_ITEM"""


def p_imp(p):
  """IMPORTANT : OIMPORTANT TITLE CUERPO CIMPORTANT
    | OIMPORTANT CUERPO CIMPORTANT"""


def p_add(p):
  """ADD : OADD IN_ADD CADD"""


def p_IN_ADD(p):
  """IN_ADD : TEXTO
    | STREET
    | CITY
    | STATE
    | PHONE
    | EMAIL
    | TEXTO IN_ADD
    | STREET IN_ADD
    | CITY IN_ADD
    | STATE IN_ADD
    | PHONE IN_ADD
    | EMAIL IN_ADD
    """


def p_in_holder(p):
  """IN_HOLDER : HOLDER
    | HOLDER IN_HOLDER"""


def p_cr(p):
  """CR : OCR IN_YEAR IN_HOLDER CCR
    | OCR IN_YEAR  CCR"""


def p_in_year(p):
  """IN_YEAR : YEAR
    | YEAR IN_YEAR"""


def p_street(p):
  """STREET : OSTREET CUERPO3 CSTREET"""


def p_city(p):
  """CITY : OCITY CUERPO3 CCITY"""


def p_state(p):
  """STATE : OSTATE CUERPO3 CSTATE"""


def p_phone(p):
  """PHONE : OPHONE CUERPO3 CPHONE"""


def p_email(p):
  """EMAIL : OEMAIL CUERPO3 CEMAIL"""


def p_date(p):
  """DATE : ODATE CUERPO3 CDATE"""


def p_year(p):
  """YEAR : OYEAR CUERPO3 CYEAR"""


def p_holder(p):
  """HOLDER : OHOLDER CUERPO3 CHOLDER"""


def p_section(p):
  """SECTION :  SECT
    | SIMPSECT"""


def p_simpsect(p):
  """SIMPSECT : OSIMPSECT IN_SIMPSECT CSIMPSECT"""


def p_in_simpect(p):
  '''IN_SIMPSECT : INFO CUERPO
  | TITLE CUERPO
  | INFO TITLE CUERPO'''


def p_sect(p):
  """SECT : OSECT IN_ART_SECT CSECT
    | OSECT IN_ART_SECT CSECT SECT"""


def p_paragraph(p):
  """PARAGRAPH : PARA PARAGRAPH
    | SIMPARA PARAGRAPH
    | PARA
    | SIMPARA"""


def p_para(p):
  """PARA : OPARA IN_PARA CPARA"""


def p_in_para(p):
  """IN_PARA :  ITEMLIST
    | IMPORTANT
    | ADD
    | MO
    | TABLE
    | TEXTO
    | EMPHASIS
    | LINK
    | EMAIL
    | AUTH
    | COMMENT
    | TEXTO IN_PARA
    | EMPHASIS IN_PARA
    | LINK IN_PARA
    | EMAIL IN_PARA
    | AUTH IN_PARA
    | COMMENT IN_PARA
    | ITEMLIST IN_PARA
    | IMPORTANT IN_PARA
    | ADD IN_PARA
    | MO IN_PARA
    | TABLE IN_PARA
    """


def p_simpara(p):
  """SIMPARA : OSIMPARA CUERPO2 CSIMPARA"""


def p_abs(p):
  """ABS : OABS TITLE PARAGRAPH CABS
    | OABS PARAGRAPH CABS"""


# TABLAS
def p_table(p):
  """TABLE : OTABLE TABLE_MO TGROUP CTABLE"""


def p_table_mo(p):
  """TABLE_MO : MO TABLE_MO
    | MO"""


def p_tgroup(p):
  """TGROUP : OTGROUP TBODY CTGROUP TGROUP
    | OTGROUP THEAD TBODY CTGROUP TGROUP
    | OTGROUP TFOOT TBODY CTGROUP TGROUP
    | OTGROUP TBODY CTGROUP
    | OTGROUP THEAD TBODY CTGROUP
    | OTGROUP TFOOT TBODY CTGROUP
    | OTGROUP THEAD TFOOT TBODY CTGROUP
    """


def p_thead(p):
  """THEAD : OTHEAD FILA CTHEAD"""


def p_tfoot(p):
  """TFOOT : OTFOOT FILA CTFOOT"""


def p_tbody(p):
  """TBODY : OTBODY FILA CTBODY"""


def p_fila(p):
  """FILA : OROW ENTRY CROW
    | OROW ENTRYTBL CROW
    | OROW ENTRY CROW FILA
    | OROW ENTRYTBL CROW FILA"""


def p_entry(p):
  """ENTRY : OENTRY IN_ENTRY CENTRY"""


def p_in_entry(p):
  """IN_ENTRY : TEXTO
    | ITEMLIST
    | IMPORTANT
    | PARA
    | SIMPARA
    | MO
    | COMMENT
    | ABS
    | TEXTO ENTRY
    | ITEMLIST ENTRY
    | IMPORTANT ENTRY
    | PARA ENTRY
    | SIMPARA ENTRY
    | MO ENTRY
    | COMMENT ENTRY
    | ABS ENTRY"""


def p_entrytbl(p):
  """ENTRYTBL : OENTRYTBL TBODY CENTRYTBL
    | OENTRYTBL THEAD TBODY CENTRYTBL"""


# MULTIMEDIA
def p_link(p):
  """LINK : LINKO """


def p_img(p):
  """IMG : IMGO FREF FREFA"""


def p_vdo(p):
  """VDO : VDOO FREF FREFA"""


def p_mo(p):
  """MO : OMO INFO IN_MO CMO
    | OMO IN_MO CMO"""


def p_in_mo(p):
  """IN_MO : VDOBJECT
    | IMGOBJECT
    | VDOBJECT IN_MO
    | IMGOBJECT IN_MO"""


def p_vdobject(p):
  """VDOBJECT : OVIDOBJ INFO VDO CVIDOBJ
    | OVIDOBJ VDO CVIDOBJ"""


def p_imgobject(p):
  """IMGOBJECT : OIMGOBJ INFO IMG CIMGOBJ
    | OIMGOBJ IMG CIMGOBJ"""


def p_error(p):
  global valido
  valido = False
  if p:
    line, column = find_line_column(p.lexer.lexdata, p)
    print(
      "Error de sintaxis en la entrada: token '{0}', línea {1}, posición {2}".
      format(p.value, line, column))
  else:
    print("Error de sintaxis: entrada incompleta")


def find_line_column(input_text, token):
  last_cr = input_text.rfind('\n', 0, token.lexpos)
  if last_cr < 0:
    last_cr = 0
  line = input_text.count('\n', 0, token.lexpos) + 1
  column = (token.lexpos - last_cr)
  return line, column


# Crear el parser
parser = yacc.yacc()


def run_parser():
  global valido
  filename = input("Ingrese el nombre del archivo de texto: ")
  try:
    with open(filename, 'r', encoding='utf-8') as file:
      data = file.read()
      parser.parse(data)
      if valido:
        print("Análisis sintáctico exitoso.")
      else:
        print("Tu archivo no cumple con las reglas gramaticales.")
  except FileNotFoundError:
    print("Archivo no encontrado.")


# Ejecutar el parser
run_parser()


def generar_archivo_html():
  if valido:
    direccion_archivo = input(
      "Ingresa la dirección donde deseas guardar el archivo: ")
    nombre_archivo = input("Ingresa el nombre del archivo: ")
    ruta_completa = direccion_archivo + "/" + nombre_archivo + ".html"

    contenido_html = """
            <!DOCTYPE html>
            <html>
            <head>
            <title> """ + nombre_archivo + """ </title>
            </head>
            <body>
                """ + html + """
            </body>
            </html>
        """
    try:
      with open(ruta_completa, "w") as archivo:
        archivo.write(contenido_html)
      print("Se ha creado el archivo con éxito en la siguiente ruta:",
            ruta_completa)
    except Exception as e:
      pass


# Llamada a la función

generar_archivo_html()
