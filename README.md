# Python — Prácticas de Dificultad Gradual

Repositorio de **uso meramente didáctico** para aprender o repasar Python de forma gradual, resolviendo problemas como los de una entrevista técnica.

Avanza por niveles, de lo básico a lo avanzado, y **no mires soluciones** hasta haber intentado cada problema por tu cuenta.

## Propósito

- Aprender Python desde cero con ejercicios progresivos.
- Repasar conceptos clave de forma práctica.
- Practicar para entrevistas técnicas (lógica, algoritmos y estructuras de datos).
- Acercarse al mundo de Datos e IA mediante problemas aplicados.

Cada ejercicio introduce **una herramienta nueva**:
variables → condicionales → ciclos → strings → listas → diccionarios → funciones → algoritmos → estructuras de datos.

## Contenido

Los enunciados de los 40 problemas están en [`Problems`](./Problems), organizados en 7 niveles:

| Nivel | Tema | Problemas |
| ----- | ---- | --------: |
| 1 — Fundamentos | sintaxis, variables, condicionales y ciclos | 1–8 |
| 2 — Strings | cadenas | 9–14 |
| 3 — Listas | listas | 15–20 |
| 4 — Diccionarios y funciones | diccionarios y funciones | 21–25 |
| 5 — Problemas de algoritmos | algoritmos | 26–30 |
| 6 — Entrevista Junior | escenarios integradores | 31–35 |
| 7 — Data/IA | datos e inteligencia artificial | 36–40 |

## Características

- **40 problemas** de dificultad gradual en un solo documento.
- **7 niveles** temáticos claramente definidos.
- **Formato estándar** por ejercicio: enunciado, entrada, salida, ejemplos y restricciones.
- **Sin soluciones incluidas**: fomenta intentar primero y comparar después.
- **Solo biblioteca estándar** de Python; sin dependencias externas.

## Tecnologías

- **Python 3.x** — lenguaje de programación.
- **Markdown** — formato de documentación y enunciados.
- Solo se usa la biblioteca estándar de Python (`csv`, `math`, etc.).

## Estructura del proyecto

```
python-practicas-dificultad-gradual/
├── Problems            # Enunciados de los 40 problemas (Markdown)
└── README.md           # Este archivo
```

> 💡 Cada persona puede crear sus propios archivos de solución (por ejemplo, `soluciones/nivel1.py`) para practicar sin modificar los enunciados.

## Requisitos previos

- **Python 3.8 o superior** instalado. Verifica con:
  ```bash
  python --version
  ```
- Un editor de texto o IDE (VS Code recomendado).

## Instalación

Este repositorio no requiere dependencias externas.

```bash
git clone <url-del-repositorio>
cd python-practicas-dificultad-gradual
```

Si quieres un entorno aislado (opcional):

```bash
python -m venv .venv
```

- **Windows:** `.venv\Scripts\activate`
- **macOS/Linux:** `source .venv/bin/activate`

## Configuración

No se requiere configuración adicional. El repositorio funciona tal cual se clona.

## Cómo usar

1. Abre el archivo [`Problems`](./Problems).
2. Elige el nivel que corresponda a tu dominio actual (tabla de contenidos al inicio).
3. Lee el problema y resuélvelo en tu propio archivo `.py`.
4. Ejecuta tu solución con:
   ```bash
   python tu_solucion.py
   ```
5. Antes de buscar ayuda, revisa que tu solución cubra los casos normales y los casos límite.

## Ejecución

Cada ejercicio es un script independiente. No hay un punto de entrada único:

```bash
python <archivo-de-solucion>.py
```

## Variables de entorno

No aplica. No hay servidores, credenciales ni configuración por variables de entorno.

## Scripts disponibles

No hay scripts automatizados de construcción ni de pruebas. El proyecto se centra en la práctica manual de cada ejercicio.

## Despliegue

No aplica. Es un repositorio de aprendizaje local; no se despliega en ningún entorno.

## Método recomendado

> **No busques la solución inmediatamente.**

Para cada problema:

1. Entender exactamente qué entra y qué debe salir.
2. Escribir algunos ejemplos.
3. Resolverlo primero de la manera más sencilla que se te ocurra.
4. Probar casos normales y casos límite.
5. Preguntarte: **"¿puedo hacerlo más eficiente?"**
6. Solo entonces comparar con una solución más profesional.

## Contribución

¿Quieres aportar? Las contribuciones son bienvenidas:

- Corregir erratas o mejorar la redacción de los enunciados.
- Ampliar ejemplos o aclarar restricciones.
- Sugerir nuevos problemas manteniendo la dificultad gradual.

Para colaborar:

1. Haz un *fork* del repositorio.
2. Crea una rama: `git checkout -b mejora/nombre-descriptivo`.
3. Realiza tus cambios y haz *commit* con mensajes descriptivos.
4. Abre un *pull request* explicando el cambio.

## Licencia

Este repositorio no declara una licencia específica. Su contenido es de uso libre con fines educativos y personales.
