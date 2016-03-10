
MAKE_WHOLE_DOCUMENTS = False

DOC_PREAMBLE = '''
\documentclass{article}
\usepackage{siunitx}
\usepackage[sfdefault]{roboto}
\usepackage[T1]{fontenc}
\usepackage{pifont}
\usepackage{rotating}
\\begin{document}
'''
PREAMBLE = '''
\\begin{table}[p]
  \centering
'''

END_TAB = '''
  \end{tabular}
  '''
END = '''
  \caption{%s}
  \label{tab:myfirsttable}
\end{table}
'''
DOC_END = '''
\end{document}
'''

SPECIALS = {'\\': "\\slash",
            '^': "hat",
            chr(127): "del",
            ' ': "spc",
            '~': "tdl"}
def latex_escape_chr(ch):
	if ch in SPECIALS.keys():
		return SPECIALS[ch]
	if ch in ['$', '%', '\\', '#', '&', '{', '}', '^', '_']:
		return '\\%s' % ch
	return ch

def write_out_ascii_chart(filename):
  out = file(filename, 'w')
  if MAKE_WHOLE_DOCUMENTS:
  	out.write(DOC_PREAMBLE)
  out.write(PREAMBLE)

  cols = 8
  out.write('\\begin{tabular}{ l' + ('c ' * (cols - 1)) + ' }')
  matrix = {}
  for a in range(0, 20):
  	matrix[a] = [''] * cols

  for c in range(32,128):
  	matrix[3 + c % 16][int(c / 16)] = chr(c)

  matrix[2][0] = 'hex 1st digit \\ding{165}'
  matrix[3][0] = 'hex 2nd digit \\ding{116}'
  for c in range(0, 16):
  #	rep = '00' + filter(lambda x: x != 'b', bin(c))
  #	for bit in range(1, 5):
  #		matrix[3 + c][6-bit] = rep[-bit]
  	matrix[3 + c][1] = hex(c)[-1]

  for c in range(2, 8):
  	rep = '00' + filter(lambda x: x != 'b', bin(c))
  	
  	#matrix[0][6 + c] = rep[len(rep) - 3] + '--'
  	#matrix[1][6 + c] = '-' + rep[len(rep) - 2] + '-'
  	#matrix[2][6 + c] = str(c) + '-' + rep[len(rep) - 1]
  	matrix[2][c] = str(c)

  for y in range(0, 20):
  	row = matrix[y]
  	prow = ''
  	for i, ch in enumerate(row):
  		prow += latex_escape_chr(ch)
  		if i < len(row) - 1:
  			prow += ' & '
  		else:
  			prow += ' \\\\'
  	out.write(prow + '\n')
  	if (y == 2):
  		out.write('\hline\n')
  out.write(END_TAB)
  out.write(END % 'ASCII Printable Characters')
  if MAKE_WHOLE_DOCUMENTS:
  	out.write(DOC_END)
  out.close()

def write_out_hex_chart(filename):
  out = file(filename, 'w')
  if MAKE_WHOLE_DOCUMENTS:
  	out.write(DOC_PREAMBLE)
  out.write(PREAMBLE)

  cols = 19
  out.write('\\begin{sideways}\\begin{tabular}{ l' + ('c ' * (cols - 1)) + ' }')
  matrix = {}
  for a in range(0, 20):
  	matrix[a] = [''] * cols

  for c in range(0,256):
  	matrix[3 + c % 16][2 + int(c / 16)] = c

  matrix[2][0] = 'hex 1st digit \\ding{165}'
  matrix[3][0] = 'hex 2nd digit \\ding{116}'
  for c in range(0, 16):
  #	rep = '00' + filter(lambda x: x != 'b', bin(c))
  #	for bit in range(1, 5):
  #		matrix[3 + c][6-bit] = rep[-bit]
  	matrix[3 + c][1] = '\\textit{' + hex(c)[-1] + '}'

  for c in range(0, 16):
  	rep = '00' + filter(lambda x: x != 'b', bin(c))
  	
  	#matrix[0][6 + c] = rep[len(rep) - 3] + '--'
  	#matrix[1][6 + c] = '-' + rep[len(rep) - 2] + '-'
  	#matrix[2][6 + c] = str(c) + '-' + rep[len(rep) - 1]
  	matrix[2][c+2] = '\\textit{' + hex(c)[-1] + '}'

  for y in range(0, 20):
  	row = matrix[y]
  	prow = ''
  	for i, ch in enumerate(row):
  		prow += str(ch)
  		if i < len(row) - 1:
  			prow += ' & '
  		else:
  			prow += ' \\\\'
  	out.write(prow + '\n')
  	if (y == 2):
  		out.write('\hline\n')
  out.write(END_TAB)
  out.write('\\end{sideways}')
  out.write(END % 'hex -> decimal')
  if MAKE_WHOLE_DOCUMENTS:
  	out.write(DOC_END)
  out.close()

def main():
	write_out_ascii_chart('ascii.tex')
	write_out_hex_chart('hex.tex')

if __name__ == "__main__":
  main()