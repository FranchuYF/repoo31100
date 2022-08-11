import datetime

fechaActual= datetime.datetime.now()

fechaPasada = datetime.datetime(2023, 5, 19)
diferencia = fechaPasada - fechaActual
print(diferencia.total_seconds())

