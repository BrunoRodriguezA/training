from .snack import Snack

class Inventario:
    
    def __init__(self):
        self._lista_items = []
        
    
    # coleccion-like 
    def __len__(self) -> int:
        return len(self._lista_items)
    
    def __iter__(self):
        return iter(self._lista_items)

    def __contains__(self, snack: Snack) -> bool:
        return snack in self._lista_items    
    
    def agregar(self, snack:Snack) :
        self._lista_items.append(snack)
        
    def eliminar(self, id_snack):
        for snack in self._lista_items:
            if snack.id_snack == id_snack:
                self._lista_items.remove(snack)
                return  snack
                
    def buscar_por_nombre(self, substr):
        substr = substr.lower()
        return [sn for sn in self._lista_items if substr in sn.nombre.lower()]
        
    
    def total_items(self):
        return len(self._lista_items)
    
    def total_valor(self):
        total_valor = 0
        return sum(sn.precio for sn in self._lista_items)
        

    

if __name__ == "__main__":
    inv = Inventario()
    
    s1 = Snack('patatas', 1)
    s2 = Snack('refresco', 5)
    s3 = Snack('chocolate', .5)
    

    for s in (s1,s2,s3):
        inv.agregar(s)
    
    assert inv.total_items() == 3
    assert inv.total_valor() == sum([s.precio for s in (s1, s2, s3)])
    assert [sn.nombre for sn in inv.buscar_por_nombre("cho")] == ["chocolate"]

    # print(len(inv))
    # for s in inv:
    #     print(s)
    