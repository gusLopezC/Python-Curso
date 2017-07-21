def palindromo(frase):

    valor2=frase.replace(' ','')#variable local solo se aplica al metodo
    return valor2==valor2[::-1]


frase='anita lava la tina'#es globalse usa en todo el proyecto

resultado = palindromo(frase)
print(resultado)

#-------------
#se una palabara reservada global para hacer la variable local a global
def valor_global():
    global variable_global
    variable_global='Texto cambiado'

variable_global='Esto es una variable global'
print(variable_global)
valor_global();
print(variable_global)