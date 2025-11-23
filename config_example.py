"""
Configuración de parámetros para el bot de trading Cross WOW

Copia este archivo como 'config.py' y ajusta los valores según tus necesidades.
IMPORTANTE: No subas 'config.py' a GitHub (ya está en .gitignore)
"""

# ========== CREDENCIALES IQ OPTION ==========
# IMPORTANTE: Cambia estos valores por los tuyos
EMAIL = "tu_email@ejemplo.com"
PASSWORD = "tu_contraseña"

# ========== PARÁMETROS DE TRADING ==========

# Tipo de cuenta: "PRACTICE" o "REAL"
ACCOUNT_TYPE = "PRACTICE"

# Activo a operar (ejemplos: "EURUSD", "GBPUSD", "USDJPY", etc.)
ASSET = "EURUSD"

# Balance inicial
INITIAL_BALANCE = 1000

# Número total de operaciones planificadas
TOTAL_OPERATIONS = 20

# Número de operaciones ganadoras objetivo (Masaniello)
# Recomendación: 60-70% del total de operaciones
TARGET_WINS = 14

# Expiración en minutos (para opciones binarias)
EXPIRATION_MINUTES = 1

# ========== INDICADORES TÉCNICOS ==========

# Número de velas para análisis
CANDLES_COUNT = 100

# Periodos de las medias móviles
SMA_PERIOD = 20  # Media Móvil Simple
EMA_PERIOD = 5   # Media Móvil Exponencial

# Periodo del RSI (Relative Strength Index)
RSI_PERIOD = 14

# Periodo del ADX (Average Directional Index)
ADX_PERIOD = 14

# Periodo del ATR (Average True Range)
ATR_PERIOD = 14

# Bandas de Bollinger
BB_PERIOD = 20
BB_DEVIATIONS = 2

# ========== VALIDACIÓN DE SEÑALES ==========

# Rango válido de RSI (evita sobrecompra/sobreventa)
RSI_MIN = 30
RSI_MAX = 70

# Umbral mínimo de ADX para considerar tendencia fuerte
ADX_THRESHOLD = 25

# Multiplicador de ATR para volatilidad máxima permitida
# 0.02 = 2% del precio actual
ATR_VOLATILITY_MAX = 0.02

# ========== GESTIÓN DE RIESGO ==========

# Porcentaje máximo del balance a arriesgar por operación
MAX_RISK_PERCENT = 0.05  # 5% del balance

# Número máximo de pérdidas consecutivas antes de pausar
MAX_CONSECUTIVE_LOSSES = 3

# Tiempo de pausa tras pérdidas consecutivas (en segundos)
PAUSE_DURATION = 300  # 5 minutos

# Tiempo de espera cuando no hay señal válida (en segundos)
WAIT_TIME_NO_SIGNAL = 30  # 30 segundos

# ========== LOGGING ==========

# Nivel de logging: "DEBUG", "INFO", "WARNING", "ERROR"
LOG_LEVEL = "INFO"

# Archivo de log
LOG_FILE = "trading_log.txt"

# Archivo de estadísticas
STATS_FILE = "estadisticas.json"

# ========== AVANZADO ==========

# Habilitar reinicio automático al alcanzar objetivo
AUTO_RESTART = True

# Habilitar notificaciones de consola con colores
ENABLE_CONSOLE_COLORS = True

# ========== PRESETS ==========

# Preset conservador (menor riesgo, menos operaciones)
CONSERVATIVE = {
    'MAX_RISK_PERCENT': 0.03,  # 3%
    'MAX_CONSECUTIVE_LOSSES': 2,
    'ADX_THRESHOLD': 30,
    'RSI_MIN': 35,
    'RSI_MAX': 65,
}

# Preset moderado (balance entre riesgo y oportunidades)
MODERATE = {
    'MAX_RISK_PERCENT': 0.05,  # 5%
    'MAX_CONSECUTIVE_LOSSES': 3,
    'ADX_THRESHOLD': 25,
    'RSI_MIN': 30,
    'RSI_MAX': 70,
}

# Preset agresivo (mayor riesgo, más operaciones)
AGGRESSIVE = {
    'MAX_RISK_PERCENT': 0.08,  # 8%
    'MAX_CONSECUTIVE_LOSSES': 4,
    'ADX_THRESHOLD': 20,
    'RSI_MIN': 25,
    'RSI_MAX': 75,
}

# Preset activo (usa: CONSERVATIVE, MODERATE, o AGGRESSIVE)
# Puedes descomentar para aplicar un preset:
# ACTIVE_PRESET = CONSERVATIVE
# ACTIVE_PRESET = MODERATE
# ACTIVE_PRESET = AGGRESSIVE
