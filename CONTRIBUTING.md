# Guía de Contribución 🤝

¡Gracias por tu interés en contribuir a Cross WOW! Este documento proporciona pautas y mejores prácticas para contribuir al proyecto.

## 📋 Tabla de Contenidos

- [Código de Conducta](#código-de-conducta)
- [¿Cómo puedo contribuir?](#cómo-puedo-contribuir)
- [Proceso de Desarrollo](#proceso-de-desarrollo)
- [Guías de Estilo](#guías-de-estilo)
- [Reportar Bugs](#reportar-bugs)
- [Sugerir Mejoras](#sugerir-mejoras)
- [Pull Requests](#pull-requests)

## 📜 Código de Conducta

Este proyecto y todos los que participan en él se rigen por nuestro compromiso de proporcionar un entorno acogedor y libre de acoso para todos, independientemente de:

- Edad
- Tamaño corporal
- Discapacidad
- Etnia
- Identidad y expresión de género
- Nivel de experiencia
- Nacionalidad
- Apariencia personal
- Raza
- Religión
- Identidad y orientación sexual

### Nuestros Estándares

**Comportamientos que contribuyen a crear un ambiente positivo:**

✅ Usar lenguaje acogedor e inclusivo
✅ Respetar diferentes puntos de vista y experiencias
✅ Aceptar críticas constructivas con gracia
✅ Enfocarse en lo que es mejor para la comunidad
✅ Mostrar empatía hacia otros miembros

**Comportamientos inaceptables:**

❌ Uso de lenguaje o imágenes sexualizadas
❌ Comentarios insultantes/despectivos y ataques personales
❌ Acoso público o privado
❌ Publicar información privada de otros sin permiso
❌ Otras conductas que podrían considerarse inapropiadas

## 🚀 ¿Cómo puedo contribuir?

### 1. Reportar Bugs

Los bugs se rastrean como [GitHub Issues](https://github.com/victalejo/cross_wow/issues). Antes de crear un issue:

- **Verifica** que el bug no haya sido reportado ya
- **Comprueba** que no esté en la lista de problemas conocidos
- **Asegúrate** de usar la última versión del código

### 2. Corregir Bugs

Revisa los issues con la etiqueta `bug`. Si encuentras uno que te gustaría resolver:

1. Comenta en el issue indicando que trabajarás en él
2. Sigue el [Proceso de Desarrollo](#proceso-de-desarrollo)
3. Envía un Pull Request

### 3. Implementar Nuevas Características

Si deseas añadir una nueva característica:

1. Abre primero un issue para discutir la propuesta
2. Espera feedback de los mantenedores
3. Una vez aprobado, implementa siguiendo nuestras guías
4. Envía un Pull Request

### 4. Mejorar Documentación

La documentación siempre puede mejorar:

- Corregir errores tipográficos
- Aclarar explicaciones confusas
- Añadir ejemplos
- Traducir a otros idiomas

## 🔧 Proceso de Desarrollo

### Configuración del Entorno

1. **Fork** el repositorio

2. **Clona** tu fork:
```bash
git clone https://github.com/TU_USUARIO/cross_wow.git
cd cross_wow
```

3. **Añade** el repositorio original como upstream:
```bash
git remote add upstream https://github.com/victalejo/cross_wow.git
```

4. **Crea** un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

5. **Instala** dependencias:
```bash
pip install numpy
# Instala TA-Lib según tu sistema operativo
```

### Flujo de Trabajo

1. **Sincroniza** con upstream antes de empezar:
```bash
git checkout main
git pull upstream main
```

2. **Crea** una rama para tu trabajo:
```bash
git checkout -b feature/nombre-descriptivo
# o
git checkout -b fix/nombre-del-bug
```

3. **Realiza** tus cambios siguiendo las [Guías de Estilo](#guías-de-estilo)

4. **Commit** tus cambios:
```bash
git add .
git commit -m "Descripción clara del cambio"
```

5. **Push** a tu fork:
```bash
git push origin feature/nombre-descriptivo
```

6. **Abre** un Pull Request desde GitHub

### Convención de Nombres de Ramas

- `feature/nombre-caracteristica` - Para nuevas características
- `fix/nombre-bug` - Para corrección de bugs
- `docs/nombre-mejora` - Para cambios en documentación
- `refactor/nombre-refactor` - Para refactorización de código
- `test/nombre-test` - Para añadir o mejorar tests

## 📝 Guías de Estilo

### Código Python

Seguimos [PEP 8](https://www.python.org/dev/peps/pep-0008/) con algunas excepciones:

```python
# ✅ BIEN
def calcular_media_movil(datos, periodo):
    """
    Calcula la media móvil simple.
    
    Args:
        datos (list): Lista de precios
        periodo (int): Número de periodos
        
    Returns:
        float: Media móvil calculada
    """
    if len(datos) < periodo:
        return None
    return sum(datos[-periodo:]) / periodo


# ❌ MAL
def calc_mm(d,p):
    return sum(d[-p:])/p
```

### Estilo de Código

**Nombres de Variables:**
- Usa nombres descriptivos en español o inglés (consistente)
- Variables: `snake_case`
- Constantes: `UPPER_CASE`
- Clases: `PascalCase`

**Documentación:**
```python
def funcion_ejemplo(parametro1, parametro2):
    """
    Breve descripción de una línea.
    
    Descripción más detallada si es necesario,
    explicando el propósito y comportamiento.
    
    Args:
        parametro1 (tipo): Descripción
        parametro2 (tipo): Descripción
        
    Returns:
        tipo: Descripción del valor retornado
        
    Raises:
        TipoError: Cuando ocurre X
    """
    pass
```

**Importaciones:**
```python
# Orden:
# 1. Librerías estándar
import time
from datetime import datetime

# 2. Librerías de terceros
import numpy as np
from talib import EMA, SMA

# 3. Módulos locales
from iqoptionapi.stable_api import IQ_Option
import masaniello as ms
```

### Commits

**Formato de Mensajes de Commit:**

```
tipo: Descripción breve (máx 50 caracteres)

Explicación detallada opcional del cambio,
envuelve a 72 caracteres.

- Punto adicional 1
- Punto adicional 2
```

**Tipos de Commit:**
- `feat`: Nueva característica
- `fix`: Corrección de bug
- `docs`: Cambios en documentación
- `style`: Formato, punto y coma faltantes, etc.
- `refactor`: Refactorización de código
- `test`: Añadir tests
- `chore`: Mantenimiento

**Ejemplos:**
```
feat: Añadir indicador RSI al análisis técnico

Implementa el cálculo del RSI con periodo configurable
para mejorar las señales de entrada.

fix: Corregir error en cálculo de Masaniello

El método ExecuteInvestment no manejaba correctamente
el caso cuando el balance era menor que la inversión mínima.
```

## 🐛 Reportar Bugs

Al reportar un bug, incluye:

### Información del Sistema
- Sistema operativo y versión
- Versión de Python
- Versiones de dependencias relevantes

### Descripción del Problema
- **Título claro y descriptivo**
- **Pasos para reproducir** (detallados)
- **Comportamiento esperado**
- **Comportamiento actual**
- **Capturas de pantalla** (si aplica)
- **Logs de error completos**

### Plantilla de Issue para Bugs

```markdown
## Descripción
Breve descripción del problema

## Pasos para Reproducir
1. Ir a '...'
2. Hacer clic en '...'
3. Ver error

## Comportamiento Esperado
Qué debería ocurrir

## Comportamiento Actual
Qué ocurre en realidad

## Entorno
- OS: [ej. Windows 10]
- Python: [ej. 3.9.5]
- Versión Cross WOW: [ej. 1.0.0]

## Logs
```
Pega aquí los logs de error
```

## Capturas
Si aplica, añade capturas de pantalla
```

## 💡 Sugerir Mejoras

Para sugerir una mejora o nueva característica:

1. **Verifica** que no exista ya una sugerencia similar
2. **Abre un issue** con la etiqueta `enhancement`
3. **Describe** claramente la mejora propuesta
4. **Explica** por qué sería útil
5. **Incluye** ejemplos de uso si es posible

### Plantilla de Issue para Mejoras

```markdown
## Resumen
Breve descripción de la mejora

## Motivación
¿Por qué es necesaria esta mejora?

## Propuesta
Descripción detallada de cómo funcionaría

## Alternativas Consideradas
Otras formas de resolver el problema

## Ejemplo de Uso
```python
# Código mostrando cómo se usaría
```

## Impacto
¿A quién beneficiaría esto?
```

## 📤 Pull Requests

### Antes de Enviar

- [ ] He leído la guía de contribución
- [ ] Mi código sigue el estilo del proyecto
- [ ] He comentado mi código, especialmente en áreas complejas
- [ ] He actualizado la documentación correspondiente
- [ ] Mis cambios no generan nuevas advertencias
- [ ] He probado que mi corrección funciona

### Proceso de Revisión

1. Un mantenedor revisará tu PR
2. Puede solicitar cambios o aclaraciones
3. Realiza los cambios solicitados
4. El PR será fusionado una vez aprobado

### Checklist del PR

```markdown
## Descripción
Descripción clara de los cambios

## Tipo de Cambio
- [ ] Bug fix
- [ ] Nueva característica
- [ ] Breaking change
- [ ] Documentación

## ¿Cómo se ha probado?
Describe las pruebas realizadas

## Checklist
- [ ] Mi código sigue el estilo del proyecto
- [ ] He realizado una auto-revisión
- [ ] He comentado código complejo
- [ ] He actualizado la documentación
- [ ] Mis cambios no generan advertencias
```

## 🧪 Tests

Actualmente el proyecto no tiene tests automatizados, pero es una área donde las contribuciones son especialmente bienvenidas.

### Añadir Tests

Si deseas contribuir con tests:

1. Usa `pytest` como framework
2. Coloca los tests en un directorio `tests/`
3. Nombra los archivos como `test_*.py`
4. Asegúrate de que todos los tests pasen antes de enviar el PR

```python
# tests/test_masaniello.py
import pytest
from masaniello import masanielloSH

def test_masaniello_initialization():
    ms = masanielloSH(80, 1000)
    assert ms.initialBalance == 1000
    assert ms.profitParam == 1.80
```

## 📞 Contacto

Si tienes preguntas sobre cómo contribuir:

- Abre un issue con la etiqueta `question`
- Contacta al autor: valejoapps@gmail.com

## 🙏 Agradecimientos

¡Gracias por contribuir a Cross WOW! Cada contribución, grande o pequeña, es valiosa y apreciada.

---

**Nota**: Esta guía de contribución puede actualizarse. Verifica siempre la última versión antes de contribuir.
