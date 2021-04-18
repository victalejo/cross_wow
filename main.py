import time
from datetime import datetime

from iqoptionapi.stable_api import IQ_Option
import masaniello as ms
from talib import EMA, SMA
import numpy as np

VIC = IQ_Option("valejoapps@gmail.com", "Victor18")
VIC.connect()
activo = "EURUSD-OTC"
expiracion = 1
velas_q = 100

while True:

    velas = VIC.get_candles(activo, (int(expiracion) * 60), 10, time.time())

    ultimo = round(velas[0]['close'], 4)
    primeiro = round(velas[-1]['close'], 4)
    # if now.minute == 0 and now.second in se or now.minute == 5 and now.second in se or now.minute == 10 and now.second in se or now.minute == 15 and now.second in se or now.minute == 20 and now.second in se or now.minute == 25 and now.second in se or now.minute == 30 and now.second in se or now.minute == 35 and now.second in se or now.minute == 40 and now.second in se or now.minute == 45 and now.second in se or now.minute == 50 and now.second in se or now.minute == 55 and now.second in se:

    inicio = time.time()
    # print(inicio)

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

    precio = round(velas[-1]['close'], 5)
    ema201 = round(salida1[-1], 5)
    ema202 = round(salida1[-2], 5)
    ema51 = round(salida2[-1], 5)
    ema52 = round(salida2[-2], 5)

    print("debe ser igual la ema 20 {} y ema 5 {} y mayor o menor la ema 20 {} y la ema 5 {}".format(ema202, ema52, ema201, ema51))
    if ema202 == ema52 and ema51 > ema201:
        VIC.buy(50, activo, "call", 1)
    elif ema202 == ema52 and ema51 < ema201:
        VIC.buy(50, activo, "put", 1)
"""    d = VIC.get_all_profit()

    print('Activo:', activo,
          '| pago:', d,
          '| precio:', precio,
          '| hora:', round(time.time() - inicio, 2), 's',
          '| TVela:', datetime.fromtimestamp(int(velas[-1]['at']) // 1000000000).strftime('%H:%M:%S'),
          'CCI:', cci
          )"""
