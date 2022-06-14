from Minerales import minerales

class AgenteClasificador:
    
    '''
        Clase que representa al agente clasificador de piedras por minerales

        Args
        ----
        piedra(int): indica la piedra
        densidad(float): indica la densidad de la piedra que será evaluado para detectar cada mineral
        dureza(float): indica la dureza de la piedra basado en la escala de Mohs

        Metodos
        -------
        __init__(self)
        validarInt(self,numero)
        validarFloat(self,numero)
        ingresoPiedra(self,piedra)
        ingresoDensidad(self,densidad)
        ingresoDureza(self,dureza)
    '''

    #Se inicializan variables propias de la clase
    piedra = 0
    densidad = 0
    dureza = 0
    costo = 0

    def __init__(self):

        return None

    def validarInt(self,numero):
        try:
            int(numero)
            esInt = True
        except:
            print("No es un número")
            esInt = False
        
        return esInt

    def validarFloat(self,numero):
        try:
            float(numero)
            esFloat = True
        except:
            print("No es un número")
            esFloat = False
        
        return esFloat


    def ingresoPiedra(self,piedra):
        esInt = self.validarInt(piedra)
        if(esInt == True):
            piedra = int(piedra)
            if(piedra == 0 or piedra == 1):
                self.piedra = piedra
                self.costo += 1
                return False
            else:
                print("Ingrese 1 ó 0")
                return True
    


        

    def ingresoDensidad(self,densidad):
        try:
            self.densidad = float(densidad)
            if(self.densidad >= 1.5 and self.densidad <= 6):
                print('Se ha recibido un registro')
                return False
            else:
                print('Se ingresa entre 1.5 a 6')
                return True

        except:
            print('No se ha ingresado un número')
        
        

    
    def ingresoDureza(self,dureza):
        try:
            self.dureza = float(dureza)
            if(self.dureza >= 1 and self.dureza <= 9):
                print('Se ha recibido un registro')
                costo += 1
                return False
            else:
                print('Se ingresa entre 1 a 9')
                return True

        except:
            print('No se ha ingresado un número')
        
       



if __name__ == '__main__':

    agente = AgenteClasificador()
    while True:
        C_densidad = True
        C_dureza = True
        piedra = input('Ingrese la piedra (1 ó 0): ')
        agente.ingresoPiedra(piedra)
        if(agente.piedra == 1):
            while(C_densidad == True):
                densidad = input('Ingrese la densidad: ')
                C_densidad = agente.ingresoDensidad(densidad)
            
            while(C_dureza == True):
                dureza = input('Ingrese la dureza: ')
                C_dureza = agente.ingresoDureza(dureza)
            
            mineral = minerales.esFluorita()
            mineral = minerales.esAragonita()
            mineral = minerales.esCalcita()
            mineral = minerales.esCuarzo()
            mineral = minerales.esDolomita()
            mineral = minerales.esGypsum()
            mineral = minerales.esHalita()
            mineral = minerales.esMagnetita()

            print('El mineral hallado es: ', mineral)
            print('El costo de la ejecución es: ', agente.costo)

        opcion = input('Desea continuar con la ejecución (si/no): ').lower
        
        if(opcion == 'si'):
            print('------------------------------------------')
        elif(opcion == 'no'):
            break
        else:
            print('Se ha escrito una opción errónea')

                    

            
            
            
        

        
    

        
