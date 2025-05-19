/* De prefererencia cambiar el nombre del lenguaje aquí y en el nombre del archivo */
grammar MiLenguaje;

/* Sintáctico */
program: ;


/*
La sintaxis de las reglas es:

regla1:
    regla2 TOKEN1 regla2 "tokenliteral" regla2 #nombredelnodo1
    | regla2 TOKEN1 regla2 "tokenliteral" regla2 #nombredelnodo2
    | regla2 TOKEN1 regla2 "tokenliteral" regla2 #nombredelnodo3
    ;

    Se puede usar libremente la recursión.

    Por ejemplo

expresion:
    expresion "**" expresion    #dobleasterisco
    | expresion "##" expresion  #doblehash
    | TOKEN                     #casoHoja
    ;

*/


/* Léxico
En mayúsculas el nombre del token y luego una regexp. Se usan arriba en las reglas de la gramática.
*/

/*
Ejemplos:

TOKEN1: "palabrareservada";
TOKEN2: "mas" | "de" | "una";

TOKEN3: [b-x]+;

BLANK: "todosmissblanks" -> skip;

*/