# Cross WOW 📈

Bot automatizado de trading para IQ Option que utiliza análisis técnico con indicadores de media móvil (SMA y EMA) combinado con el método de gestión de capital Masaniello.

## 📋 Descripción

Cross WOW es una herramienta de trading automatizado que:

- Conecta con la API de IQ Option para ejecutar operaciones binarias
- Analiza el mercado usando indicadores técnicos (SMA de 20 periodos y EMA de 5 periodos)
- Implementa el sistema de gestión de capital Masaniello para optimizar inversiones
- Ejecuta operaciones automáticas basadas en el cruce de medias móviles
- Soporta tanto cuentas reales como de práctica

## ⚠️ Advertencia

**IMPORTANTE**: El trading de opciones binarias conlleva riesgos financieros significativos. Este bot es solo para fines educativos y de demostración. El autor no se hace responsable de pérdidas financieras. Use bajo su propio riesgo y preferiblemente en cuentas de práctica.

## 🚀 Características

- **Análisis Técnico Avanzado**: Sistema multi-indicador con SMA, EMA, RSI, ADX, ATR y Bandas de Bollinger
- **Validación Multi-Capa**: Requiere 5 confirmaciones simultáneas antes de operar
- **Gestión Avanzada de Riesgo**: Límites de inversión, protección contra pérdidas consecutivas
- **Sistema de Logging Completo**: Registra cada operación con detalles técnicos
- **Estadísticas en Tiempo Real**: Winrate, rachas, balance actualizado constantemente
- **Gestión de Capital Masaniello**: Sistema italiano de optimización de inversiones
- **Operaciones Automáticas**: Ejecuta CALL y PUT automáticamente según señales validadas
- **Soporte Multi-Activo**: Compatible con todos los activos de IQ Option
- **Modo Práctica/Real**: Elige entre cuenta demo o real
- **Protección de Capital**: Máximo 5% del balance por operación + pausas automáticas

## 📦 Requisitos

- Python 3.7+
- Cuenta en IQ Option
- Conexión estable a Internet

### Dependencias

```bash
numpy
TA-Lib
```

## 🔧 Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/victalejo/cross_wow.git
cd cross_wow
```

2. Instala las dependencias:

```bash
pip install numpy
```

3. Instala TA-Lib:

**Windows:**
- Descarga el wheel apropiado desde [aquí](https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib)
- Instala con: `pip install TA_Lib-0.4.XX-cpXX-cpXXm-win_amd64.whl`

**Linux/Mac:**
```bash
# Instalar dependencias del sistema
sudo apt-get install build-essential wget

# Descargar e instalar TA-Lib
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib/
./configure --prefix=/usr
make
sudo make install

