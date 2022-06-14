from Clasificador import AgenteClasificador

class minerales:
    '''
    Clase usada para llevar las sentencias para cada mineral, conectada a la clase clasificador para obtener los atributos de dicha clase

    atributos
    ---------
        none
    
    mètodos
    -------
        __init__(self)
        esHalita(self)
        esGypsum(self)
        esCalcita(self)
        esDolomita(self)
        esAragonita(self)
    
    '''


    def __init__(self):

        return None

    def esHalita(self):

        if(AgenteClasificador.dureza >= 2 and AgenteClasificador.dureza <= 2.5):
            if(AgenteClasificador.densidad >= 2 and self.densidad <= 2.165):
                AgenteClasificador.mineral = 'Halita'
                AgenteClasificador.costo += 1

        return AgenteClasificador.mineral

    def esGypsum(self):
            
        if(AgenteClasificador.dureza >= 2 and AgenteClasificador.dureza <= 2.5):
            if(AgenteClasificador.densidad >= 2.3 and AgenteClasificador.densidad <= 2.33):
                AgenteClasificador.mineral = 'Gypsum'
                AgenteClasificador.costo += 1

        return AgenteClasificador.mineral


    def esCalcita(self):

        if(AgenteClasificador.dureza >= 3 and AgenteClasificador.dureza <= 3.5):
            if(AgenteClasificador.densidad >= 2.7 and AgenteClasificador.densidad <= 2.72):
                AgenteClasificador.mineral = 'Calcita'
                AgenteClasificador.costo += 1

        return AgenteClasificador.mineral

    def esDolomita(self):

        if(AgenteClasificador.dureza >= 3.5 and AgenteClasificador.dureza <= 4):
            if(AgenteClasificador.densidad >= 2.8 and AgenteClasificador.densidad <= 2.84):
                AgenteClasificador.mineral = 'Dolomita'
                AgenteClasificador.costo += 1

        return AgenteClasificador.mineral
        
    def esAragonita(self):

        if(AgenteClasificador.dureza >= 3.5 and AgenteClasificador.dureza <= 4):
            if(AgenteClasificador.densidad >= 2.9 and AgenteClasificador.densidad <= 2.94):
                AgenteClasificador.mineral = 'Aragonita'
                AgenteClasificador.costo += 1

        return AgenteClasificador.mineral

    def esFluorita(self):

        if(AgenteClasificador.dureza >= 4 and AgenteClasificador.dureza <= 4.5):
            if(AgenteClasificador.densidad >= 3 and AgenteClasificador.densidad <= 3.5):
                AgenteClasificador.mineral = 'Fluorita'
                AgenteClasificador.costo += 1

        return AgenteClasificador.mineral
    
    def esMagnetita(self):

        if(AgenteClasificador.dureza >= 5 and AgenteClasificador.dureza <= 5.5):
            if(AgenteClasificador.densidad >= 5.1 and AgenteClasificador.densidad <= 5.2):
                AgenteClasificador.mineral = 'Magnetita'
                AgenteClasificador.costo += 1

        return AgenteClasificador.mineral

    def esCuarzo(self):

        if(AgenteClasificador.dureza >= 7 and AgenteClasificador.dureza <= 7.5):
            if(AgenteClasificador.densidad >= 2.6 and AgenteClasificador.densidad <= 2.66):
                AgenteClasificador.mineral = 'Cuarzo'
                AgenteClasificador.costo += 1

        return AgenteClasificador.mineral
