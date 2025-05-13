from antlr4 import *
from antlr.MayoLexer import MayoLexer
from antlr.MayoParser import MayoParser
from antlr.MayoListener import MayoListener
import sys

class miListener(MayoListener):
    def enterRepite(self, ctx: MayoParser.RepiteContext):
        #print(type(ctx.expresion()))
        if not isinstance(ctx.expresion(),  MayoParser.ConstanteContext):
            raise Exception("Error, repite no tiene constante para la expresion")

def main():
    parser = MayoParser(CommonTokenStream(MayoLexer(FileStream('test.txt'))))
    tree = parser.program()

    walker = ParseTreeWalker()
    walker.walk(miListener(), tree)

if __name__ == '__main__':
    main()