# Instalar wrapper de Python
pip install TA-Lib
```

## 💻 Uso

1. Edita `main.py` y configura tus credenciales de IQ Option (línea 99):

```python
VIC = IQ_Option("tu_email@ejemplo.com", "tu_contraseña")
```

2. Ejecuta el bot:

```bash
python main.py
```

3. Sigue las instrucciones en pantalla:

```
REAL O PRACTICA: PRACTICE
Activo: EURUSD
Balance: 1000
numero de tiradas: 10
posibles ganados: 6
```

### Parámetros de Entrada

- **REAL O PRACTICA**: Tipo de cuenta a usar (`PRACTICE` o `REAL`)
- **Activo**: Par de divisas u activo a operar (ej: `EURUSD`, `GBPUSD`)
- **Balance**: Capital inicial disponible
- **Número de tiradas**: Total de operaciones planificadas en la sesión
- **Posibles ganados**: Cantidad de operaciones ganadoras objetivo según Masaniello

## 📊 Estrategia de Trading

El bot utiliza una estrategia mejorada con validación multi-capa:

### Indicadores Técnicos Utilizados

1. **SMA(20)**: Media Móvil Simple de 20 periodos - Identifica tendencia general
2. **EMA(5)**: Media Móvil Exponencial de 5 periodos - Señal de entrada
3. **RSI(14)**: Índice de Fuerza Relativa - Evita sobrecompra/sobreventa
4. **ADX(14)**: Índice Direccional Promedio - Confirma fuerza de tendencia
5. **ATR(14)**: Rango Verdadero Promedio - Mide volatilidad
6. **Bandas de Bollinger(20,2)**: Identifica rangos de precio

### Señal de CALL (Compra)

Se requieren **5 confirmaciones simultáneas**:

- ✓ EMA(5) cruza por encima de SMA(20)
- ✓ RSI entre 30-70 (no sobrecomprado)
- ✓ ADX > 25 (tendencia fuerte)
- ✓ Precio por encima de Banda Media de Bollinger
- ✓ Volatilidad controlada (ATR < 2% del precio)

### Señal de PUT (Venta)

Se requieren **5 confirmaciones simultáneas**:

- ✓ EMA(5) cruza por debajo de SMA(20)
- ✓ RSI entre 30-70 (no sobrevendido)
- ✓ ADX > 25 (tendencia fuerte)
- ✓ Precio por debajo de Banda Media de Bollinger
- ✓ Volatilidad controlada (ATR < 2% del precio)

### Gestión de Riesgo

- **Límite por operación**: Máximo 5% del balance actual
- **Protección anti-pérdidas**: Pausa automática tras 3 pérdidas consecutivas (5 minutos)
- **Masaniello optimizado**: Calcula inversión óptima basándose en:
  - Capital disponible
  - Operaciones restantes
  - Porcentaje de profit del activo
  - Victorias/derrotas acumuladas

### Sistema de Logging

Cada operación registra:
- Timestamp, tipo de operación (CALL/PUT)
- Monto invertido
- Valores de RSI, ADX, ATR
- Resultado (ganancia/pérdida)
- Balance actualizado
- Winrate en tiempo real

**Ver documentación completa**: [MEJORAS_ESTRATEGIA.md](MEJORAS_ESTRATEGIA.md)

## 📁 Estructura del Proyecto

```
cross_wow/
├── main.py              # Script principal del bot
├── masaniello.py        # Implementación del sistema Masaniello
├── iqoptionapi/         # API de IQ Option
│   ├── stable_api.py    # API estable principal
│   ├── http/            # Endpoints HTTP
│   └── ws/              # WebSocket y canales
├── README.md            # Este archivo
├── LICENSE              # Licencia GPL-3.0
└── CONTRIBUTING.md      # Guía de contribución
```

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor, lee [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles sobre nuestro código de conducta y proceso de pull requests.

## 📝 Licencia

Este proyecto está bajo la Licencia GNU General Public License v3.0 - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Víctor Alejo**
- Email: valejoapps@gmail.com
- GitHub: [@victalejo](https://github.com/victalejo)

## ⚖️ Disclaimer Legal

Este software se proporciona "tal cual", sin garantía de ningún tipo. El trading de opciones binarias es altamente especulativo y conlleva un alto nivel de riesgo. Solo debe operar con dinero que pueda permitirse perder.

El autor no es responsable de:
- Pérdidas financieras derivadas del uso de este software
- Problemas técnicos o errores en la ejecución
- Cambios en la API de IQ Option
- Violaciones de términos de servicio de terceros

## 🔍 FAQ

### ¿Es legal usar este bot?
Verifique los términos de servicio de IQ Option en su región. Algunos países pueden tener restricciones.

### ¿Garantiza ganancias?
No. Ningún sistema de trading garantiza ganancias. Los mercados son impredecibles.

### ¿Puedo modificar la estrategia?
Sí, el código es open source bajo GPL-3.0. Puede modificarlo según sus necesidades.

### ¿Funciona con otros brokers?
No, está específicamente diseñado para IQ Option.

## 📚 Recursos Adicionales

- [Documentación de TA-Lib](https://ta-lib.org/)
- [Sistema Masaniello](https://es.wikipedia.org/wiki/Masaniello_(apuestas))
- [IQ Option](https://iqoption.com/)

## 🐛 Reportar Problemas

Si encuentras algún bug o tienes sugerencias, por favor abre un [issue](https://github.com/victalejo/cross_wow/issues).

## ⭐ Agradecimientos

- A la comunidad de IQ Option API
- A los desarrolladores de TA-Lib
- A todos los contribuidores del proyecto

---

**Nota**: Este proyecto es independiente y no está afiliado, asociado, autorizado, respaldado por, ni de ninguna manera conectado oficialmente con IQ Option o cualquiera de sus subsidiarias o afiliados.
