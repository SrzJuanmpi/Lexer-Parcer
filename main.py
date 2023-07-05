# Librerías
import ply.lex as lex
import ply.yacc as yacc
import sys
import os
from PyQt5.QtWidgets import (
  QApplication,
  QMainWindow,
  QTextEdit,
  QPushButton,
  QFileDialog,
  QHBoxLayout,
  QWidget,
  QMessageBox,
)
from PyQt5.QtGui import QColor, QPalette, QLinearGradient, QFont, QFontDatabase
from PyQt5.QtCore import Qt, pyqtSignal

# Variables
valido = True
html = ""
error_messages = []

tokens = (
  "TEXTO",
  # Tokens para cabecera y article
  "DOC1",
  "DOC2",
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
  "URL",
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

aux_entry = 1
title_section = False
title_article = False
title_info = False
es_imagen = False
es_video = False


def t_DOC1(t):
  r"<\!DOCTYPE"
  return t


def t_DOC2(t):
  r"article>"
  global html
  html += "<!DOCTYPE html>"
  return t


def t_OARTICLE(t):
  r"<article>"
  global html
  global title_article
  title_article = True
  html += "<html lang='es'> <head> <meta charset='UTF-8'> <style> .info { background: rgb(9, 184, 9); color: white; font-size: 8pt; width: 420px; margin: 0px; margin-bottom: auto;}.important {background: rgb(237, 27, 24);color: white;width: 420px;margin: 0px; margin-bottom: auto;} </style> </head> <body>"
  return t


def t_CARTICLE(t):
  r"</article>"
  global html
  html += "</body></html>"
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
  global title_info
  title_info = True
  html += "<div class='info'>"
  return t


def t_CINFO(t):
  r"</info>"
  global html
  html += "</div>"
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
  global html
  html += "<table>"
  return t


def t_CTABLE(t):
  r"</informaltable>"
  global html
  html += "</table>"
  return t


def t_OTGROUP(t):
  r"<tgroup>"
  return t


def t_CTGROUP(t):
  r"</tgroup>"
  return t


def t_OTHEAD(t):
  r"<thead>"
  global html
  html += "<thead>"
  return t


def t_CTHEAD(t):
  r"</thead>"
  global html
  html += "</thead>"
  return t


def t_OTFOOT(t):
  r"<tfoot>"
  global html
  html += "<tfoot>"
  return t


def t_CTFOOT(t):
  r"</tfoot>"
  global html
  html += "</tfoot>"
  return t


def t_OTBODY(t):
  r"<tbody>"
  global html
  html += "<tbody>"
  return t


def t_CTBODY(t):
  r"</tbody>"
  global html
  html += "</tbody>"
  return t


def t_OROW(t):
  r"<row>"
  global html
  html += "<tr>"
  return t


def t_CROW(t):
  r"</row>"
  global aux_entry
  global html
  # Cuento las filas de la tabla, para la 1er Fila se tendrá un contenido resaltado, las demas ya no...
  aux_entry += 1
  html += "</tr>"
  return t


def t_OENTRY(t):
  r"<entry>"
  global aux_entry
  global html
  if aux_entry == 1:
    html += "<th>"
  else:
    html += "<td>"
  return t


def t_CENTRY(t):
  r"</entry>"
  global aux_entry
  global html
  if aux_entry == 1:
    html += "</th>"
  else:
    html += "</td>"
  return t


def t_OENTRYTBL(t):
  r"<entrytbl>"
  global html
  html += "<table>"
  return t


def t_CENTRYTBL(t):
  r"</entrytbl>"
  global html
  html += "</table>"
  return t


def t_LINKO(t):
  r"<link"
  global html
  html += "<a"
  return t


def t_VREF(t):
  r"xlink:href="
  global html
  html += " href ="
  return t


def t_IMGO(t):
  r"<imagedata"
  global html
  global es_imagen
  es_imagen = True
  html += "<a"
  return t


def t_VDOO(t):
  r"<videodata"
  global html
  global es_video
  es_video = True
  return t


def t_FREF(t):
  r"fileref="
  global html
  if es_imagen:
    html += " fileref="
  return t


def t_URL(t):
  r"(\"(https|http|ftps|ftp)\://((\.|[A-Z]|[a-z])+(?!-)([ÁÉÍÓÚáéíóú\-\w]+|[0-9]+|:([0-9])*)(?<!-))(\.|[A-Z]|[a-z])+(\/[A-Za-z0-9._/]+)*(\#(\w.(?!\.))+)?) \"/>"
  global html
  html += t.value[:-2] + 'target="_blank">¡Haz click aqui!</a>'
  return t


def t_FREFA(t):
  r"([^<>]+)/>"
  global html
  global es_imagen
  global es_video
  if es_imagen:
    html += t.value[:-2] + "><img src=" + t.value[:-2] + "></a>"
    es_imagen = False
  else:
    html += ('<iframe width="560" height="315" src=' + t.value +
             'frameborder="0" allowfullscreen></iframe>')
    es_video = False
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
  global html
  global title_section
  global title_article
  global title_info

  if title_info:
    html += "<h3>"
  elif title_section:
    html += "<h2>"
  elif title_article:
    html += "<h1>"
  return t


def t_CTITLE(t):
  r"</title>"
  global html
  global title_section
  global title_article
  global title_info

  if title_info:
    html += "</h3>"
    title_info = False
  elif title_section:
    html += "</h2>"
    title_section = False
  elif title_article:
    html += "</h1>"
    title_article = False
  return t


def t_OIMPORTANT(t):
  r"<important>"
  global html
  global title_info
  title_info = True
  html += "<div class = 'important' >"
  return t


def t_CIMPORTANT(t):
  r"</important>"
  global html
  html += "</div>"
  return t


def t_OITEMLIST(t):
  r"<itemizedlist>"
  global html
  html += "<ul>"
  return t


def t_CITEMLIST(t):
  r"</itemizedlist>"
  global html
  html += "</ul>"
  return t


def t_OLISTITEM(t):
  r"<listitem>"
  global html
  html += "<li>"
  return t


def t_CLISTITEM(t):
  r"</listitem>"
  global html
  html += "</li>"
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
  global title_section
  title_section = True
  return t


def t_CSIMPSECT(t):
  r"</simplesect>"
  return t


def t_OSECT(t):
  r"<section>"
  global title_section
  title_section = True
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
  global title_info
  title_info = True
  return t


def t_CABS(t):
  r"</abstract>"
  return t


def t_TEXTO(t):
  r"([^<>]+)"
  global html
  html += t.value
  return t


t_ignore = " \t" " \n"


def t_error(t):
  global valido
  valido = False
  linea, columna = nro_linea_columna2(t.lexer.lexdata, t)
  error_message = f"Error léxico: Caracter inesperado '{t.value[0]}' en línea {linea}, posición {columna}"
  error_messages.append(error_message)
  t.lexer.skip(1)


def nro_linea_columna2(input_text, token):
  last_cr = input_text.rfind("\n", 0, token.lexpos)
  if last_cr < 0:
    last_cr = 0
  line = input_text.count("\n", 0, token.lexpos) + 1
  column = token.lexpos - last_cr
  return line, column


# PRODUCCIONES


def p_E(p):
  """E : DOC XMLPROLOG ARTICLE
    | ARTICLE
    | XMLPROLOG ARTICLE
    | DOC ARTICLE"""


def p_DOC(p):
  """DOC : DOC1 DOC2"""


def p_ARTICLE(p):
  """ARTICLE : OARTICLE IN_ART_SECT CARTICLE"""


def p_XMLVERSION(p):
  """XMLPROLOG : XML VERSION ENCODING"""


def p_IN_ART_SECT(p):
  """IN_ART_SECT : INFO TITLE CUERPO SECTION
    | INFO CUERPO
    | TITLE CUERPO
    | INFO TITLE CUERPO
    | INFO CUERPO SECTION
    | TITLE CUERPO SECTION
    | CUERPO
    | CUERPO SECTION"""


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
  """AUTH : OAUTH IN_AUTH CAUTH"""


def p_in_auth(p):
  """IN_AUTH : FN
    | SN"""


def p_fn(p):
  """FN : OFIRSTNAME CUERPO3 CFIRSTNAME
    | OFIRSTNAME CUERPO3 CFIRSTNAME IN_AUTH"""


def p_sn(p):
  """SN : OSURNAME CUERPO3 CSURNAME
    | OSURNAME CUERPO3 CSURNAME IN_AUTH"""


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


def p_cuerpo3(p):
  """CUERPO3 : TEXTO
    | EMPHASIS
    | LINK
    | COMMENT
    | TEXTO CUERPO3
    | EMPHASIS CUERPO3
    | LINK CUERPO3
    | COMMENT CUERPO3"""


def p_section(p):
  """SECTION :  SECT
    | SIMPSECT"""


def p_simpsect(p):
  """SIMPSECT : OSIMPSECT IN_SIMPSECT CSIMPSECT"""


def p_in_simpect(p):
  """IN_SIMPSECT : INFO CUERPO
    | TITLE CUERPO
    | INFO TITLE CUERPO"""


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
  """TABLE : OTABLE TABLE_MO CTABLE
    | OTABLE TGROUP CTABLE"""


def p_table_mo(p):
  """TABLE_MO : MO TABLE_MO
    | MO"""


def p_tgroup(p):
  """TGROUP : OTGROUP TBODY CTGROUP TGROUP
    | OTGROUP THEAD TBODY CTGROUP TGROUP
    | OTGROUP TFOOT TBODY CTGROUP TGROUP
    | OTGROUP THEAD TFOOT TBODY CTGROUP TGROUP
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
  """ENTRY : OENTRY IN_ENTRY CENTRY
    | OENTRY IN_ENTRY CENTRY ENTRY"""


def p_in_entry(p):
  """IN_ENTRY : TEXTO
    | ITEMLIST
    | IMPORTANT
    | PARA
    | SIMPARA
    | MO
    | COMMENT
    | ABS
    | TEXTO IN_ENTRY
    | ITEMLIST IN_ENTRY
    | IMPORTANT IN_ENTRY
    | PARA IN_ENTRY
    | SIMPARA IN_ENTRY
    | MO IN_ENTRY
    | COMMENT IN_ENTRY
    | ABS IN_ENTRY"""


def p_entrytbl(p):
  """ENTRYTBL : OENTRYTBL TBODY CENTRYTBL
    | OENTRYTBL THEAD TBODY CENTRYTBL
    | OENTRYTBL TBODY CENTRYTBL ENTRYTBL
    | OENTRYTBL THEAD TBODY CENTRYTBL ENTRYTBL"""


# MULTIMEDIA
def p_link(p):
  """LINK : LINKO VREF URL"""


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
  linea, columna = nro_linea_columna(p.lexer.lexdata, p)
  if p:
    error_message = f"Error de sintaxis: Token inesperado '{p.value}' en línea {linea}, posición {columna}"
    error_messages.append(
      error_message)  # Manda a la interface el mensaje de error
  else:
    error_message = "Error de sintaxis: Entrada incompleta"
    error_messages.append(
      error_message)  # Manda a la interface el mensaje de error


def nro_linea_columna(input_text,
                      token):  # Controla el número de línea y columna
  last_cr = input_text.rfind("\n", 0, token.lexpos)
  if last_cr < 0:
    last_cr = 0
  linea = input_text.count("\n", 0, token.lexpos) + 1
  columna = token.lexpos - last_cr
  return linea, columna


class XMLCompiler(QMainWindow):

  def __init__(self):
    super().__init__()
    # Ventana Principal
    self.setWindowTitle("Interprete de XML Docbook Article a HTML")
    self.setGeometry(100, 100, 1280, 800)

    # Fondo de pantalla con gradiente de verde
    self.set_background_gradient(QColor(4, 68, 1), QColor(13, 177, 0),
                                 QColor(92, 241, 76))

    # Widget principal
    central_widget = QWidget(self)
    self.setCentralWidget(central_widget)

    # Diseño horizontal para los cuadros de texto
    layout = QHBoxLayout(central_widget)

    # Cuadro de texto principal para introducir el código XML
    self.text_edit = QTextEdit(self)
    self.text_edit.setGeometry(10, 10, 800, 780)
    self.text_edit.setPlaceholderText("Escriba su código aquí...")
    self.text_edit.setStyleSheet("background-color: #B6D8A8;font-size: 10pt;")

    # Cuadro de texto para errores
    self.error_text_edit = QTextEdit(self)
    self.error_text_edit.setGeometry(860, 400, 350, 350)
    self.error_text_edit.setStyleSheet(
      "background-color: white; font-size: 10pt;")
    self.error_text_edit.setReadOnly(True)

    # Botón para cargar un archivo de texto externo
    self.load_button = QPushButton("Cargar Archivo", self)
    self.load_button.setGeometry(860, 100, 350, 60)
    self.load_button.setStyleSheet(
      "background-color: #A2C8A2; color: black; border-radius: 15px;")
    self.load_button.setFont(QFont("Arial", 14, QFont.Bold))

    # Botón para compilar el texto
    self.compile_button = QPushButton("Traducir", self)
    self.compile_button.setGeometry(860, 200, 350, 60)
    self.compile_button.setStyleSheet(
      "background-color: #A2C8A2; color: black; border-radius: 15px;")
    self.compile_button.setFont(QFont("Arial", 14, QFont.Bold))

    # Botón para salir de la aplicación
    self.exit_button = QPushButton("Salir", self)
    self.exit_button.setGeometry(860, 300, 350, 60)
    self.exit_button.setStyleSheet(
      "background-color: #A2C8A2; color: black; border-radius: 15px;")
    self.exit_button.setFont(QFont("Arial", 14, QFont.Bold))

    # Conectar los botones a sus funciones correspondientes
    self.load_button.clicked.connect(self.load_file)
    self.compile_button.clicked.connect(self.compile_text)
    self.exit_button.clicked.connect(self.close)

  # La magia de la interface
  def compile_text(self):
    global error_messages
    error_messages = []  # Si hubo un msj anterior, lo borramos

    # Obtener el código XML del cuadro de texto principal
    xml = self.text_edit.toPlainText()

    # Reiniciar la variable global 'valido', sino el próximo código puede fallar
    global valido
    valido = True

    # Creamos al lexer y al parser
    lexer = lex.lex()
    parser = yacc.yacc()

    # Ejecutar el análisis léxico y sintáctico
    lexer.input(xml)
    parser.parse(
      xml, lexer=lexer
    )  # Invocamos al parser, que a la vez ya invoca el lexer, todo intergrado

    # Mostrar los mensajes de error en el cuadro de texto de errores
    if (
        not valido
    ):  # valido es falso cuando hay un error, por lo tanto el not lo vuelve verdadero y entra al 1er bloque del condicional
      self.error_text_edit.setPlainText("\n".join(error_messages))
    else:  # Si está todo OK viene acá
      self.error_text_edit.setPlainText(
        "Compilación exitosa. No se encontraron errores.")

    # Guardar el contenido en un archivo HTML
    arch_resultado = "resultado.html"
    with open(arch_resultado, "w") as file:
      file.write(html)
    ubi_arch_resultado = os.path.abspath(arch_resultado)
    QMessageBox.information(
      self,
      "Archivo generado",
      f"Archivo HTML generado:\n{ubi_arch_resultado}",
    )

  # Estilo del fondo

  def set_background_gradient(self, color1, color2, color3):
    palette = self.palette()
    gradient = QLinearGradient(0, 0, 0, self.height())
    gradient.setColorAt(0, color1)
    gradient.setColorAt(0.5, color2)
    gradient.setColorAt(1, color3)
    palette.setBrush(QPalette.Window, gradient)
    self.setPalette(palette)

  # Carga del archivo
  def load_file(self):
    file_dialog = QFileDialog(self)
    file_dialog.setWindowTitle("Cargar Archivo")
    file_dialog.setFileMode(QFileDialog.ExistingFile)
    file_dialog.setNameFilter("Archivos de Texto (*.txt *.xml)")
    file_dialog.setDefaultSuffix("txt")

    if file_dialog.exec_():
      file_path = file_dialog.selectedFiles()[0]
      with open(file_path, "r") as file:
        self.text_edit.setPlainText(file.read())


# Crear interface y sus funcionalidades
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = XMLCompiler()
  window.show()
  sys.exit(app.exec_())
