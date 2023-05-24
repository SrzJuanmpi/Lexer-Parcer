import ply.lex as lex

tokens = (
  'URL',
  'protocol',
  'dom',
  'port',
  'route',
  'fragment',
)

t_protocol = r'[a-z]* '
t_dom = r'[a-zA-Z_.-]+'
t_port = r'[0-9]* '
t_route = r'[a-zA-Z./_-]+'
t_fragment = r'[a-zA-Z_-]+ '


def p_URL(p):
  '''URL: protocol '://' dom ':' port '/' route '#' fragment   
        |protocol '://' dom '/' route '#' fragment
        |protocol '://' dom '/' route 
        |protocol '://' dom ':' port
        | protocol '://' dom'''
  if p[4] == ':':
    p[0] = p[1]
  elif p[6] == '#':
    p[0] = p[1]
  elif p[4] == '/':
    p[0] = p[1]
  elif p[4] == ':':
    p[0] = p[1]
  elif p[2] == '://':
    p[0] = p[1]


t_ignore = " \t"


def t_newline(t):
  r'\n+'
  t.lexer.lineno += t.value.count("\n")


def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)


# Construccion del lexer

lexer = lex.lex()

data = '''
https://regexr.com/
'''

lexer.input(data)

# Tokenize
while True:
  tok = lexer.token()
  if not tok:
    break  # No more input
  print(tok.type, tok.value, tok.lineno, tok.lexpos)
