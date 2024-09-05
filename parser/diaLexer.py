# Generated from ./dia.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,60,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,1,1,1,1,2,1,2,1,3,4,3,25,8,3,11,3,12,3,26,
        1,3,1,3,1,4,4,4,32,8,4,11,4,12,4,33,1,4,1,4,1,5,1,5,5,5,40,8,5,10,
        5,12,5,43,9,5,1,5,1,5,1,6,1,6,5,6,49,8,6,10,6,12,6,52,9,6,1,6,1,
        6,1,7,4,7,57,8,7,11,7,12,7,58,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,
        7,15,8,1,0,5,2,0,10,10,13,13,3,0,9,9,12,12,32,32,1,0,39,39,1,0,34,
        34,7,0,10,10,13,13,34,34,39,39,59,59,123,123,125,125,64,0,1,1,0,
        0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,
        0,13,1,0,0,0,0,15,1,0,0,0,1,17,1,0,0,0,3,19,1,0,0,0,5,21,1,0,0,0,
        7,24,1,0,0,0,9,31,1,0,0,0,11,37,1,0,0,0,13,46,1,0,0,0,15,56,1,0,
        0,0,17,18,5,123,0,0,18,2,1,0,0,0,19,20,5,125,0,0,20,4,1,0,0,0,21,
        22,5,59,0,0,22,6,1,0,0,0,23,25,7,0,0,0,24,23,1,0,0,0,25,26,1,0,0,
        0,26,24,1,0,0,0,26,27,1,0,0,0,27,28,1,0,0,0,28,29,6,3,0,0,29,8,1,
        0,0,0,30,32,7,1,0,0,31,30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,
        34,1,0,0,0,34,35,1,0,0,0,35,36,6,4,0,0,36,10,1,0,0,0,37,41,5,39,
        0,0,38,40,8,2,0,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,
        1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,44,45,5,39,0,0,45,12,1,0,0,0,
        46,50,5,34,0,0,47,49,8,3,0,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,1,
        0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,50,1,0,0,0,53,54,5,34,0,0,54,
        14,1,0,0,0,55,57,8,4,0,0,56,55,1,0,0,0,57,58,1,0,0,0,58,56,1,0,0,
        0,58,59,1,0,0,0,59,16,1,0,0,0,6,0,26,33,41,50,58,1,6,0,0
    ]

class diaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LPAREN = 1
    RPAREN = 2
    SEMICOLON = 3
    LINEBREAK = 4
    WS = 5
    STRING_SINGLE = 6
    STRING_DOUBLE = 7
    CODE = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "LPAREN", "RPAREN", "SEMICOLON", "LINEBREAK", "WS", "STRING_SINGLE", 
            "STRING_DOUBLE", "CODE" ]

    ruleNames = [ "LPAREN", "RPAREN", "SEMICOLON", "LINEBREAK", "WS", "STRING_SINGLE", 
                  "STRING_DOUBLE", "CODE" ]

    grammarFileName = "dia.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


