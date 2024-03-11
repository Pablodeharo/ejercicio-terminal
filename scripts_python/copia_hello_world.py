from datetime import datetime

fecha_hora_actual = datetime.now()strftime("%y-%m")

with open("outputs/res.txt", "a") as archivo:
	archivo.write(f'Tarea finalizada a las {fecha_hora_actual}')
