class Palindromo():

    def __init__(self,palindromo):
        self.palindromo = palindromo

    def __str__(self):
        return str(self.palindromo.upper())

    @staticmethod
    def esPalindromo(palabra):                    # Reutilizamos el codigo de la funcion palindromo de los ejercicicos de recursividad
        a,b = 'áéíóúüñÁÉÍÓÚÜ','aeiouunAEIOUU'
        palabra = palabra.replace(" ","")
        trans = str.maketrans(a,b)
        string = palabra.translate(trans)

        if len(string)<2:
            return True
        elif string.lower()[0]!=string.lower()[-1]:
            return False
        return esPalindromo(string[1:-1])         # Aqui no entiendo porque no reconoce la funcion esPalindromo

    def test(self):
        booleano = esPalindromo(self.palindromo)
        return booleano

# Pregunta adicional: Porque primero se ejecuta el test(), por lo que sale primero True, y luego el print de RADAR