class Palindromo():

    def __init__(self,palindromo):
        self.palindromo = palindromo
    def __str__(self):
        return es_palindromo(self.palindromo)

    def es_palindromo(palabra):                    # Reutilizamos el codigo de la funcion palindromo de los ejercicicos de recursividad
        a,b = 'áéíóúüñÁÉÍÓÚÜ','aeiouunAEIOUU'
        palabra = palabra.replace(" ","")
        trans = str.maketrans(a,b)
        string = palabra.translate(trans)
        if len(string)<2:
            return True
        elif string.lower()[0]!=string.lower()[-1]:
            return False
        return es_palindromo(string[1:-1])