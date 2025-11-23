import time
from datetime import datetime
import logging
import json

from iqoptionapi.stable_api import IQ_Option
import masaniello as ms
from talib import EMA, SMA, RSI, ADX, ATR, BBANDS
import numpy as np

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('trading_log.txt'),
        logging.StreamHandler()
    ]
)

def analisis(VIC, activo, velas_q):
    """Análisis técnico completo con múltiples indicadores"""
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

    # Medias móviles
    sma20 = SMA(dados_f['close'], timeperiod=20)
    ema5 = EMA(dados_f['close'], timeperiod=5)
    
    # RSI para detectar sobrecompra/sobreventa
    rsi = RSI(dados_f['close'], timeperiod=14)
    
    # ADX para fuerza de tendencia
    adx = ADX(dados_f['high'], dados_f['low'], dados_f['close'], timeperiod=14)
    
    # ATR para volatilidad
    atr = ATR(dados_f['high'], dados_f['low'], dados_f['close'], timeperiod=14)
    
    # Bandas de Bollinger para volatilidad y rango
    upper, middle, lower = BBANDS(dados_f['close'], timeperiod=20, nbdevup=2, nbdevdn=2)

    return {
        'sma20_1': round(sma20[-1], 5),
        'sma20_2': round(sma20[-2], 5),
        'ema5_1': round(ema5[-1], 5),
        'ema5_2': round(ema5[-2], 5),
        'rsi': round(rsi[-1], 2),
        'adx': round(adx[-1], 2),
        'atr': round(atr[-1], 5),
        'bb_upper': round(upper[-1], 5),
        'bb_middle': round(middle[-1], 5),
        'bb_lower': round(lower[-1], 5),
        'close': round(dados_f['close'][-1], 5)
    }

def mariano(profit, VIC, posibles_ganados, operaciones_totales, balance):
    app = ms.masanielloSH(int(profit), balance)
    matriz = app.EntryDataMasanielloFutureInvesment(
        app.Matrix(posibles_ganados, operaciones_totales))
    return matriz, app

def validar_senal_call(indicadores):
    """Validación avanzada para señal CALL con múltiples confirmaciones"""
    # Cruce de EMAs (señal principal)
    cruce_alcista = indicadores['ema5_1'] > indicadores['sma20_1']
    
    # RSI no debe estar en sobrecompra (evitar entrar en picos)
    rsi_valido = 30 < indicadores['rsi'] < 70
    
    # ADX debe indicar tendencia fuerte (> 25)
    tendencia_fuerte = indicadores['adx'] > 25
    
    # Precio debe estar por encima de la banda media de Bollinger
    precio_tendencia = indicadores['close'] > indicadores['bb_middle']
    
    # Volatilidad adecuada (ATR no extremadamente alta)
    volatilidad_normal = indicadores['atr'] < indicadores['close'] * 0.02  # 2% del precio
    
    return cruce_alcista and rsi_valido and tendencia_fuerte and precio_tendencia and volatilidad_normal

def validar_senal_put(indicadores):
    """Validación avanzada para señal PUT con múltiples confirmaciones"""
    # Cruce de EMAs (señal principal)
    cruce_bajista = indicadores['ema5_1'] < indicadores['sma20_1']
    
    # RSI no debe estar en sobreventa (evitar entrar en caídas extremas)
    rsi_valido = 30 < indicadores['rsi'] < 70
    
    # ADX debe indicar tendencia fuerte (> 25)
    tendencia_fuerte = indicadores['adx'] > 25
    
    # Precio debe estar por debajo de la banda media de Bollinger
    precio_tendencia = indicadores['close'] < indicadores['bb_middle']
    
    # Volatilidad adecuada (ATR no extremadamente alta)
    volatilidad_normal = indicadores['atr'] < indicadores['close'] * 0.02  # 2% del precio
    
    return cruce_bajista and rsi_valido and tendencia_fuerte and precio_tendencia and volatilidad_normal

