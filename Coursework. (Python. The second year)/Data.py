WAYTOASM = 'test.asm'
WAYTOLST = 'test.lst'

Lexemes = {
    'COMMAND': 'STI|POP|INC|CMP|MOV|AND|XOR|JNZ',
    'SYMBOL': '[,\\+\\-\\/\\*:\\]\\[]',
    'DIRECTIVE': 'SEGMENT|ENDS|END',
    'DIR_TYPE': 'DWORD|BYTE|PTR',
    'SEG_REG': 'CS|SS|DS|ES',
	'32_REG': 'EBP|ESI|EDI|EAX|EBX|ECX|EDX',
	'8_REG': 'AL|BL|CL|DL|AH|BH|CH|DH',
	'TYPE': 'DB|DD|DW',
	'HEX': '[0-9][0-9A-F]*H',
    'DEC':'-?[0-9]*D|-?[0-9]*',
    'BIN': '[01]*B'
}
Memmory = {
    'ID': 1,
	#'SEG_REG SYMBOL ID SYMBOL 32-REG SYMBOL DEC SYMBOL': 7,
    'DIR_TYPE DIR_TYPE SEG_REG SYMBOL SYMBOL 32_REG SYMBOL DEC SYMBOL': 7,
    'SEG_REG SYMBOL SYMBOL 32_REG SYMBOL DEC SYMBOL': 4,

    #'SEG_REG SYMBOL ID SYMBOL 32_REG SYMBOL DEC SYMBOL': 6,
    #'DIR_TYPE DIR_TYPE ID SYMBOL 32_REG SYMBOL DEC SYMBOL':6
}

MemAND = {
    'ID': 6,
    #'ID SYMBOL 32_REG SYMBOL DEC SYMBOL': 7,
    #'SEG_REG SYMBOL ID SYMBOL 32_REG SYMBOL DEC SYMBOL': 7,
    #'SEG_REG SYMBOL ID': 6,
    #'DIR_TYPE DIR_TYPE SEG_REG SYMBOL ID': 6,
    #'DIR_TYPE DIR_TYPE ID': 6,
    #'DIR_TYPE DIR_TYPE ID SYMBOL 32_REG SYMBOL DEC SYMBOL': 7,
    #'DIR_TYPE DIR_TYPE SEG_REG SYMBOL ID SYMBOL 32_REG SYMBOL DEC SYMBOL': 7,
    'DIR_TYPE DIR_TYPE SYMBOL 32_REG SYMBOL DEC SYMBOL': 7,
    'SYMBOL 32_REG SYMBOL DEC SYMBOL': 7,
    'SEG_REG SYMBOL SYMBOL 32_REG SYMBOL DEC SYMBOL': 7,
    'DIR_TYPE DIR_TYPE SEG_REG SYMBOL SYMBOL 32_REG SYMBOL DEC SYMBOL': 7,

}

Imm = [
    '[HEX|DEC|BIN] SYMBOL [HEX|DEC|BIN]'
]

Var = {
    'DB':[],
    'DW':[],
    'DD':[]

}
Segments = dict()
stopflag = False
segment_end_flag = False
seg = []

