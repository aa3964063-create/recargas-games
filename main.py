import time

def consultar_nombre_ff(player_id):
    print(f"\n[SISTEMA]: Conectando con servidores de Garena...")
    time.sleep(1) # Simula el tiempo de carga
    
    # Lista de IDs de prueba (puedes añadir más)
    # En una API real, esto consultaría una base de datos externa
    base_datos_simulada = {
        "12345678": "Elite_Killer",
        "87654321": "GarenaMaster",
        "11223344": "DiamantePura",
        "55667788": "Donato_Fan"
    }

    print(f"[SISTEMA]: Buscando nombre para el ID: {player_id}...")
    time.sleep(1)

    if player_id in base_datos_simulada:
        return {
            "status": "success",
            "nombre": base_datos_simulada[player_id],
            "mensaje": "ID Verificado ✅"
        }
    else:
        return {
            "status": "error",
            "mensaje": "ID no encontrado en la región actual ❌"
        }

# --- PRUEBA INTERACTIVA ---
print("--- VERIFICADOR DE NOMBRES FREE FIRE ---")
id_usuario = input("Introduce el ID del jugador: ")

resultado = consultar_nombre_ff(id_usuario)

if resultado["status"] == "success":
    print(f"\n[RESULTADO]: {resultado['mensaje']}")
    print(f"Nombre del Jugador: {resultado['nombre']}")
else:
    print(f"\n[ERROR]: {resultado['mensaje']}")
