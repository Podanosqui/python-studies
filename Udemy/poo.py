class Casa: # Classe
    def __init__(self, cor, quartos, banheiros): # Construtor
        
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros
        
    # Métodos
    def mostrar_cor(self): 
        print(f'A cor da casa é {self.cor}')
        
    def mostrar_quartos(self):
        print(f'Essa casa tem {self.quartos} quartos')
        
    def mostrar_banheiros(self):
        print(f'A casa tem {self.banheiros} banheiros.')
        
    def pintar_casa(self, nova_cor):
        print(f'Printando a casa de {self.cor} para {nova_cor}')
        

# Instâncias da classe
casa1 = Casa('Azul', 4, 1)
casa2 = Casa('Amarela', 6, 0)

print('Casa 1:')
casa1.mostrar_cor()
casa1.mostrar_quartos()
casa1.mostrar_banheiros()
casa1.pintar_casa('Rosa')

print('\nCasa 2:')
casa2.mostrar_cor()
casa2.mostrar_quartos()
casa2.mostrar_banheiros()