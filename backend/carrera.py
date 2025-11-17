import fastf1
import pandas as pd
import datetime

year = datetime.datetime.now().year
ronda = 21


def explorar_datos_carrera(round=ronda, year=year):
    """Explorar todas las columnas y datos disponibles"""
    carrera = fastf1.get_session(year, round, 'R')
    carrera.load()
    resultados = carrera.results
    
    print("=" * 80)
    print("COLUMNAS DISPONIBLES:")
    print("=" * 80)
    print(resultados.columns.tolist())
    print("\n")
    
    print("=" * 80)
    print("INFORMACIÓN DEL DATAFRAME:")
    print("=" * 80)
    print(resultados.info())
    print("\n")
    
    print("=" * 80)
    print("PRIMERAS 5 FILAS COMPLETAS:")
    print("=" * 80)
    # Mostrar todas las columnas sin truncar
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    print(resultados.head())
    print("\n")
    
    print("=" * 80)
    print("EJEMPLO DE DATOS DE UN PILOTO:")
    print("=" * 80)
    primer_piloto = resultados.iloc[0]
    for columna, valor in primer_piloto.items():
        print(f"{columna}: {valor}")
    print("\n")
    
    return resultados


def resultados_carrera(round=ronda, year=year):
    """Obtener resultados formateados de la carrera"""
    carrera = fastf1.get_session(year, round, 'R')
    carrera.load()
    resultados = carrera.results
    
    resultados_pilotos = []
    
    for index, fila in resultados.iterrows():
        piloto = fila['Abbreviation']
        posicion = fila['Position']
        tiempo = fila['Time']
        status = fila['Status']
        
        # Formatear el tiempo según el caso
        if pd.notna(tiempo):
            total_seconds = tiempo.total_seconds()
            
            if posicion == 1:
                minutes = int(total_seconds // 60)
                seconds = total_seconds % 60
                tiempo_str = f"{minutes}:{seconds:06.3f}"
            else:
                tiempo_str = f"+{total_seconds:.3f}"
        else:
            if 'Lap' in str(status):
                tiempo_str = status
            else:
                tiempo_str = status
        
        resultados_pilotos.append({
            'posicion': int(posicion) if pd.notna(posicion) else None,
            'piloto': piloto,
            'nombre_completo': fila['FullName'],
            'equipo': fila['TeamName'],
            'diferencia_lider': tiempo_str,
            'puntos': fila['Points'],
            'grid': fila['GridPosition'],
            'status': status
        })
    
    resultados_pilotos = sorted(resultados_pilotos, key=lambda x: x['posicion'] if x['posicion'] else 999)
    
    return resultados_pilotos


if __name__ == "__main__":
    # Descomentar esta línea para explorar todos los datos:
    # explorar_datos_carrera(ronda, year)
    
    # Resultados formateados
    resultados = resultados_carrera(ronda, year)
    
    print("\n" + "=" * 80)
    print("RESULTADOS DE LA CARRERA:")
    print("=" * 80)
    for resultado in resultados:
        print(f"P{resultado['posicion']}: {resultado['piloto']} ({resultado['equipo']}) - "
              f"Tiempo: {resultado['diferencia_lider']} - "
              f"Grid: {resultado['grid']} - "
              f"Puntos: {resultado['puntos']}")