import requests
import fastf1

from matplotlib import pyplot as plt

import fastf1
import fastf1.plotting


BASE = "https://api.jolpi.ca/ergast/f1/"


def Winner_Last_Race():
    url = f"{BASE}2025/last/results.json"
    r = requests.get(url)
    data = r.json()
    Nombre_ganador = data["MRData"]["RaceTable"]["Races"][0]["Results"][0]["Driver"]["givenName"]
    Apellido_ganador = data["MRData"]["RaceTable"]["Races"][0]["Results"][0]["Driver"]["familyName"]
    Ganador = f"{Nombre_ganador} {Apellido_ganador}"
    #Evento = data("MRData")("RaceTable")("Races")[0]  # Obtener el último gran premio
    # Obtener el ganador de la carrera
    return print(f"Ganador del ultimo gran Premio: {Ganador}")


def Search_Position_Driver_last_Race(driver_name, abreviation == 0):
    """Buscar la posición de un piloto en la última carrera.
    Args:
    driver_name (str): Nombre completo del piloto (ejemplo: "Max Verstappen").
    abreviation (int): Si es 1, devuelve la abreviatura del piloto.
    Returns:
    str: Posición del piloto o mensaje si no participó."""
    url = f"{BASE}2025/last/results.json"
    r = requests.get(url)
    data = r.json()
    
    results = data["MRData"]["RaceTable"]["Races"][0]["Results"]
    
    # Buscar el piloto en los resultados
    for i, result in enumerate(results):
        driver_full_name = f"{result['Driver']['givenName']}  {result['Driver']['familyName']}"
        driver_abreviation = result['Driver']['code']

        if driver_full_name == driver_name:
            posicion = result["position"]
            return print(f"{driver_name} finalizó en la posición: {posicion}")
        if abreviation == 1:
            return driver_abreviation

    # Si no se encuentra el piloto
    return print(f"{driver_name} no participó en la última carrera.")

def strategy_driver(driver_name, year, round, session_type):
    """Obtener y mostrar la estrategia de neumáticos de un piloto en una carrera específica.
    Args:
    driver_name (str): Nombre completo del piloto (ejemplo: "Max Verstappen").
    year (int): Año de la carrera."""
    url = f"{BASE}2025/last/results.json"
    r = requests.get(url)
    data = r.json()
    results = data["MRData"]["RaceTable"]["Races"][0]["Results"]
    driver = Search_Position_Driver_last_Race(driver_name,1)
    session = fastf1.get_session(2025, "Canada", 'R')
    session.load()
    laps = session.laps
    driver = session.get_driver(driver)["Abbreviation"]
    stints = laps[["Driver", "Stint", "Compound", "LapNumber"]]
    stints = stints.groupby(["Driver", "Stint", "Compound"])
    stints = stints.count().reset_index()
    stints = stints.rename(columns={"LapNumber": "StintLength"})
    print(stints)


   

    #Buscar el piloto y su estrategia


    
    #id_driver =
    #if Driver == driver_name:
    #position = data["MRData"]["RaceTable"]["Races"][0]["Results"][0]["position"]
    #    for i in position in data["MRData"]["RaceTable"]["Races"][0]["Results"][i]
            
        
        
    #    return print(f"{driver_name} finalizo en la posicion: {position}")
    #else:
    #    return print(f"{driver_name} did not participate in the last race.")
    


#def get_driver_standings():
#    url = f"{BASE}current/driverStandings.json"
#    r = requests.get(url)
#    data = r.json()
#    return data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]

#standings = get_driver_standings()
#for d in standings:
#    print(d["Driver"]["givenName"], d["Driver"]["familyName"], d["points"])

if __name__ == "__main__":
         
    Winner_Last_Race()

    print("-----")
    print("¿Quieres saber la posicion de un piloto en la ultima carrera?")
    piloto = input("Introduce el nombre completo del piloto (Ejemplo: Max Verstappen): ")
    Search_Position_Driver_last_Race(piloto,0)
    strategy_driver()


    #clasificacion_pilotos = get_driver_standings()

    #print(f"Driver Standings: {clasificacion_pilotos}")

pass