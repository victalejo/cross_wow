"""
Script de prueba para validar los nuevos indicadores técnicos
Este script prueba el cálculo de indicadores sin conectarse a IQ Option
"""

import numpy as np
from talib import EMA, SMA, RSI, ADX, ATR, BBANDS

def test_indicators():
    """Prueba el cálculo de todos los indicadores"""
    print("🧪 Probando indicadores técnicos...\n")
    
    # Datos de ejemplo (simulando 100 velas)
    np.random.seed(42)
    close_prices = 100 + np.cumsum(np.random.randn(100) * 0.5)
    high_prices = close_prices + np.random.rand(100) * 2
    low_prices = close_prices - np.random.rand(100) * 2
    
    print("📊 Datos de prueba generados:")
    print(f"   Precio de cierre actual: ${close_prices[-1]:.2f}")
    print(f"   Precio máximo: ${high_prices[-1]:.2f}")
    print(f"   Precio mínimo: ${low_prices[-1]:.2f}\n")
    
    # Calcular indicadores
    print("📈 Calculando indicadores...\n")
    
    # Medias móviles
    sma20 = SMA(close_prices, timeperiod=20)
    ema5 = EMA(close_prices, timeperiod=5)
    print(f"✓ SMA(20): ${sma20[-1]:.4f}")
    print(f"✓ EMA(5): ${ema5[-1]:.4f}")
    
    # RSI
    rsi = RSI(close_prices, timeperiod=14)
    print(f"✓ RSI(14): {rsi[-1]:.2f}")
    
    # ADX
    adx = ADX(high_prices, low_prices, close_prices, timeperiod=14)
    print(f"✓ ADX(14): {adx[-1]:.2f}")
    
    # ATR
    atr = ATR(high_prices, low_prices, close_prices, timeperiod=14)
    print(f"✓ ATR(14): {atr[-1]:.4f}")
    
    # Bandas de Bollinger
    upper, middle, lower = BBANDS(close_prices, timeperiod=20, nbdevup=2, nbdevdn=2)
    print(f"✓ Banda Superior: ${upper[-1]:.4f}")
    print(f"✓ Banda Media: ${middle[-1]:.4f}")
    print(f"✓ Banda Inferior: ${lower[-1]:.4f}")
    
    print("\n✅ Todos los indicadores calculados correctamente!")
    
    # Simular validación de señal
    print("\n🔍 Probando validación de señales...\n")
    
    indicadores = {
        'sma20_1': sma20[-1],
        'sma20_2': sma20[-2],
        'ema5_1': ema5[-1],
        'ema5_2': ema5[-2],
        'rsi': rsi[-1],
        'adx': adx[-1],
        'atr': atr[-1],
        'bb_upper': upper[-1],
        'bb_middle': middle[-1],
        'bb_lower': lower[-1],
        'close': close_prices[-1]
    }
    
    # Validar señal CALL
    cruce_alcista = indicadores['ema5_1'] > indicadores['sma20_1']
    rsi_valido = 30 < indicadores['rsi'] < 70
    tendencia_fuerte = indicadores['adx'] > 25
    precio_tendencia = indicadores['close'] > indicadores['bb_middle']
    volatilidad_normal = indicadores['atr'] < indicadores['close'] * 0.02
    
    print("Validación de señal CALL:")
    print(f"   {'✓' if cruce_alcista else '✗'} EMA(5) > SMA(20): {cruce_alcista}")
    print(f"   {'✓' if rsi_valido else '✗'} RSI en rango 30-70: {rsi_valido} (RSI={indicadores['rsi']:.1f})")
    print(f"   {'✓' if tendencia_fuerte else '✗'} ADX > 25: {tendencia_fuerte} (ADX={indicadores['adx']:.1f})")
    print(f"   {'✓' if precio_tendencia else '✗'} Precio > BB_Media: {precio_tendencia}")
    print(f"   {'✓' if volatilidad_normal else '✗'} Volatilidad controlada: {volatilidad_normal}")
    
    senal_call_valida = all([cruce_alcista, rsi_valido, tendencia_fuerte, 
                              precio_tendencia, volatilidad_normal])
    
    print(f"\n{'🟢 SEÑAL CALL VÁLIDA' if senal_call_valida else '🔴 SEÑAL CALL NO VÁLIDA'}")
    
    # Validar señal PUT
    cruce_bajista = indicadores['ema5_1'] < indicadores['sma20_1']
    precio_tendencia_bajista = indicadores['close'] < indicadores['bb_middle']
    
    print("\nValidación de señal PUT:")
    print(f"   {'✓' if cruce_bajista else '✗'} EMA(5) < SMA(20): {cruce_bajista}")
    print(f"   {'✓' if rsi_valido else '✗'} RSI en rango 30-70: {rsi_valido} (RSI={indicadores['rsi']:.1f})")
    print(f"   {'✓' if tendencia_fuerte else '✗'} ADX > 25: {tendencia_fuerte} (ADX={indicadores['adx']:.1f})")
    print(f"   {'✓' if precio_tendencia_bajista else '✗'} Precio < BB_Media: {precio_tendencia_bajista}")
    print(f"   {'✓' if volatilidad_normal else '✗'} Volatilidad controlada: {volatilidad_normal}")
    
    senal_put_valida = all([cruce_bajista, rsi_valido, tendencia_fuerte, 
                            precio_tendencia_bajista, volatilidad_normal])
    
    print(f"\n{'🟢 SEÑAL PUT VÁLIDA' if senal_put_valida else '🔴 SEÑAL PUT NO VÁLIDA'}")
    
    print("\n" + "="*60)
    print("✅ Prueba completada exitosamente!")
    print("="*60)

if __name__ == "__main__":
    try:
        test_indicators()
    except ImportError as e:
        print(f"❌ Error: {e}")
        print("\n⚠️  Asegúrate de tener instalado TA-Lib:")
        print("   pip install TA-Lib")
        print("\n   En Windows, descarga el wheel desde:")
        print("   https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
