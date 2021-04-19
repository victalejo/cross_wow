import time
from datetime import datetime

from iqoptionapi.stable_api import IQ_Option
import masaniello as ms
from talib import EMA, SMA
import numpy as np

def analisis(VIC, activo, velas_q):

    velas = VIC.get_candles(activo, 60, velas_q, time.time())

    dados_f = {
        'open': np.empty(velas_q),
        'high': np.empty(velas_q),
        'low': np.empty(velas_q),
        'close': np.empty(velas_q),
        'volume': np.empty(velas_q)
    }

    for x in range(0, velas_q):
        dados_f['open'][x] = velas[x]['open']
        dados_f['high'][x] = velas[x]['max']
        dados_f['low'][x] = velas[x]['min']
        dados_f['close'][x] = velas[x]['close']
        dados_f['volume'][x] = velas[x]['volume']

    salida1 = SMA(dados_f['close'], timeperiod=20)
    salida2 = EMA(dados_f['close'], timeperiod=5)

    ema201 = round(salida1[-1], 5)
    ema202 = round(salida1[-2], 5)
    ema51 = round(salida2[-1], 5)
    ema52 = round(salida2[-2], 5)

    return ema201, ema202, ema51, ema52

def mariano(profit, VIC, posibles_ganados, operaciones_totales, balance):
    app = ms.masanielloSH(int(profit), balance)
    matriz = app.EntryDataMasanielloFutureInvesment(
        app.Matrix(posibles_ganados, operaciones_totales))
    return matriz, app

def compra(proxima_inversion, VIC, activo):
    check, id = VIC.buy(proxima_inversion, activo, "call", 1)
    gan = VIC.check_win_v3(id)
    if gan > 0:
        wl = "w"
    else:
        wl = "l"
    return wl

def venta(proxima_inversion, VIC, activo):
    check, id = VIC.buy(proxima_inversion, activo, "put", 1)
    gan = VIC.check_win_v3(id)
    if gan > 0:
        wl = "w"
    else:
        wl = "l"
    return wl

def logica(VIC, activo, velas_q, posibles_ganados, profit, operaciones_totales, balance):
    operaciones = 0
    ganados = 0
    matriz, app = mariano(profit, VIC, posibles_ganados, operaciones_totales, balance)
    while True:
        ema201, ema202, ema51, ema52 = analisis(VIC, activo, velas_q)
        proxima_inversion = app.ExecuteInvestment(matrizResult=matriz)
        analisis(VIC, activo, velas_q)
        if ema202 == ema52 and ema51 > ema201:
            wl = compra(proxima_inversion, VIC, activo)
            if wl == "w":
                ganados += 1
            operaciones += 1
            app.ExecuteMasaniello(WL_input=wl, wind=posibles_ganados)
            if ganados == posibles_ganados:
                break
        elif ema202 == ema52 and ema51 < ema201:
            wl = venta(proxima_inversion, VIC, activo)
            if wl == "w":
                ganados += 1
            operaciones += 1
            app.ExecuteMasaniello(WL_input=wl, wind=posibles_ganados)
            if ganados == posibles_ganados:
                break
    print("Lo has logrado, vamos de nuevo...")
    logica(VIC, activo, velas_q, app, posibles_ganados, profit, operaciones_totales)


def main():
    VIC = IQ_Option("valejoapps@gmail.com", "Victor18")
    VIC.connect()
    VIC.change_balance(input("REAL O PRACTICA: "))
    activo = input("Activo: ")
    balance = int(input("Balance: "))
    expiracion = 1
    velas_q = 100
    operaciones_totales = int(input('numero de tiradas: '))
    posibles_ganados = int(input('posibles ganados: '))
    d = VIC.get_all_profit()
    profit = 100 * d[activo]["turbo"]
    logica(VIC, activo, velas_q, posibles_ganados, profit, operaciones_totales, balance)

if __name__ == '__main__':
    main()