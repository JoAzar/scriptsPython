from datetime import datetime
import pytz
rojo = '\033[91m'
verde = '\033[92m'
azul = '\033[94m'
magenta = '\033[95m'
amarillo = '\033[93m'
resetColor = '\033[0m'
blanco = '\033[97m'

if __name__ == '__main__':
    places = ['Asia/Tokyo', 'Europe/Madrid', 'America/Argentina/Buenos_Aires', 'US/eastern', 'US/Pacific', 'UTC']
    cities = ['Tokyo', 'Madrid', 'Buenos Aires', 'New York', 'California', 'UTC']
    for place, cityN in zip(places, cities):
        cityT = datetime.now(pytz.timezone(place))
        stringFormateado = "Fecha en [{cityN} => [{cityT.strftime('%Y/%m/%d | %H:%M | %Z')}]"
        largo = len(stringFormateado)
        marco = (largo-10)*"─"
        print(marco+"\n"+f"Fecha en "+verde+f"[{cityN}] "+resetColor+"=>"+rojo+f" [{cityT.strftime('%Y/%m/%d | %H:%M | %Z')}]"+resetColor)
    print(marco)
