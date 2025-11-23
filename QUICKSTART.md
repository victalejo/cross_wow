# 🚀 Guía de Inicio Rápido - Cross WOW v2.0

Esta guía te ayudará a configurar y ejecutar el bot de trading en menos de 5 minutos.

---

## ⚡ Pasos Rápidos

### 1️⃣ Instalar Dependencias

```powershell
# Instalar NumPy
pip install numpy

# Instalar TA-Lib (Windows)
# Descarga el wheel desde: https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
# Ejemplo para Python 3.11, 64-bit:
pip install TA_Lib-0.4.28-cp311-cp311-win_amd64.whl
```

### 2️⃣ Configurar Credenciales

Edita `main.py` en la línea 179:

```python
VIC = IQ_Option("tu_email@ejemplo.com", "tu_contraseña")
```

### 3️⃣ Probar Indicadores (Opcional)

```powershell
python test_indicators.py
```

Deberías ver algo como:
```
🧪 Probando indicadores técnicos...
✓ SMA(20): $100.2345
✓ EMA(5): $100.1234
✓ RSI(14): 45.67
...
✅ Todos los indicadores calculados correctamente!
```

### 4️⃣ Ejecutar el Bot

```powershell
python main.py
```

### 5️⃣ Ingresar Parámetros

Cuando se ejecute, te pedirá:

```
REAL O PRACTICA: PRACTICE
Activo: EURUSD
Balance: 1000
numero de tiradas: 20
posibles ganados: 14
```

**Recomendaciones iniciales:**
- Tipo de cuenta: `PRACTICE` (para probar)
- Activo: `EURUSD` (el más líquido)
- Balance: `1000` (balance disponible)
- Número de tiradas: `20` (total de operaciones)
- Posibles ganados: `14` (70% de 20 = objetivo realista)

---

## 📊 ¿Qué Esperar?

Durante la ejecución verás:

```
=== INICIO DE SESIÓN ===
Activo: EURUSD | Balance: $1000 | Objetivo: 14/20 operaciones

--- Operación 1/20 ---
Balance actual: $1000.00
📈 SEÑAL CALL CONFIRMADA
CALL - Inversión: $50.00 | RSI: 45.2 | ADX: 32.5 | ATR: 0.0015
✓ GANADA - Ganancia: $42.50
📊 Winrate: 100.0% (1W/0L)

--- Operación 2/20 ---
...
```

Al finalizar:

```
=== RESUMEN DE SESIÓN ===
Balance inicial: $1000.00
Balance final: $1450.00
Ganancia/Pérdida: $450.00 (45.00%)
Total operaciones: 20
Ganadas: 14 | Perdidas: 6
Winrate: 70.0%
Mejor racha ganadora: 5
Peor racha perdedora: 2
```

---

## 📁 Archivos Generados

Después de ejecutar, encontrarás:

- **`trading_log.txt`**: Log detallado de todas las operaciones
- **`estadisticas.json`**: Estadísticas de la sesión en formato JSON

---

## ⚙️ Personalización Rápida

### Cambiar Límite de Riesgo

En `main.py`, función `logica()`, línea ~120:

```python
# Cambiar de 5% a 3% del balance por operación
if proxima_inversion > balance_actual * 0.03:  # Era 0.05
```

### Cambiar Pausas por Pérdidas

En `main.py`, cuando llamas a `logica()`, línea ~179:

```python
# Cambiar de 3 a 5 pérdidas consecutivas
logica(VIC, activo, velas_q, posibles_ganados, profit, 
       operaciones_totales, balance, max_perdidas_consecutivas=5)
```

### Ajustar Umbrales de Indicadores

En las funciones `validar_senal_call()` y `validar_senal_put()`:

```python
# Línea ~60: Hacer RSI más restrictivo
rsi_valido = 35 < indicadores['rsi'] < 65  # Era 30-70

# Línea ~65: Requerir tendencia más fuerte
tendencia_fuerte = indicadores['adx'] > 30  # Era 25
```

---

## 🛡️ Seguridad

### Protecciones Automáticas Activas

✅ **Límite por operación**: Máximo 5% del balance  
✅ **Pausa tras pérdidas**: 5 minutos después de 3 pérdidas consecutivas  
✅ **Validación multi-indicador**: 5 confirmaciones antes de operar  
✅ **Filtro de volatilidad**: No opera si ATR > 2% del precio  

---

## 🆘 Solución de Problemas

### Error: "No module named 'talib'"

**Solución:**
```powershell
# Descarga el wheel correcto para tu versión de Python
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
pip install TA_Lib-0.4.XX-cpXX-cpXXm-win_amd64.whl
```

### Error: "Can't connect to IQ Option"

**Solución:**
- Verifica tus credenciales en `main.py`
- Comprueba tu conexión a Internet
- Asegúrate de que tu cuenta IQ Option esté activa

### El bot no opera (sin señales)

**Causas comunes:**
- Condiciones de mercado no favorables (lateral, baja volatilidad)
- Umbrales muy restrictivos (ADX < 25, RSI fuera de rango)
- Horario de mercado cerrado

**Solución:**
- Espera a horarios de mayor actividad (sesión europea/americana)
- Ajusta umbrales en las funciones de validación
- Prueba con otro activo más volátil

### Muchas pérdidas consecutivas

**Solución:**
- El bot pausará automáticamente tras 3 pérdidas
- Considera ajustar parámetros de validación
- Prueba con cuenta PRACTICE primero
- Revisa `trading_log.txt` para identificar patrones

---

## 📖 Más Información

- **Documentación completa**: [MEJORAS_ESTRATEGIA.md](MEJORAS_ESTRATEGIA.md)
- **Changelog**: [CHANGELOG.md](CHANGELOG.md)
- **README principal**: [README.md](README.md)
- **Configuración avanzada**: [config_example.py](config_example.py)

---

## 🎯 Consejos para Mejores Resultados

1. **Siempre prueba en PRACTICE primero** (mínimo 100 operaciones)
2. **Opera durante horarios de alta liquidez** (8:00-17:00 UTC)
3. **Empieza con pares mayores** (EURUSD, GBPUSD, USDJPY)
4. **Monitorea el winrate**: Objetivo mínimo 60%
5. **Revisa los logs regularmente** para identificar patrones
6. **No modifiques parámetros durante una sesión activa**
7. **Establece límites diarios** de pérdida máxima
8. **Mantén un registro histórico** de tus sesiones

---

## ⚠️ Recordatorio Importante

Este bot es para **fines educativos**. El trading conlleva riesgos:

- ❌ No inviertas dinero que no puedas perder
- ❌ No confíes ciegamente en el bot
- ❌ No operes bajo presión emocional
- ✅ Usa cuenta PRACTICE extensivamente
- ✅ Entiende cómo funciona cada indicador
- ✅ Mantén registros y analiza resultados

---

## 🤝 Soporte

¿Problemas? ¿Preguntas?

- **Email**: valejoapps@gmail.com
- **Issues**: [GitHub Issues](https://github.com/victalejo/cross_wow/issues)

---

**¡Buena suerte y opera responsablemente! 🚀📈**

---

Última actualización: 23 de noviembre de 2025  
Versión: 2.0
