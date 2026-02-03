grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// TODO: Define grammar rules here
// ###### Parser Rules ######
program: (structdecl | funcdecl)+ EOF;
// ###### Struct Declaration ######
structdecl: STRUCT ID LBRACE members* RBRACE;
members: type ID SEMI;
type: INT_KW | FLOAT_KW | STRING_KW | ID ;
// ###### Function Declaration ######
funcdecl: returntype ID LPAREN listparam? RPAREN LBRACE stmt+ RBRACE;
returntype: type | VOID | ;
param: paramtype ID ;
paramtype: INT_KW | FLOAT_KW | STRING_KW | ID ;  // không có AUTO
listparam: param listpr;
listpr: COMMA param listpr | ;
// ###### Statements ######
stmt: vardecl SEMI
     | assignstmt SEMI
     | condstmt 
     | switchstmt
     | whilestmt 
     | forstmt 
     | returnstmt SEMI
     | exprstmt SEMI
     | blockstmt 
     | breakstmt SEMI
     | continuestmt SEMI ;
assignstmt: ID ASSIGN expr 
            | ID DOT ID ASSIGN expr ;
condstmt: IF LPAREN expr RPAREN stmt (ELSE stmt)? ;
whilestmt: WHILE LPAREN expr RPAREN stmt ;
forstmt: FOR LPAREN init? SEMI condition? SEMI update? RPAREN stmt ;
init: vardecl | assignstmt;
condition: expr;
update: assignstmt | expr;  // hoặc cụ thể hơn

switchstmt: SWITCH LPAREN expr RPAREN LBRACE case* RBRACE ;
case: CASE expr COLON stmt* 
    | DEFAULT COLON stmt* ;
returnstmt: RETURN expr? ;
exprstmt: expr ;
blockstmt: LBRACE stmt+ RBRACE ;
breakstmt: BREAK ;
continuestmt: CONTINUE ;
// ###### Variable Declaration ######
vardecl: type ID (ASSIGN expr)? ;

// ###### Expressions ######
// ===== EXPRESSIONS =====
// Level 1: Logical OR (lowest precedence)
expr: logicalOR;

logicalOR: logicalAND ( OR logicalAND)*;

// Level 2: Logical AND
logicalAND: equality (AND equality)*;

// Level 3: Equality
equality: relational ((EQ | NEQ) relational)*;

// Level 4: Relational
relational: additive ((LT | LE | GT | GE) additive)*;

// Level 5: Additive
additive: multiplicative ((PLUS | MINUS) multiplicative)*;

// Level 6: Multiplicative
multiplicative: unary ((MUL | DIV | MOD) unary)*;
// Level 7: Unary
unary: (NOT | MINUS | PLUS | INC | DEC) unary
     | postfix;

// Level 8: Postfix (highest precedence)
postfix: primary postfixOp*;
postfixOp: INC | DEC | DOT ID | LPAREN arglist? RPAREN;

// Primary expressions
primary: INT
       | FLOAT
       | STRING
       | ID
       | LPAREN expr RPAREN
       | LBRACE arglist? RBRACE;  // struct literal

// Function call arguments
arglist: expr (COMMA expr)*;

// ##### LEXER RULES #####

// Keywords (phải đặt trước ID)
AUTO: 'auto';
BREAK: 'break';
CASE: 'case';
CONTINUE: 'continue';
DEFAULT: 'default';
ELSE: 'else';
FLOAT_KW: 'float';
FOR: 'for';
IF: 'if';
INT_KW: 'int';
RETURN: 'return';
STRING_KW: 'string';
STRUCT: 'struct';
SWITCH: 'switch';
VOID: 'void';
WHILE: 'while';

// Operators
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
AND: '&&';
OR: '||';
NOT: '!';
INC: '++';
DEC: '--';
ASSIGN: '=';
DOT: '.';

// Separators
LBRACE: '{';
RBRACE: '}';
LPAREN: '(';
RPAREN: ')';
SEMI: ';';
COMMA: ',';
COLON: ':';
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

// ##### LITERALS #####

// Integer literal: 1+ digits
INT: [0-9]+;

// Float literal: 3 dạng
FLOAT: [0-9]+ '.' [0-9]* EXPONENT?   // 1., 1.5, 1.5e2
     | '.' [0-9]+ EXPONENT?           // .5, .5e2
     | [0-9]+ EXPONENT;               // 1e4, 2E-3

fragment EXPONENT: [eE] [+-]? [0-9]+;

// ##### STRING LITERAL #####
// Valid string
STRING: '"' (STR_CHAR | ESC_SEQ)* '"' {
self.text = self.text[1:-1]
};

fragment STR_CHAR: ~["\\\r\n];
fragment ESC_SEQ: '\\' [bfrnt"\\];

// ##### IDENTIFIER #####
ID: [a-zA-Z_][a-zA-Z0-9_]*;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs

ERROR_CHAR: .;
// ##### STRING ERRORS #####
// ILLEGAL_ESCAPE: backslash + invalid character
ILLEGAL_ESCAPE: '"' (STR_CHAR | ESC_SEQ)* '\\' ~[bfrnt"\\\r\n] {
self.text = self.text[1:]
};
// UNCLOSE_STRING: string not closed before newline/CR/EOF
UNCLOSE_STRING: '"' (STR_CHAR | ESC_SEQ)* ('\r' | '\n' | EOF) {
self.text = self.text[1:]
};