grammar Mayo;

program: (expresion | sentencia)*;

sentencia:
    'si' expresion 'entonces' sentencia 'contrariamente' sentencia '_' #ifelse
    | 'si' expresion 'entonces' sentencia  '_'                         #if
    | 'trastrueco' expresion  encasode* '_'                           #switch
    | expresion                                 #sent_exp
    | 'repite' expresion ':' sentencia  '_'        #repite
    | 'mientras' expresion 'ejecuta' sentencia   '_'      #while
    | tipo VARIABLE '(' var_decl (',' var_decl)* ')' '{' sentencia+ '}' #func_def
    | VARIABLE '(' expresion (',' expresion)* ')' #func_call
    | tipo VARIABLE (',' VARIABLE)* #decl
    ;

var_decl: tipo VARIABLE;

tipo: 'entero' | 'cadena';

encasode:
    'encasode' expresion ':' sentencia
    ;

expresion:
    expresion  '*' expresion    #multi
    | expresion '+' expresion   #suma
    | NUMERO                    #entero
    | FLOTANTE                  #flotante
    | CADENA                    #cadena
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
CADENA: '"' [a-zA-Z0-9]* '"';
FLOTANTE: [0-9]* '.' [0-9]*;
VARIABLE: [a-zA-Z0-9_]+;
SPACE: [ \n\r]+ -> skip;