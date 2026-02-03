# Generated from c:/Users/Admin/tyc-compiler/src/grammar/TyC.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,51,365,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,1,0,4,0,79,8,0,
        11,0,12,0,80,1,0,1,0,1,1,1,1,1,1,1,1,5,1,89,8,1,10,1,12,1,92,9,1,
        1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,3,4,106,8,4,1,4,
        1,4,1,4,4,4,111,8,4,11,4,12,4,112,1,4,1,4,1,5,1,5,1,5,3,5,120,8,
        5,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,135,8,
        9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,160,8,
        10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,170,8,11,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,3,12,179,8,12,1,13,1,13,1,13,1,13,1,
        13,1,13,1,14,1,14,1,14,3,14,190,8,14,1,14,1,14,3,14,194,8,14,1,14,
        1,14,3,14,198,8,14,1,14,1,14,1,14,1,15,1,15,3,15,205,8,15,1,16,1,
        16,1,17,1,17,3,17,211,8,17,1,18,1,18,1,18,1,18,1,18,1,18,5,18,219,
        8,18,10,18,12,18,222,9,18,1,18,1,18,1,19,1,19,1,19,1,19,5,19,230,
        8,19,10,19,12,19,233,9,19,1,19,1,19,1,19,5,19,238,8,19,10,19,12,
        19,241,9,19,3,19,243,8,19,1,20,1,20,3,20,247,8,20,1,21,1,21,1,22,
        1,22,4,22,253,8,22,11,22,12,22,254,1,22,1,22,1,23,1,23,1,24,1,24,
        1,25,1,25,1,25,1,25,3,25,267,8,25,1,26,1,26,1,27,1,27,1,27,5,27,
        274,8,27,10,27,12,27,277,9,27,1,28,1,28,1,28,5,28,282,8,28,10,28,
        12,28,285,9,28,1,29,1,29,1,29,5,29,290,8,29,10,29,12,29,293,9,29,
        1,30,1,30,1,30,5,30,298,8,30,10,30,12,30,301,9,30,1,31,1,31,1,31,
        5,31,306,8,31,10,31,12,31,309,9,31,1,32,1,32,1,32,5,32,314,8,32,
        10,32,12,32,317,9,32,1,33,1,33,1,33,3,33,322,8,33,1,34,1,34,5,34,
        326,8,34,10,34,12,34,329,9,34,1,35,1,35,1,35,1,35,1,35,1,35,3,35,
        337,8,35,1,35,3,35,340,8,35,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,
        36,1,36,1,36,3,36,352,8,36,1,36,3,36,355,8,36,1,37,1,37,1,37,5,37,
        360,8,37,10,37,12,37,363,9,37,1,37,0,0,38,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,0,6,4,0,7,7,10,10,12,12,47,47,1,0,22,23,1,0,
        24,27,1,0,17,18,1,0,19,21,2,0,17,18,30,32,377,0,78,1,0,0,0,2,84,
        1,0,0,0,4,95,1,0,0,0,6,99,1,0,0,0,8,101,1,0,0,0,10,119,1,0,0,0,12,
        121,1,0,0,0,14,124,1,0,0,0,16,126,1,0,0,0,18,134,1,0,0,0,20,159,
        1,0,0,0,22,169,1,0,0,0,24,171,1,0,0,0,26,180,1,0,0,0,28,186,1,0,
        0,0,30,204,1,0,0,0,32,206,1,0,0,0,34,210,1,0,0,0,36,212,1,0,0,0,
        38,242,1,0,0,0,40,244,1,0,0,0,42,248,1,0,0,0,44,250,1,0,0,0,46,258,
        1,0,0,0,48,260,1,0,0,0,50,262,1,0,0,0,52,268,1,0,0,0,54,270,1,0,
        0,0,56,278,1,0,0,0,58,286,1,0,0,0,60,294,1,0,0,0,62,302,1,0,0,0,
        64,310,1,0,0,0,66,321,1,0,0,0,68,323,1,0,0,0,70,339,1,0,0,0,72,354,
        1,0,0,0,74,356,1,0,0,0,76,79,3,2,1,0,77,79,3,8,4,0,78,76,1,0,0,0,
        78,77,1,0,0,0,79,80,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,82,1,
        0,0,0,82,83,5,0,0,1,83,1,1,0,0,0,84,85,5,13,0,0,85,86,5,47,0,0,86,
        90,5,35,0,0,87,89,3,4,2,0,88,87,1,0,0,0,89,92,1,0,0,0,90,88,1,0,
        0,0,90,91,1,0,0,0,91,93,1,0,0,0,92,90,1,0,0,0,93,94,5,36,0,0,94,
        3,1,0,0,0,95,96,3,6,3,0,96,97,5,47,0,0,97,98,5,39,0,0,98,5,1,0,0,
        0,99,100,7,0,0,0,100,7,1,0,0,0,101,102,3,10,5,0,102,103,5,47,0,0,
        103,105,5,37,0,0,104,106,3,16,8,0,105,104,1,0,0,0,105,106,1,0,0,
        0,106,107,1,0,0,0,107,108,5,38,0,0,108,110,5,35,0,0,109,111,3,20,
        10,0,110,109,1,0,0,0,111,112,1,0,0,0,112,110,1,0,0,0,112,113,1,0,
        0,0,113,114,1,0,0,0,114,115,5,36,0,0,115,9,1,0,0,0,116,120,3,6,3,
        0,117,120,5,15,0,0,118,120,1,0,0,0,119,116,1,0,0,0,119,117,1,0,0,
        0,119,118,1,0,0,0,120,11,1,0,0,0,121,122,3,14,7,0,122,123,5,47,0,
        0,123,13,1,0,0,0,124,125,7,0,0,0,125,15,1,0,0,0,126,127,3,12,6,0,
        127,128,3,18,9,0,128,17,1,0,0,0,129,130,5,40,0,0,130,131,3,12,6,
        0,131,132,3,18,9,0,132,135,1,0,0,0,133,135,1,0,0,0,134,129,1,0,0,
        0,134,133,1,0,0,0,135,19,1,0,0,0,136,137,3,50,25,0,137,138,5,39,
        0,0,138,160,1,0,0,0,139,140,3,22,11,0,140,141,5,39,0,0,141,160,1,
        0,0,0,142,160,3,24,12,0,143,160,3,36,18,0,144,160,3,26,13,0,145,
        160,3,28,14,0,146,147,3,40,20,0,147,148,5,39,0,0,148,160,1,0,0,0,
        149,150,3,42,21,0,150,151,5,39,0,0,151,160,1,0,0,0,152,160,3,44,
        22,0,153,154,3,46,23,0,154,155,5,39,0,0,155,160,1,0,0,0,156,157,
        3,48,24,0,157,158,5,39,0,0,158,160,1,0,0,0,159,136,1,0,0,0,159,139,
        1,0,0,0,159,142,1,0,0,0,159,143,1,0,0,0,159,144,1,0,0,0,159,145,
        1,0,0,0,159,146,1,0,0,0,159,149,1,0,0,0,159,152,1,0,0,0,159,153,
        1,0,0,0,159,156,1,0,0,0,160,21,1,0,0,0,161,162,5,47,0,0,162,163,
        5,33,0,0,163,170,3,52,26,0,164,165,5,47,0,0,165,166,5,34,0,0,166,
        167,5,47,0,0,167,168,5,33,0,0,168,170,3,52,26,0,169,161,1,0,0,0,
        169,164,1,0,0,0,170,23,1,0,0,0,171,172,5,9,0,0,172,173,5,37,0,0,
        173,174,3,52,26,0,174,175,5,38,0,0,175,178,3,20,10,0,176,177,5,6,
        0,0,177,179,3,20,10,0,178,176,1,0,0,0,178,179,1,0,0,0,179,25,1,0,
        0,0,180,181,5,16,0,0,181,182,5,37,0,0,182,183,3,52,26,0,183,184,
        5,38,0,0,184,185,3,20,10,0,185,27,1,0,0,0,186,187,5,8,0,0,187,189,
        5,37,0,0,188,190,3,30,15,0,189,188,1,0,0,0,189,190,1,0,0,0,190,191,
        1,0,0,0,191,193,5,39,0,0,192,194,3,32,16,0,193,192,1,0,0,0,193,194,
        1,0,0,0,194,195,1,0,0,0,195,197,5,39,0,0,196,198,3,34,17,0,197,196,
        1,0,0,0,197,198,1,0,0,0,198,199,1,0,0,0,199,200,5,38,0,0,200,201,
        3,20,10,0,201,29,1,0,0,0,202,205,3,50,25,0,203,205,3,22,11,0,204,
        202,1,0,0,0,204,203,1,0,0,0,205,31,1,0,0,0,206,207,3,52,26,0,207,
        33,1,0,0,0,208,211,3,22,11,0,209,211,3,52,26,0,210,208,1,0,0,0,210,
        209,1,0,0,0,211,35,1,0,0,0,212,213,5,14,0,0,213,214,5,37,0,0,214,
        215,3,52,26,0,215,216,5,38,0,0,216,220,5,35,0,0,217,219,3,38,19,
        0,218,217,1,0,0,0,219,222,1,0,0,0,220,218,1,0,0,0,220,221,1,0,0,
        0,221,223,1,0,0,0,222,220,1,0,0,0,223,224,5,36,0,0,224,37,1,0,0,
        0,225,226,5,3,0,0,226,227,3,52,26,0,227,231,5,41,0,0,228,230,3,20,
        10,0,229,228,1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,0,231,232,1,0,
        0,0,232,243,1,0,0,0,233,231,1,0,0,0,234,235,5,5,0,0,235,239,5,41,
        0,0,236,238,3,20,10,0,237,236,1,0,0,0,238,241,1,0,0,0,239,237,1,
        0,0,0,239,240,1,0,0,0,240,243,1,0,0,0,241,239,1,0,0,0,242,225,1,
        0,0,0,242,234,1,0,0,0,243,39,1,0,0,0,244,246,5,11,0,0,245,247,3,
        52,26,0,246,245,1,0,0,0,246,247,1,0,0,0,247,41,1,0,0,0,248,249,3,
        52,26,0,249,43,1,0,0,0,250,252,5,35,0,0,251,253,3,20,10,0,252,251,
        1,0,0,0,253,254,1,0,0,0,254,252,1,0,0,0,254,255,1,0,0,0,255,256,
        1,0,0,0,256,257,5,36,0,0,257,45,1,0,0,0,258,259,5,2,0,0,259,47,1,
        0,0,0,260,261,5,4,0,0,261,49,1,0,0,0,262,263,3,6,3,0,263,266,5,47,
        0,0,264,265,5,33,0,0,265,267,3,52,26,0,266,264,1,0,0,0,266,267,1,
        0,0,0,267,51,1,0,0,0,268,269,3,54,27,0,269,53,1,0,0,0,270,275,3,
        56,28,0,271,272,5,29,0,0,272,274,3,56,28,0,273,271,1,0,0,0,274,277,
        1,0,0,0,275,273,1,0,0,0,275,276,1,0,0,0,276,55,1,0,0,0,277,275,1,
        0,0,0,278,283,3,58,29,0,279,280,5,28,0,0,280,282,3,58,29,0,281,279,
        1,0,0,0,282,285,1,0,0,0,283,281,1,0,0,0,283,284,1,0,0,0,284,57,1,
        0,0,0,285,283,1,0,0,0,286,291,3,60,30,0,287,288,7,1,0,0,288,290,
        3,60,30,0,289,287,1,0,0,0,290,293,1,0,0,0,291,289,1,0,0,0,291,292,
        1,0,0,0,292,59,1,0,0,0,293,291,1,0,0,0,294,299,3,62,31,0,295,296,
        7,2,0,0,296,298,3,62,31,0,297,295,1,0,0,0,298,301,1,0,0,0,299,297,
        1,0,0,0,299,300,1,0,0,0,300,61,1,0,0,0,301,299,1,0,0,0,302,307,3,
        64,32,0,303,304,7,3,0,0,304,306,3,64,32,0,305,303,1,0,0,0,306,309,
        1,0,0,0,307,305,1,0,0,0,307,308,1,0,0,0,308,63,1,0,0,0,309,307,1,
        0,0,0,310,315,3,66,33,0,311,312,7,4,0,0,312,314,3,66,33,0,313,311,
        1,0,0,0,314,317,1,0,0,0,315,313,1,0,0,0,315,316,1,0,0,0,316,65,1,
        0,0,0,317,315,1,0,0,0,318,319,7,5,0,0,319,322,3,66,33,0,320,322,
        3,68,34,0,321,318,1,0,0,0,321,320,1,0,0,0,322,67,1,0,0,0,323,327,
        3,72,36,0,324,326,3,70,35,0,325,324,1,0,0,0,326,329,1,0,0,0,327,
        325,1,0,0,0,327,328,1,0,0,0,328,69,1,0,0,0,329,327,1,0,0,0,330,340,
        5,31,0,0,331,340,5,32,0,0,332,333,5,34,0,0,333,340,5,47,0,0,334,
        336,5,37,0,0,335,337,3,74,37,0,336,335,1,0,0,0,336,337,1,0,0,0,337,
        338,1,0,0,0,338,340,5,38,0,0,339,330,1,0,0,0,339,331,1,0,0,0,339,
        332,1,0,0,0,339,334,1,0,0,0,340,71,1,0,0,0,341,355,5,44,0,0,342,
        355,5,45,0,0,343,355,5,46,0,0,344,355,5,47,0,0,345,346,5,37,0,0,
        346,347,3,52,26,0,347,348,5,38,0,0,348,355,1,0,0,0,349,351,5,35,
        0,0,350,352,3,74,37,0,351,350,1,0,0,0,351,352,1,0,0,0,352,353,1,
        0,0,0,353,355,5,36,0,0,354,341,1,0,0,0,354,342,1,0,0,0,354,343,1,
        0,0,0,354,344,1,0,0,0,354,345,1,0,0,0,354,349,1,0,0,0,355,73,1,0,
        0,0,356,361,3,52,26,0,357,358,5,40,0,0,358,360,3,52,26,0,359,357,
        1,0,0,0,360,363,1,0,0,0,361,359,1,0,0,0,361,362,1,0,0,0,362,75,1,
        0,0,0,363,361,1,0,0,0,35,78,80,90,105,112,119,134,159,169,178,189,
        193,197,204,210,220,231,239,242,246,254,266,275,283,291,299,307,
        315,321,327,336,339,351,354,361
    ]

