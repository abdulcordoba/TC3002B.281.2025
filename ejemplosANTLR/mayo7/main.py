from antlr4 import *
from antlr.MayoLexer import MayoLexer
from antlr.MayoParser import MayoParser
from antlr.MayoListener import MayoListener
import sys

class miListener(MayoListener):
    variables = {}
    def enterDecl(self, ctx:MayoParser.DeclContext):
        for x in ctx.VARIABLE():
            #if x.getText() in self.variables.keys():
            #    raise Exception("Variable {} redeclarada ".format(x.getText()))
            self.variables[x.getText()] = ctx.tipo().getText()
    def enterAsignacion(self, ctx:MayoParser.AsignacionContext):
        v = ctx.VARIABLE().getText()
        if v not in self.variables.keys():
            raise Exception("Variable '{}' no declarada previamente".format(v))
class miListener2(MayoListener):
    def exitMulti(self, ctx:MayoParser.MultiContext):
        #Inferencia de tipos
        if ctx.expresion(0).data_type != ctx.expresion(1).data_type:
            raise Exception("Error en operación")
        ctx.data_type = ctx.expresion(0).data_type
    def enterVar(self, ctx:MayoParser.VarContext):
        ctx.data_type = self.variables[ctx.getText()]
    def enterEntero(self, ctx:MayoParser.EnteroContext):
        ctx.data_type = 'entero'
    def enterFlotante(self, ctx:MayoParser.FlotanteContext):
        ctx.data_type = 'flotante'
    def enterCadena(self, ctx:MayoParser.CadenaContext):
        ctx.data_type = 'cadena'
class miListener3(MayoListener):
    funciones = {}
    def enterFunc_def(self, ctx:MayoParser.Func_defContext):
        params = {}
        for x in ctx.var_decl():
            params[x.VARIABLE().getText()] = x.tipo().getText()
        self.funciones[ctx.VARIABLE().getText()] = params
    def exitFunc_call(self, ctx:MayoParser.Func_callContext):
        params = self.funciones[ctx.VARIABLE().getText()]
        if len(ctx.expresion()) != len(params):
            raise Exception("# de parámetros({}) no coincide con la definición({})".format(len(ctx.expresion()), len(params)))
        for e, t in zip(ctx.expresion(), params.values()):
            if e.data_type != t:
                raise Exception("Tipos no coinciden exp:{} y var:{}".format(e.data_type,t))
def main():
    parser = MayoParser(CommonTokenStream(MayoLexer(FileStream('test.txt'))))
    tree = parser.program()

    walker = ParseTreeWalker()
    #walker.walk(miListener(), tree)
    walker.walk(miListener2(), tree)
    walker.walk(miListener3(), tree)

if __name__ == '__main__':
    main()