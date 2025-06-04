from domain.cancion.cancion import Cancion
from application.cancion.cancion_service import CancionService
from adapters.cancion.cancion_adapters import CancionAdapter

def main():
    cancion_adapter = CancionAdapter()
    
    cancion_service = CancionService(cancion_adapter)
    
    canciones = cancion_service.get_all_canciones()
    for Cancion in canciones:
        print(f"ID Cancion: {Cancion.id_cancion}, Titulo: {Cancion.titulo}, Autor: {Cancion.autor}")

if __name__ == "__main__":
    main()