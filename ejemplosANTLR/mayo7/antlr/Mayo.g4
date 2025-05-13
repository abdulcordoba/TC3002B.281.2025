grammar Mayo;

program: (expresion | sentencia)*;

sentencia:
    'si' expresion 'entonces' sentencia 'contrariamente' sentencia '_' #ifelse
    | 'si' expresion 'entonces' sentencia  '_'                         #if
    | 'trastrueco' expresion  encasode* '_'                           #switch
    | expresion                                 #sent_exp
    | 'repite' expresion ':' sentencia  '_'        #repite
    | 'mientras' expresion 'ejecuta' sentencia   '_'      #while
    ;

encasode:
    'encasode' expresion ':' sentencia
    ;

expresion:
    expresion  '*' expresion    #multi
    | expresion '+' expresion   #suma
    | NUMERO                    #constante
    | VARIABLE                  #var
    | '(' expresion ')'         #lista
    | VARIABLE '=' expresion    #asignacion
    | 'def' VARIABLE params 'as' sentencia* '_' #funcion
    ;

params:
    VARIABLE (',' VARIABLE)*
    ;


UNO: 'uno';
DOS: 'dos';
TRES: 'tres';
NUMERO: [0-9]+;
VARIABLE: [a-zA-Z0-9_]+;
SPACE: [ \n\r]+ -> skip;