from antlr4 import *

# elParser, elLexer, elListener serán generados a partir del .g4, importar arriba

class miListener(elListener):
    # Aquí sobreescribir los métodos del Listener genérico para implementar la lógica
    # Recordar orden en profundidad del recorrido

    # Por ejemplo
    # ctx: elParser.ProgramContext tiene los métodos para recuperar las partes de esa regla gramatical
    # Si la regla en el g4 es: program: (expresion | sentencia)*;
    # existen métodos: ctx.expresion(), ctx.sentencia() para no terminales
    # si son tokens: holamundo: VARIABLE
    # entonces existe: ctx.VARIABLE().getText()
    # para recuperar el string correspondiente al token

    # def enterProgram(self, ctx: elParser.ProgramContext):
    #    pass

    pass

def main():
    parser = elParser(CommonTokenStream(elLexer(FileStream('test.txt'))))
    tree = parser.program()

    walker = ParseTreeWalker()
    # Puedo hacer los recorridos con los listeners que quiera!

    walker.walk(miListener(), tree)
    walker.walk(miListener(), tree)
    walker.walk(miListener(), tree)

if __name__ == '__main__':
    main()