def compra(proxima_inversion, VIC, activo, indicadores):
    """Ejecuta una operación CALL con logging"""
    logging.info(f"CALL - Inversión: ${proxima_inversion:.2f} | RSI: {indicadores['rsi']} | ADX: {indicadores['adx']} | ATR: {indicadores['atr']}")
    check, id = VIC.buy(proxima_inversion, activo, "call", 1)
    gan = VIC.check_win_v3(id)
    if gan > 0:
        wl = "w"
        logging.info(f"✓ GANADA - Ganancia: ${gan:.2f}")
    else:
        wl = "l"
        logging.info(f"✗ PERDIDA - Pérdida: ${abs(gan):.2f}")
    return wl

def venta(proxima_inversion, VIC, activo, indicadores):
    """Ejecuta una operación PUT con logging"""
    logging.info(f"PUT - Inversión: ${proxima_inversion:.2f} | RSI: {indicadores['rsi']} | ADX: {indicadores['adx']} | ATR: {indicadores['atr']}")
    check, id = VIC.buy(proxima_inversion, activo, "put", 1)
    gan = VIC.check_win_v3(id)
    if gan > 0:
        wl = "w"
        logging.info(f"✓ GANADA - Ganancia: ${gan:.2f}")
    else:
        wl = "l"
        logging.info(f"✗ PERDIDA - Pérdida: ${abs(gan):.2f}")
    return wl

