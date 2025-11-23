# 🪟 Guía de Instalación para Windows - Cross WOW v2.0

Esta guía te ayudará a instalar todas las dependencias necesarias en Windows.

---

## 📋 Requisitos Previos

- ✅ Windows 10/11
- ✅ Python 3.8 o superior instalado
- ✅ PowerShell (incluido en Windows)
- ✅ Conexión a Internet

---

## 🚀 Instalación Paso a Paso

### Paso 1: Verificar Python

Abre PowerShell y ejecuta:

```powershell
python --version
```

Deberías ver algo como: `Python 3.11.x`

Si no está instalado, descárgalo desde: https://www.python.org/downloads/

---

### Paso 2: Instalar NumPy

```powershell
pip install numpy
```

Espera a que termine la instalación. Deberías ver:
```
Successfully installed numpy-X.XX.X
```

---

### Paso 3: Instalar TA-Lib (Crítico)

TA-Lib es la librería más importante. En Windows requiere pasos especiales.

#### Opción A: Instalación con Wheel (Recomendado) 🌟

1. **Determina tu versión de Python y arquitectura:**

```powershell
python -c "import sys; print(f'Python {sys.version_info.major}.{sys.version_info.minor} - {sys.maxsize > 2**32 and \"64\" or \"32\"} bits')"
```

Ejemplo de salida: `Python 3.11 - 64 bits`

2. **Descarga el wheel correcto:**

Ve a: https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib

Descarga el archivo según tu configuración:

| Python | Bits | Archivo a descargar |
|--------|------|---------------------|
| 3.8 | 64-bit | `TA_Lib‑0.4.28‑cp38‑cp38‑win_amd64.whl` |
| 3.9 | 64-bit | `TA_Lib‑0.4.28‑cp39‑cp39‑win_amd64.whl` |
| 3.10 | 64-bit | `TA_Lib‑0.4.28‑cp310‑cp310‑win_amd64.whl` |
| 3.11 | 64-bit | `TA_Lib‑0.4.28‑cp311‑cp311‑win_amd64.whl` |
| 3.12 | 64-bit | `TA_Lib‑0.4.28‑cp312‑cp312‑win_amd64.whl` |

3. **Instala el wheel descargado:**

```powershell
# Navega a la carpeta de descargas
cd $env:USERPROFILE\Downloads

# Instala el wheel (ajusta el nombre según tu archivo)
pip install TA_Lib-0.4.28-cp311-cp311-win_amd64.whl
```

Deberías ver:
```
Successfully installed TA-Lib-0.4.28
```

#### Opción B: Usando pip (Puede no funcionar)

```powershell
pip install TA-Lib
```

⚠️ Si falla, usa la Opción A.

---

### Paso 4: Verificar Instalación

Ejecuta el script de prueba incluido:

```powershell
# Navega al directorio del proyecto
cd ruta\a\cross_wow

# Ejecuta las pruebas
python test_indicators.py
```

Si todo está correcto, verás:

```
🧪 Probando indicadores técnicos...

📊 Datos de prueba generados:
   Precio de cierre actual: $100.23
   ...

📈 Calculando indicadores...

✓ SMA(20): $100.2345
✓ EMA(5): $100.1234
✓ RSI(14): 45.67
✓ ADX(14): 32.50
✓ ATR(14): 0.0234
✓ Banda Superior: $102.4567
✓ Banda Media: $100.2345
✓ Banda Inferior: $98.0123

✅ Todos los indicadores calculados correctamente!
...
```

---

## 🔧 Solución de Problemas Comunes

### Error: "pip no se reconoce como comando"

**Solución:**

```powershell
# Reinstala Python y marca "Add Python to PATH"
# O ejecuta:
python -m pip install --upgrade pip
```

### Error: "Microsoft Visual C++ 14.0 is required"

**Solución:**

1. Descarga Visual C++ Build Tools:
   https://visualstudio.microsoft.com/visual-cpp-build-tools/

2. Instala seleccionando "C++ build tools"

3. Reinicia PowerShell

4. Intenta instalar TA-Lib de nuevo

### Error: "No matching distribution found for TA-Lib"

**Solución:**

Usa la Opción A (wheel) en lugar de pip directo.

### Error al importar numpy: "DLL load failed"

**Solución:**

```powershell
# Desinstala numpy
pip uninstall numpy

# Reinstala versión compatible
pip install numpy==1.24.3
```

### Permisos insuficientes

**Solución:**

Ejecuta PowerShell como Administrador:
- Click derecho en PowerShell → "Ejecutar como administrador"

---

## ✅ Verificación Final

Ejecuta este comando para verificar todas las dependencias:

```powershell
python -c "import numpy; import talib; print('✅ Todas las dependencias instaladas correctamente!')"
```

Si ves el mensaje de éxito, ¡estás listo para usar el bot!

---

## 📦 Lista de Verificación de Instalación

```
☐ Python 3.8+ instalado
☐ pip funcional
☐ NumPy instalado
☐ TA-Lib instalado
☐ test_indicators.py ejecutado exitosamente
☐ Todas las importaciones funcionan
```

---

## 🎯 Siguiente Paso

Una vez completada la instalación:

1. **Configura tus credenciales** en `main.py`:
   ```python
   VIC = IQ_Option("tu_email@ejemplo.com", "tu_contraseña")
   ```

2. **Lee la guía rápida**: [QUICKSTART.md](QUICKSTART.md)

3. **Ejecuta el bot**:
   ```powershell
   python main.py
   ```

---

## 📞 Ayuda Adicional

Si sigues teniendo problemas:

1. **Revisa la documentación oficial de TA-Lib:**
   https://ta-lib.org/

2. **Busca tu error específico en:**
   - Stack Overflow
   - GitHub Issues del proyecto TA-Lib

3. **Contacta al autor:**
   - Email: valejoapps@gmail.com
   - GitHub: https://github.com/victalejo/cross_wow/issues

---

## 💡 Consejos Pro

- Usa un entorno virtual para aislar dependencias:
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  pip install numpy
  pip install TA_Lib-XXX.whl
  ```

- Actualiza pip regularmente:
  ```powershell
  python -m pip install --upgrade pip
  ```

- Guarda los wheels descargados para futuras reinstalaciones

---

**¡Buena suerte con la instalación! 🚀**

---

Última actualización: 23 de noviembre de 2025  
Versión: 2.0
