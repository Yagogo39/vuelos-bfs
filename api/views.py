from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import buscar_solucion_BFS, Nodo

# Agrega esta vista al final de tu views.py
@api_view(['GET'])
def lista_ciudades(request):
    conexiones = {
        'Jiloyork': {'Celaya', 'CDMX', 'Queretaro'},
        'Sonora': {'Zacatecas', 'Sinaloa'},
        'Guanajuato': {'Aguascalientes'},
        'Oaxaca': {'Queretaro'},
        'Sinaloa': {'Celaya', 'Sonora', 'Jiloyork'},
        'Queretaro': {'Monterrey'},
        'Celaya': {'Jiloyork', 'Sinaloa'},
        'Zacatecas': {'Sonora', 'Monterrey', 'Queretaro'},
        'Monterrey': {'Zacatecas', 'Sinaloa'},
        'Tamaulipas': {'Queretaro'},
        'Queretaro': {'Tamaulipas', 'Zacatecas', 'Sinaloa', 'Jiloyork', 'Oaxaca'},
        'Aguascalientes': {},
        'CDMX': {}
    }

    ciudades = sorted(list(conexiones.keys()))
    return Response({'ciudades': ciudades})

@api_view(['POST'])
def ruta_vuelo(request):
    conexiones = {
        'Jiloyork': {'Celaya', 'CDMX', 'Queretaro'},
        'Sonora': {'Zacatecas', 'Sinaloa'},
        'Guanajuato': {'Aguascalientes'},
        'Oaxaca': {'Queretaro'},
        'Sinaloa': {'Celaya', 'Sonora', 'Jiloyork'},
        'Queretaro': {'Monterrey'},
        'Celaya': {'Jiloyork', 'Sinaloa'},
        'Zacatecas': {'Sonora', 'Monterrey', 'Queretaro'},
        'Monterrey': {'Zacatecas', 'Sinaloa'},
        'Tamaulipas': {'Queretaro'},
        'Queretaro': {'Tamaulipas', 'Zacatecas', 'Sinaloa', 'Jiloyork', 'Oaxaca'},
        'Aguascalientes': {},
        'CDMX': {}
    }

    origen = request.data.get('origen')
    destino = request.data.get('destino')

    nodo_solucion = buscar_solucion_BFS(conexiones, origen, destino)

    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.reverse()
        return Response({'ruta': resultado})
    
    return Response({'error': 'No se encontro una ruta'})