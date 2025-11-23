# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [2.0.0] - 2025-11-23

### 🎉 Agregado

#### Indicadores Técnicos Avanzados
- **RSI (Relative Strength Index)** con periodo 14 para detectar sobrecompra/sobreventa
- **ADX (Average Directional Index)** con periodo 14 para medir fuerza de tendencia
- **ATR (Average True Range)** con periodo 14 para evaluar volatilidad
- **Bandas de Bollinger** (20,2) para identificar rangos de precio

#### Sistema de Validación Multi-Capa
- Validación de señales CALL con 5 confirmaciones simultáneas
- Validación de señales PUT con 5 confirmaciones simultáneas
- Filtros inteligentes para evitar señales falsas
- Detección de condiciones de mercado favorables

#### Gestión Avanzada de Riesgo
- Límite máximo de inversión por operación (5% del balance)
- Protección contra pérdidas consecutivas (pausa tras 3 pérdidas)
- Ajuste automático de inversión cuando Masaniello sugiere montos excesivos
- Sistema de pausas automáticas durante condiciones adversas (5 minutos)

#### Sistema de Logging Completo
- Registro detallado en archivo `trading_log.txt`
- Timestamps para cada operación
- Registro de valores de todos los indicadores
- Resultados de cada operación (ganancia/pérdida exacta)
- Salida en consola con formato mejorado y emojis

#### Estadísticas en Tiempo Real
- Cálculo de winrate actualizado tras cada operación
- Tracking de rachas ganadoras y perdedoras
- Identificación de mejor y peor racha
- Balance actualizado en cada operación

#### Resumen de Sesión
- Reporte completo al finalizar la sesión
- Comparación balance inicial vs final
- Ganancia/pérdida total y porcentual
- Estadísticas completas de rendimiento

#### Persistencia de Datos
- Guardado automático de estadísticas en `estadisticas.json`
- Fecha y hora de cada sesión
- Historial completo de rendimiento
- Formato JSON para fácil análisis

#### Archivos de Configuración
- `config_example.py` con todos los parámetros personalizables
- Presets predefinidos: Conservador, Moderado, Agresivo
- Documentación inline de cada parámetro

#### Archivos de Prueba
- `test_indicators.py` para validar indicadores sin conectarse
- Pruebas de validación de señales
- Verificación de cálculos

#### Documentación
- `MEJORAS_ESTRATEGIA.md` con explicación detallada de todas las mejoras
- README actualizado con nuevas características
- `requirements.txt` actualizado
- `.gitignore` para proteger datos sensibles

### 🔧 Cambiado

#### Función `analisis()`
- Retorna diccionario completo de indicadores en lugar de 4 valores
- Incluye 11 valores diferentes (6 indicadores)
- Mejor organización y claridad del código

#### Funciones `compra()` y `venta()`
- Ahora reciben diccionario de indicadores
- Registran información detallada con logging
- Mensajes más descriptivos con valores técnicos
- Retroalimentación visual mejorada

#### Función `logica()`
- Gestión completa de riesgo implementada
- Tracking de estadísticas en tiempo real
- Sistema de pausas automáticas
- Validación de inversión máxima
- Espera inteligente entre señales
- Resumen final de sesión
- Guardado automático de estadísticas

### 🛡️ Seguridad

- `.gitignore` agregado para evitar subir:
  - Archivos de log con información de operaciones
  - Estadísticas en JSON
  - Archivo `config.py` con credenciales
  - Archivos temporales y cache

### 📚 Documentación

- Documentación completa en `MEJORAS_ESTRATEGIA.md`
- README actualizado con sección de estrategia expandida
- Comentarios mejorados en el código
- Docstrings en todas las funciones nuevas
- Ejemplos de uso de configuración

### ⚡ Rendimiento

- Espera de 30 segundos cuando no hay señales válidas (reduce carga API)
- Validación eficiente con evaluación de cortocircuito
- Cálculo optimizado de indicadores (una sola llamada a API)

---

## [1.0.0] - Versión Original

### Características Iniciales
- Análisis técnico básico con SMA y EMA
- Sistema de gestión de capital Masaniello
- Operaciones automáticas CALL y PUT
- Conexión con API de IQ Option
- Soporte para cuentas PRACTICE y REAL

---

## Notas de Migración

### De v1.0.0 a v2.0.0

**Dependencias nuevas requeridas:**
```bash
pip install TA-Lib
```

**Cambios en el código:**
- La función `analisis()` ahora retorna un diccionario en lugar de 4 valores
- Las funciones `compra()` y `venta()` requieren parámetro `indicadores`
- La función `logica()` tiene nuevo parámetro opcional `max_perdidas_consecutivas`

**Archivos nuevos:**
- `trading_log.txt` - Se genera automáticamente
- `estadisticas.json` - Se genera automáticamente
- `config_example.py` - Ejemplo de configuración
- `test_indicators.py` - Script de prueba
- `.gitignore` - Protección de archivos sensibles
- `MEJORAS_ESTRATEGIA.md` - Documentación de mejoras
- `CHANGELOG.md` - Este archivo

**Configuración recomendada:**
1. Copiar `config_example.py` a `config.py`
2. Editar `config.py` con tus credenciales
3. Ejecutar `test_indicators.py` para verificar instalación
4. Ejecutar `main.py` con cuenta PRACTICE primero

---

## Roadmap Futuro

### [2.1.0] - Planificado
- [ ] Soporte para archivo de configuración externo
- [ ] Notificaciones por Telegram
- [ ] Análisis de múltiples timeframes
- [ ] Backtesting automático

### [2.2.0] - Planificado
- [ ] Dashboard web en tiempo real
- [ ] Soporte para múltiples activos simultáneos
- [ ] Optimización automática de parámetros
- [ ] Machine Learning para predicción

### [3.0.0] - Futuro
- [ ] Estrategias personalizables por archivo
- [ ] Sistema de plugins
- [ ] API REST para control remoto
- [ ] Integración con otros brokers

---

Para más información, consulta [MEJORAS_ESTRATEGIA.md](MEJORAS_ESTRATEGIA.md)