def logica(VIC, activo, velas_q, posibles_ganados, profit, operaciones_totales, balance, max_perdidas_consecutivas=3):
    """Lógica mejorada con gestión de riesgo y estadísticas"""
    operaciones = 0
    ganados = 0
    perdidos = 0
    perdidas_consecutivas = 0
    estadisticas = {
        'total_operaciones': 0,
        'ganadas': 0,
        'perdidas': 0,
        'racha_ganadora': 0,
        'racha_perdedora': 0,
        'mejor_racha': 0,
        'peor_racha': 0
    }
    
    matriz, app = mariano(profit, VIC, posibles_ganados, operaciones_totales, balance)
    logging.info(f"=== INICIO DE SESIÓN ===")
    logging.info(f"Activo: {activo} | Balance: ${balance} | Objetivo: {posibles_ganados}/{operaciones_totales} operaciones")
    
    while operaciones < operaciones_totales:
        # Protección contra pérdidas consecutivas excesivas
        if perdidas_consecutivas >= max_perdidas_consecutivas:
            logging.warning(f"⚠ PAUSA: {perdidas_consecutivas} pérdidas consecutivas. Esperando mejores condiciones...")
            time.sleep(300)  # Esperar 5 minutos
            perdidas_consecutivas = 0
            continue
        
        indicadores = analisis(VIC, activo, velas_q)
        proxima_inversion = app.ExecuteInvestment(matrizResult=matriz)
        
        # Validar que la inversión no exceda el 5% del balance actual
        balance_actual = app.ReesomerCasaTotal()
        if proxima_inversion > balance_actual * 0.05:
            logging.warning(f"⚠ Inversión ajustada de ${proxima_inversion:.2f} a ${balance_actual * 0.05:.2f} (5% del balance)")
            proxima_inversion = balance_actual * 0.05
        
        logging.info(f"\n--- Operación {operaciones + 1}/{operaciones_totales} ---")
        logging.info(f"Balance actual: ${balance_actual:.2f}")
        
        # Señal CALL con validaciones mejoradas
        if validar_senal_call(indicadores):
            logging.info("📈 SEÑAL CALL CONFIRMADA")
            wl = compra(proxima_inversion, VIC, activo, indicadores)
            
            if wl == "w":
                ganados += 1
                estadisticas['ganadas'] += 1
                estadisticas['racha_ganadora'] += 1
                estadisticas['racha_perdedora'] = 0
                perdidas_consecutivas = 0
                if estadisticas['racha_ganadora'] > estadisticas['mejor_racha']:
                    estadisticas['mejor_racha'] = estadisticas['racha_ganadora']
            else:
                perdidos += 1
                estadisticas['perdidas'] += 1
                estadisticas['racha_perdedora'] += 1
                estadisticas['racha_ganadora'] = 0
                perdidas_consecutivas += 1
                if estadisticas['racha_perdedora'] > estadisticas['peor_racha']:
                    estadisticas['peor_racha'] = estadisticas['racha_perdedora']
            
            operaciones += 1
            estadisticas['total_operaciones'] += 1
            app.ExecuteMasaniello(WL_input=wl, wind=posibles_ganados)
            
            # Mostrar estadísticas actualizadas
            winrate = (estadisticas['ganadas'] / estadisticas['total_operaciones']) * 100
            logging.info(f"📊 Winrate: {winrate:.1f}% ({estadisticas['ganadas']}W/{estadisticas['perdidas']}L)")
            
            if ganados == posibles_ganados:
                logging.info("🎯 ¡OBJETIVO ALCANZADO!")
                break
                
        # Señal PUT con validaciones mejoradas
        elif validar_senal_put(indicadores):
            logging.info("📉 SEÑAL PUT CONFIRMADA")
            wl = venta(proxima_inversion, VIC, activo, indicadores)
            
            if wl == "w":
                ganados += 1
                estadisticas['ganadas'] += 1
                estadisticas['racha_ganadora'] += 1
                estadisticas['racha_perdedora'] = 0
                perdidas_consecutivas = 0
                if estadisticas['racha_ganadora'] > estadisticas['mejor_racha']:
                    estadisticas['mejor_racha'] = estadisticas['racha_ganadora']
            else:
                perdidos += 1
                estadisticas['perdidas'] += 1
                estadisticas['racha_perdedora'] += 1
                estadisticas['racha_ganadora'] = 0
                perdidas_consecutivas += 1
                if estadisticas['racha_perdedora'] > estadisticas['peor_racha']:
                    estadisticas['peor_racha'] = estadisticas['racha_perdedora']
            
            operaciones += 1
            estadisticas['total_operaciones'] += 1
            app.ExecuteMasaniello(WL_input=wl, wind=posibles_ganados)
            
            # Mostrar estadísticas actualizadas
            winrate = (estadisticas['ganadas'] / estadisticas['total_operaciones']) * 100
            logging.info(f"📊 Winrate: {winrate:.1f}% ({estadisticas['ganadas']}W/{estadisticas['perdidas']}L)")
            
            if ganados == posibles_ganados:
                logging.info("🎯 ¡OBJETIVO ALCANZADO!")
                break
        else:
            logging.debug("❌ Sin señal válida, esperando...")
            time.sleep(30)  # Esperar 30 segundos antes de revisar de nuevo
    
    # Resumen final de la sesión
    balance_final = app.ReesomerCasaTotal()
    ganancia_total = balance_final - balance
    logging.info(f"\n{'='*60}")
    logging.info(f"=== RESUMEN DE SESIÓN ===")
    logging.info(f"Balance inicial: ${balance:.2f}")
    logging.info(f"Balance final: ${balance_final:.2f}")
    logging.info(f"Ganancia/Pérdida: ${ganancia_total:.2f} ({(ganancia_total/balance)*100:.2f}%)")
    logging.info(f"Total operaciones: {estadisticas['total_operaciones']}")
    logging.info(f"Ganadas: {estadisticas['ganadas']} | Perdidas: {estadisticas['perdidas']}")
    if estadisticas['total_operaciones'] > 0:
        logging.info(f"Winrate: {(estadisticas['ganadas']/estadisticas['total_operaciones'])*100:.1f}%")
    logging.info(f"Mejor racha ganadora: {estadisticas['mejor_racha']}")
    logging.info(f"Peor racha perdedora: {estadisticas['peor_racha']}")
    logging.info(f"{'='*60}\n")
    
    # Guardar estadísticas en archivo JSON
    with open('estadisticas.json', 'w') as f:
        json.dump({
            'fecha': datetime.now().isoformat(),
            'activo': activo,
            'balance_inicial': balance,
            'balance_final': balance_final,
            'ganancia': ganancia_total,
            'estadisticas': estadisticas
        }, f, indent=4)
    
    if ganados == posibles_ganados:
        print("\n🎉 ¡Lo has logrado! Reiniciando sesión...\n")
        logica(VIC, activo, velas_q, posibles_ganados, profit, operaciones_totales, balance_final, max_perdidas_consecutivas)
    else:
        logging.info("Sesión finalizada sin alcanzar el objetivo.")


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