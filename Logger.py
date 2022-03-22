class Logger():
    def __init__(self,mensaje):
        self.mensaje=mensaje
    def __str__(self):
        cadena = '--Start log--'
        for i in range (1,6):
            cadena += '/n '+i +'ªllamada'

        cadena+= '/n --End log:'+ '5 log(s)--'

class Test():
    def __init__(self,test):
        self.test = test
