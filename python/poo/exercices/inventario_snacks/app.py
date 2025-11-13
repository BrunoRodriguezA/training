from capa_dominio.snack import Snack
from capa_dominio.inventario import Inventario

def main() -> None:
    inv = Inventario()
    
    s1 = Snack('patatas', 1)
    s2 = Snack('refresco', 5)
    s3 = Snack('chocolate', .5)
    

    for s in (s1,s2,s3):
        inv.agregar(s)
        
    print(f"Inventario: {len(inv)} items")
    
    for s in inv:
        print(s)
        
    print("Total €:", inv.total_valor())
    
if __name__ == "__main__":
    main()