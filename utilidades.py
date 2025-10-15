# utilidades.py

class Utilidades:

    @staticmethod
    def es_primo(n): # esta función dice si es primo (true) o no (false), recibe un número n
        if n < 2: #números primos solo hay a partir de 2, asi que los menores de dos = false
            return False

        i = 2 # inicializo en 2
        while i < n: # pruebo valores mientras que i sea menor que n
            if n % i == 0:   # si el resto es 0, no es primo (false)
                return False
            i = i + 1  # probamos el siguiente número menor que n

        return True


    @staticmethod
    def factorial(n):
        if n < 0:
            return "No existe el factorial de un número negativo"

        resultado = 1 # inicializo la variable en 1 porque al multiplicar por 1 se queda igual
        i = 1 # empiezo el contador en 1

        while i <= n: # mientras que i sea menor o igual a n sigo
            resultado = resultado * i   # multiplico el resultado por i
            i = i + 1  # siguiente número

        return resultado # devuelve el resultado del factorial

    # palíndromo = palabra que se lee igual al derecho y al revés
    @staticmethod
    def es_palindromo(cadena):
        cadena = cadena.lower() # todo a minusculas
        cadena = cadena.replace(" ", "") # quito espacios

        if cadena == cadena[::-1]: # comparo la cadena con la cadena al revés
            return True
        else:
            return False

    @staticmethod
    def suma_digitos(n): # devuelve la suma de los dígitos de n
        n = abs(n) # pongo n en valor absoluto (si es negativo el signo lo contaría como digito y daria error)
        texto = str(n) # cambio n a texto para poder recorrer cada dígito
        suma = 0 # creo la variable suma para ir sumando los dígitos

        # recorro cada caracter de la cadena (cada dígito)
        for caracter in texto:
            suma = suma + int(caracter)  # convertimos el carácter a número y lo sumamos

        return suma # devuelve el resultado de la suma


# pruebas
if __name__ == "__main__":
    # es_primo
    print(Utilidades.es_primo(3))
    print(Utilidades.es_primo(4))

    # factorial
    print(Utilidades.factorial(3))
    print(Utilidades.factorial(5))

    # es_palindromo
    print(Utilidades.es_palindromo("reconocer"))
    print(Utilidades.es_palindromo("Python"))

    # suma_digitos
    print(Utilidades.suma_digitos(12345))
    print(Utilidades.suma_digitos(-90210))

    