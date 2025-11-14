import requests
import fastf1


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


def Search_Position_Driver_last_Race(driver_name):
    url = f"{BASE}2025/last/results.json"
    r = requests.get(url)
    data = r.json()
    #Driver = data["MRData"]["RaceTable"]["Races"][0]["Results"][0]["Driver"]["givenName"] + " " + data["MRData"]["RaceTable"]["Races"][0]["Results"][0]["Driver"]["familyName"]
    #position = data["MRData"]["RaceTable"]["Races"][0]["Results"][0]["position"]
    #Fernando_Alonso = data["MRData"]["RaceTable"]["Races"][0]["Results"][13]["Driver"]["driverId"]

    
    Driver = data["MRData"]["RaceTable"]["Races"][0]["Results"][i]["Driver"]["givenName"] + " " + data["MRData"]["RaceTable"]["Races"][0]["Results"][i]["Driver"]["familyName"]
    i=0
    for driver_name in i:
        
        if Driver == driver_name:
            posicion = data["MRData"]["RaceTable"]["Races"][0]["Results"][i]["position"]
    
    return posicion
    

    
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
   # print("¿Quieres saber la posicion de un piloto en la ultima carrera?")
    #piloto = input("Introduce el nombre completo del piloto (Ejemplo: Max Verstappen): ")
    Search_Position_Driver_last_Race("Fernando Alonso")


    #clasificacion_pilotos = get_driver_standings()

    #print(f"Driver Standings: {clasificacion_pilotos}")

pass