class TyCParser ( Parser ):

    grammarFileName = "TyC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'auto'", "'break'", "'case'", "'continue'", 
                     "'default'", "'else'", "'float'", "'for'", "'if'", 
                     "'int'", "'return'", "'string'", "'struct'", "'switch'", 
                     "'void'", "'while'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'&&'", 
                     "'||'", "'!'", "'++'", "'--'", "'='", "'.'", "'{'", 
                     "'}'", "'('", "')'", "';'", "','", "':'" ]

    symbolicNames = [ "<INVALID>", "AUTO", "BREAK", "CASE", "CONTINUE", 
                      "DEFAULT", "ELSE", "FLOAT_KW", "FOR", "IF", "INT_KW", 
                      "RETURN", "STRING_KW", "STRUCT", "SWITCH", "VOID", 
                      "WHILE", "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQ", 
                      "NEQ", "LT", "GT", "LE", "GE", "AND", "OR", "NOT", 
                      "INC", "DEC", "ASSIGN", "DOT", "LBRACE", "RBRACE", 
                      "LPAREN", "RPAREN", "SEMI", "COMMA", "COLON", "BLOCK_COMMENT", 
                      "LINE_COMMENT", "INT", "FLOAT", "STRING", "ID", "WS", 
                      "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_structdecl = 1
    RULE_members = 2
    RULE_type = 3
    RULE_funcdecl = 4
    RULE_returntype = 5
    RULE_param = 6
    RULE_paramtype = 7
    RULE_listparam = 8
    RULE_listpr = 9
    RULE_stmt = 10
    RULE_assignstmt = 11
    RULE_condstmt = 12
    RULE_whilestmt = 13
    RULE_forstmt = 14
    RULE_init = 15
    RULE_condition = 16
    RULE_update = 17
    RULE_switchstmt = 18
    RULE_case = 19
    RULE_returnstmt = 20
    RULE_exprstmt = 21
    RULE_blockstmt = 22
    RULE_breakstmt = 23
    RULE_continuestmt = 24
    RULE_vardecl = 25
    RULE_expr = 26
    RULE_logicalOR = 27
    RULE_logicalAND = 28
    RULE_equality = 29
    RULE_relational = 30
    RULE_additive = 31
    RULE_multiplicative = 32
    RULE_unary = 33
    RULE_postfix = 34
    RULE_postfixOp = 35
    RULE_primary = 36
    RULE_arglist = 37

    ruleNames =  [ "program", "structdecl", "members", "type", "funcdecl", 
                   "returntype", "param", "paramtype", "listparam", "listpr", 
                   "stmt", "assignstmt", "condstmt", "whilestmt", "forstmt", 
                   "init", "condition", "update", "switchstmt", "case", 
                   "returnstmt", "exprstmt", "blockstmt", "breakstmt", "continuestmt", 
                   "vardecl", "expr", "logicalOR", "logicalAND", "equality", 
                   "relational", "additive", "multiplicative", "unary", 
                   "postfix", "postfixOp", "primary", "arglist" ]

    EOF = Token.EOF
    AUTO=1
    BREAK=2
    CASE=3
    CONTINUE=4
    DEFAULT=5
    ELSE=6
    FLOAT_KW=7
    FOR=8
    IF=9
    INT_KW=10
    RETURN=11
    STRING_KW=12
    STRUCT=13
    SWITCH=14
    VOID=15
    WHILE=16
    PLUS=17
    MINUS=18
    MUL=19
    DIV=20
    MOD=21
    EQ=22
    NEQ=23
    LT=24
    GT=25
    LE=26
    GE=27
    AND=28
    OR=29
    NOT=30
    INC=31
    DEC=32
    ASSIGN=33
    DOT=34
    LBRACE=35
    RBRACE=36
    LPAREN=37
    RPAREN=38
    SEMI=39
    COMMA=40
    COLON=41
    BLOCK_COMMENT=42
    LINE_COMMENT=43
    INT=44
    FLOAT=45
    STRING=46
    ID=47
    WS=48
    ERROR_CHAR=49
    ILLEGAL_ESCAPE=50
    UNCLOSE_STRING=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TyCParser.EOF, 0)

        def structdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StructdeclContext)
            else:
                return self.getTypedRuleContext(TyCParser.StructdeclContext,i)


        def funcdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.FuncdeclContext)
            else:
                return self.getTypedRuleContext(TyCParser.FuncdeclContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_program




    def program(self):

        localctx = TyCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 78
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [13]:
                    self.state = 76
                    self.structdecl()
                    pass
                elif token in [7, 10, 12, 15, 47]:
                    self.state = 77
                    self.funcdecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 80 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488401536) != 0)):
                    break

            self.state = 82
            self.match(TyCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(TyCParser.STRUCT, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LBRACE(self):
            return self.getToken(TyCParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(TyCParser.RBRACE, 0)

        def members(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.MembersContext)
            else:
                return self.getTypedRuleContext(TyCParser.MembersContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_structdecl




    def structdecl(self):

        localctx = TyCParser.StructdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_structdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(TyCParser.STRUCT)
            self.state = 85
            self.match(TyCParser.ID)
            self.state = 86
            self.match(TyCParser.LBRACE)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488360576) != 0):
                self.state = 87
                self.members()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 93
            self.match(TyCParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MembersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_members




    def members(self):

        localctx = TyCParser.MembersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_members)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.type_()
            self.state = 96
            self.match(TyCParser.ID)
            self.state = 97
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_KW(self):
            return self.getToken(TyCParser.INT_KW, 0)

        def FLOAT_KW(self):
            return self.getToken(TyCParser.FLOAT_KW, 0)

        def STRING_KW(self):
            return self.getToken(TyCParser.STRING_KW, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_type




    def type_(self):

        localctx = TyCParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488360576) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returntype(self):
            return self.getTypedRuleContext(TyCParser.ReturntypeContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(TyCParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(TyCParser.RBRACE, 0)

        def listparam(self):
            return self.getTypedRuleContext(TyCParser.ListparamContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.StmtContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_funcdecl




    def funcdecl(self):

        localctx = TyCParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.returntype()
            self.state = 102
            self.match(TyCParser.ID)
            self.state = 103
            self.match(TyCParser.LPAREN)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488360576) != 0):
                self.state = 104
                self.listparam()


            self.state = 107
            self.match(TyCParser.RPAREN)
            self.state = 108
            self.match(TyCParser.LBRACE)
            self.state = 110 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 109
                self.stmt()
                self.state = 112 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 264062106034068) != 0)):
                    break

            self.state = 114
            self.match(TyCParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturntypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def VOID(self):
            return self.getToken(TyCParser.VOID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_returntype




    def returntype(self):

        localctx = TyCParser.ReturntypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_returntype)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.type_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(TyCParser.VOID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramtype(self):
            return self.getTypedRuleContext(TyCParser.ParamtypeContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_param




    def param(self):

        localctx = TyCParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.paramtype()
            self.state = 122
            self.match(TyCParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_KW(self):
            return self.getToken(TyCParser.INT_KW, 0)

        def FLOAT_KW(self):
            return self.getToken(TyCParser.FLOAT_KW, 0)

        def STRING_KW(self):
            return self.getToken(TyCParser.STRING_KW, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_paramtype




    def paramtype(self):

        localctx = TyCParser.ParamtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paramtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488360576) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListparamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(TyCParser.ParamContext,0)


        def listpr(self):
            return self.getTypedRuleContext(TyCParser.ListprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_listparam




    def listparam(self):

        localctx = TyCParser.ListparamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_listparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.param()
            self.state = 127
            self.listpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(TyCParser.COMMA, 0)

        def param(self):
            return self.getTypedRuleContext(TyCParser.ParamContext,0)


        def listpr(self):
            return self.getTypedRuleContext(TyCParser.ListprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_listpr




    def listpr(self):

        localctx = TyCParser.ListprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_listpr)
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(TyCParser.COMMA)
                self.state = 130
                self.param()
                self.state = 131
                self.listpr()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(TyCParser.VardeclContext,0)


        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def assignstmt(self):
            return self.getTypedRuleContext(TyCParser.AssignstmtContext,0)


        def condstmt(self):
            return self.getTypedRuleContext(TyCParser.CondstmtContext,0)


        def switchstmt(self):
            return self.getTypedRuleContext(TyCParser.SwitchstmtContext,0)


        def whilestmt(self):
            return self.getTypedRuleContext(TyCParser.WhilestmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(TyCParser.ForstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(TyCParser.ReturnstmtContext,0)


        def exprstmt(self):
            return self.getTypedRuleContext(TyCParser.ExprstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(TyCParser.BlockstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(TyCParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(TyCParser.ContinuestmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_stmt




    def stmt(self):

        localctx = TyCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_stmt)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.vardecl()
                self.state = 137
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.assignstmt()
                self.state = 140
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.condstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 143
                self.switchstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 144
                self.whilestmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 145
                self.forstmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 146
                self.returnstmt()
                self.state = 147
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 149
                self.exprstmt()
                self.state = 150
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 152
                self.blockstmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 153
                self.breakstmt()
                self.state = 154
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 156
                self.continuestmt()
                self.state = 157
                self.match(TyCParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.ID)
            else:
                return self.getToken(TyCParser.ID, i)

        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def DOT(self):
            return self.getToken(TyCParser.DOT, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_assignstmt




    def assignstmt(self):

        localctx = TyCParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignstmt)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(TyCParser.ID)
                self.state = 162
                self.match(TyCParser.ASSIGN)
                self.state = 163
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(TyCParser.ID)
                self.state = 165
                self.match(TyCParser.DOT)
                self.state = 166
                self.match(TyCParser.ID)
                self.state = 167
                self.match(TyCParser.ASSIGN)
                self.state = 168
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(TyCParser.IF, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(TyCParser.ELSE, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_condstmt




    def condstmt(self):

        localctx = TyCParser.CondstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_condstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(TyCParser.IF)
            self.state = 172
            self.match(TyCParser.LPAREN)
            self.state = 173
            self.expr()
            self.state = 174
            self.match(TyCParser.RPAREN)
            self.state = 175
            self.stmt()
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 176
                self.match(TyCParser.ELSE)
                self.state = 177
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(TyCParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def stmt(self):
            return self.getTypedRuleContext(TyCParser.StmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_whilestmt




    def whilestmt(self):

        localctx = TyCParser.WhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(TyCParser.WHILE)
            self.state = 181
            self.match(TyCParser.LPAREN)
            self.state = 182
            self.expr()
            self.state = 183
            self.match(TyCParser.RPAREN)
            self.state = 184
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(TyCParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.SEMI)
            else:
                return self.getToken(TyCParser.SEMI, i)

        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def stmt(self):
            return self.getTypedRuleContext(TyCParser.StmtContext,0)


        def init(self):
            return self.getTypedRuleContext(TyCParser.InitContext,0)


        def condition(self):
            return self.getTypedRuleContext(TyCParser.ConditionContext,0)


        def update(self):
            return self.getTypedRuleContext(TyCParser.UpdateContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_forstmt




    def forstmt(self):

        localctx = TyCParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(TyCParser.FOR)
            self.state = 187
            self.match(TyCParser.LPAREN)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488360576) != 0):
                self.state = 188
                self.init()


            self.state = 191
            self.match(TyCParser.SEMI)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 264062105944064) != 0):
                self.state = 192
                self.condition()


            self.state = 195
            self.match(TyCParser.SEMI)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 264062105944064) != 0):
                self.state = 196
                self.update()


            self.state = 199
            self.match(TyCParser.RPAREN)
            self.state = 200
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(TyCParser.VardeclContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(TyCParser.AssignstmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_init




    def init(self):

        localctx = TyCParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_init)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.assignstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_condition




    def condition(self):

        localctx = TyCParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstmt(self):
            return self.getTypedRuleContext(TyCParser.AssignstmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_update




    def update(self):

        localctx = TyCParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_update)
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.assignstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(TyCParser.SWITCH, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(TyCParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(TyCParser.RBRACE, 0)

        def case(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.CaseContext)
            else:
                return self.getTypedRuleContext(TyCParser.CaseContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_switchstmt




    def switchstmt(self):

        localctx = TyCParser.SwitchstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_switchstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(TyCParser.SWITCH)
            self.state = 213
            self.match(TyCParser.LPAREN)
            self.state = 214
            self.expr()
            self.state = 215
            self.match(TyCParser.RPAREN)
            self.state = 216
            self.match(TyCParser.LBRACE)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==5:
                self.state = 217
                self.case()
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 223
            self.match(TyCParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(TyCParser.CASE, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def COLON(self):
            return self.getToken(TyCParser.COLON, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.StmtContext,i)


        def DEFAULT(self):
            return self.getToken(TyCParser.DEFAULT, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_case




    def case(self):

        localctx = TyCParser.CaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_case)
        self._la = 0 # Token type
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(TyCParser.CASE)
                self.state = 226
                self.expr()
                self.state = 227
                self.match(TyCParser.COLON)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 264062106034068) != 0):
                    self.state = 228
                    self.stmt()
                    self.state = 233
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(TyCParser.DEFAULT)
                self.state = 235
                self.match(TyCParser.COLON)
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 264062106034068) != 0):
                    self.state = 236
                    self.stmt()
                    self.state = 241
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(TyCParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_returnstmt




    def returnstmt(self):

        localctx = TyCParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(TyCParser.RETURN)
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 264062105944064) != 0):
                self.state = 245
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_exprstmt




    def exprstmt(self):

        localctx = TyCParser.ExprstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exprstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(TyCParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(TyCParser.RBRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.StmtContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_blockstmt




    def blockstmt(self):

        localctx = TyCParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_blockstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(TyCParser.LBRACE)
            self.state = 252 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 251
                self.stmt()
                self.state = 254 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 264062106034068) != 0)):
                    break

            self.state = 256
            self.match(TyCParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(TyCParser.BREAK, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_breakstmt




    def breakstmt(self):

        localctx = TyCParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(TyCParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(TyCParser.CONTINUE, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_continuestmt




    def continuestmt(self):

        localctx = TyCParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(TyCParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_vardecl




    def vardecl(self):

        localctx = TyCParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.type_()
            self.state = 263
            self.match(TyCParser.ID)
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 264
                self.match(TyCParser.ASSIGN)
                self.state = 265
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOR(self):
            return self.getTypedRuleContext(TyCParser.LogicalORContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_expr




    def expr(self):

        localctx = TyCParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.logicalOR()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalORContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAND(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.LogicalANDContext)
            else:
                return self.getTypedRuleContext(TyCParser.LogicalANDContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.OR)
            else:
                return self.getToken(TyCParser.OR, i)

        def getRuleIndex(self):
            return TyCParser.RULE_logicalOR




    def logicalOR(self):

        localctx = TyCParser.LogicalORContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_logicalOR)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.logicalAND()
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 271
                self.match(TyCParser.OR)
                self.state = 272
                self.logicalAND()
                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalANDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.EqualityContext)
            else:
                return self.getTypedRuleContext(TyCParser.EqualityContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.AND)
            else:
                return self.getToken(TyCParser.AND, i)

        def getRuleIndex(self):
            return TyCParser.RULE_logicalAND




    def logicalAND(self):

        localctx = TyCParser.LogicalANDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_logicalAND)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.equality()
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 279
                self.match(TyCParser.AND)
                self.state = 280
                self.equality()
                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.RelationalContext)
            else:
                return self.getTypedRuleContext(TyCParser.RelationalContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.EQ)
            else:
                return self.getToken(TyCParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.NEQ)
            else:
                return self.getToken(TyCParser.NEQ, i)

        def getRuleIndex(self):
            return TyCParser.RULE_equality




    def equality(self):

        localctx = TyCParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.relational()
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==23:
                self.state = 287
                _la = self._input.LA(1)
                if not(_la==22 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 288
                self.relational()
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.AdditiveContext)
            else:
                return self.getTypedRuleContext(TyCParser.AdditiveContext,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.LT)
            else:
                return self.getToken(TyCParser.LT, i)

        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.LE)
            else:
                return self.getToken(TyCParser.LE, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.GT)
            else:
                return self.getToken(TyCParser.GT, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.GE)
            else:
                return self.getToken(TyCParser.GE, i)

        def getRuleIndex(self):
            return TyCParser.RULE_relational




    def relational(self):

        localctx = TyCParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.additive()
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 251658240) != 0):
                self.state = 295
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 251658240) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 296
                self.additive()
                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.MultiplicativeContext)
            else:
                return self.getTypedRuleContext(TyCParser.MultiplicativeContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.PLUS)
            else:
                return self.getToken(TyCParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.MINUS)
            else:
                return self.getToken(TyCParser.MINUS, i)

        def getRuleIndex(self):
            return TyCParser.RULE_additive




    def additive(self):

        localctx = TyCParser.AdditiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_additive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.multiplicative()
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17 or _la==18:
                self.state = 303
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 304
                self.multiplicative()
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.UnaryContext)
            else:
                return self.getTypedRuleContext(TyCParser.UnaryContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.MUL)
            else:
                return self.getToken(TyCParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.DIV)
            else:
                return self.getToken(TyCParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.MOD)
            else:
                return self.getToken(TyCParser.MOD, i)

        def getRuleIndex(self):
            return TyCParser.RULE_multiplicative




    def multiplicative(self):

        localctx = TyCParser.MultiplicativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_multiplicative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.unary()
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0):
                self.state = 311
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 312
                self.unary()
                self.state = 317
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(TyCParser.UnaryContext,0)


        def NOT(self):
            return self.getToken(TyCParser.NOT, 0)

        def MINUS(self):
            return self.getToken(TyCParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(TyCParser.PLUS, 0)

        def INC(self):
            return self.getToken(TyCParser.INC, 0)

        def DEC(self):
            return self.getToken(TyCParser.DEC, 0)

        def postfix(self):
            return self.getTypedRuleContext(TyCParser.PostfixContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_unary




    def unary(self):

        localctx = TyCParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18, 30, 31, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7516585984) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 319
                self.unary()
                pass
            elif token in [35, 37, 44, 45, 46, 47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.postfix()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(TyCParser.PrimaryContext,0)


        def postfixOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.PostfixOpContext)
            else:
                return self.getTypedRuleContext(TyCParser.PostfixOpContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_postfix




    def postfix(self):

        localctx = TyCParser.PostfixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_postfix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.primary()
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 161061273600) != 0):
                self.state = 324
                self.postfixOp()
                self.state = 329
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INC(self):
            return self.getToken(TyCParser.INC, 0)

        def DEC(self):
            return self.getToken(TyCParser.DEC, 0)

        def DOT(self):
            return self.getToken(TyCParser.DOT, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def arglist(self):
            return self.getTypedRuleContext(TyCParser.ArglistContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_postfixOp




    def postfixOp(self):

        localctx = TyCParser.PostfixOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_postfixOp)
        self._la = 0 # Token type
        try:
            self.state = 339
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.match(TyCParser.INC)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.match(TyCParser.DEC)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 332
                self.match(TyCParser.DOT)
                self.state = 333
                self.match(TyCParser.ID)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 4)
                self.state = 334
                self.match(TyCParser.LPAREN)
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 264062105944064) != 0):
                    self.state = 335
                    self.arglist()


                self.state = 338
                self.match(TyCParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TyCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(TyCParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(TyCParser.STRING, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(TyCParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(TyCParser.RBRACE, 0)

        def arglist(self):
            return self.getTypedRuleContext(TyCParser.ArglistContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_primary




    def primary(self):

        localctx = TyCParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.match(TyCParser.INT)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.match(TyCParser.FLOAT)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 3)
                self.state = 343
                self.match(TyCParser.STRING)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 4)
                self.state = 344
                self.match(TyCParser.ID)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 5)
                self.state = 345
                self.match(TyCParser.LPAREN)
                self.state = 346
                self.expr()
                self.state = 347
                self.match(TyCParser.RPAREN)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 6)
                self.state = 349
                self.match(TyCParser.LBRACE)
                self.state = 351
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 264062105944064) != 0):
                    self.state = 350
                    self.arglist()


                self.state = 353
                self.match(TyCParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArglistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.COMMA)
            else:
                return self.getToken(TyCParser.COMMA, i)

        def getRuleIndex(self):
            return TyCParser.RULE_arglist




    def arglist(self):

        localctx = TyCParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_arglist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.expr()
            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 357
                self.match(TyCParser.COMMA)
                self.state = 358
                self.expr()
                self.state = 363
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





