
from abc import ABC, abstractmethod

class Transporte (ABC):
    @abstractmethod
    def entregar(self, pacote):
        pass
    
class Caminhao(Transporte):
    def entregar(self, pacote):
        return f"Caminhao está entregando o pacote {pacote}"
    
class Navio(Transporte):
    def entregar(self, pacote):
        return f"Navio esta entregando o pacote {pacote}"
#classe Factory method
class FabricaTransporte:
    def criar_transporte(self, tipo_transporte):
             if tipo_transporte == "Caminhão":
                 return Caminhao()
             elif tipo_transporte == "Navio":
                 return Navio()
             else:
                 raise ValueError("Tipo de transporte invalido")
          
    #codigo cliente que usa a fabricanete para criar objetos 
fabrica_transporte = FabricaTransporte()
caminhao = fabrica_transporte.criar_transporte("Caminhao")
navio = fabrica_transporte.criar_transporte("Navio")

#chama o metodo dos objetos de transporte criado 
print(caminhao.entregar("ABC123"))
print(navio.entregar("XYZ789"))
             
             