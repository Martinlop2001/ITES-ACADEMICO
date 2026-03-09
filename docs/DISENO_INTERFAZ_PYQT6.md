# Guía de diseño: interfaz PyQt6 – ITES Académico

Esta guía define cómo diseñar la interfaz **antes** de programar: pantallas, flujo, tablas, checkmarks y uso de imágenes de fondo.

---

## 1. Flujo de pantallas

```
┌─────────────────────────────────────────────────────────────────┐
│                    PANTALLA PRINCIPAL (Inicio)                   │
│  Título + imagen de fondo + [Iniciar sesión] [Registrarse] [Salir] │
└─────────────────────────────────────────────────────────────────┘
         │                    │
         │ Iniciar sesión     │ Registrarse
         ▼                    ▼
┌──────────────────┐   ┌──────────────────┐
│  Diálogo /       │   │  Formulario       │
│  ventana LOGIN   │   │  REGISTRO alumno  │
└────────┬─────────┘   └──────────────────┘
         │
         │ según rol
         ├──────────────┬──────────────┬──────────────┐
         ▼              ▼              ▼              │
   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
   │  ALUMNO  │   │  ADMIN   │   │ PROFESOR │        │
   │  Menú    │   │  Menú    │   │  Menú    │        │
   └──────────┘   └──────────┘   └──────────┘        │
         │              │              │              │
         └──────────────┴──────────────┴──────────────┘
                        │
                        │ Cerrar sesión → vuelve a Pantalla principal
                        ▼
```

- **Una ventana principal** (`QMainWindow`) que actúa como “contenedor”.
- **Varias “pantallas”** = distintos **QWidget** (o QStackedWidget) que se muestran/ocultan según la pantalla actual.
- **Diálogos** (`QDialog`) para: login, registro, formularios de alta/edición (profesor, alumno, materia, falta).

---

## 2. Pantalla principal (inicio)

- **Título**: por ejemplo “ITES Académico” o “Sistema de Asistencias” en un `QLabel` grande y centrado.
- **Imagen de fondo**: no dibujada a mano en Qt. Usar una **imagen** (PNG/JPG) y mostrarla con:
  - Un `QLabel` que ocupe todo el fondo y tenga un `QPixmap` escalado, **o**
  - Estilos de la ventana con `background-image` en la hoja de estilo (Qt Style Sheets).
- **Tres botones**:
  1. **Iniciar sesión**: abre diálogo de login; si el login es correcto, cambia a la pantalla del menú según rol.
  2. **Registrarse**: abre diálogo/formulario para registro de alumno (DNI, nombre, apellido, correo, usuario, contraseña).
  3. **Cerrar programa**: cierra la aplicación.

Los botones y el título se hacen **solo en Qt**; la parte “decorativa” es la imagen. Conviene tener una carpeta `assets/` o `recursos/` con, por ejemplo:

- `fondo_inicio.png` (o `.jpg`) para la pantalla de inicio.

---

## 2.1 Tamaño de ventana y redimensionado (todas las pantallas)

- **Tamaño por defecto**: 800×800 píxeles.
- **Tamaño mínimo**: 400×400 píxeles (el usuario puede achicar la ventana hasta ese límite).
- **Redimensionado**: la ventana debe poder agrandarse o achicarse libremente dentro de ese rango; la **estructura no debe deformarse** y debe verse correcta en cualquier tamaño.

**Cómo lograrlo en PyQt6:**

| Aspecto | Implementación |
|--------|-----------------|
| Tamaño inicial | `setFixedSize(800, 800)` **no** usar (bloquearía el redimensionado). Usar `resize(800, 800)` al mostrar la ventana. |
| Tamaño mínimo | `setMinimumSize(400, 400)` en la ventana principal (`QMainWindow`). |
| Que no se deforme | Usar **layouts** (`QHBoxLayout`, `QVBoxLayout`, `QGridLayout`) en todas las pantallas. No posicionar widgets con coordenadas fijas (`move`, `setGeometry`). |
| Tablas y listas | Asignar **size policy** adecuada: la tabla/área de contenido suele tener `Expanding` en horizontal y vertical para que ocupe el espacio disponible y crezca al agrandar la ventana. |
| Botones y barras | Mantenerlos en layouts con **stretch** o alineación; así no se aplastan ni se separan de forma rara. |
| Imagen de fondo | Si usas `QLabel` con pixmap, redimensionar el pixmap en el evento `resizeEvent` del widget (escalar al tamaño actual) para que el fondo se adapte sin deformarse; o usar `background-image` en style sheet con `background-size` para cubrir/contener. |

Aplicar estas reglas a la **ventana principal** y a cada **pantalla** (widgets dentro del `QStackedWidget`) para que todo el flujo sea consistente al cambiar de tamaño.

---

## 3. Menús según rol

### 3.1 Alumno

- **Opciones**:
  - **Consultar mis faltas**: abre una pantalla o diálogo con la lista de faltas del alumno logueado.
  - **Cerrar sesión**: vuelve a la pantalla principal y limpia el usuario actual.

### 3.2 Admin

- **Opciones** (botones o ítems de menú):
  - Gestión profesores  
  - Gestión alumnos  
  - Gestión materias  
  - Gestión faltas  
  - Crear usuario profesor  
  - Cerrar sesión  

Cada “gestión” puede ser una **nueva pantalla** dentro del mismo contenedor (QStackedWidget) o una **ventana/diálogo** que se abre al hacer clic.

### 3.3 Profesor

- **Opciones**:
  - **Registrar falta**: formulario o pantalla para elegir alumno, materia, fecha, motivo (el profesor_id se toma del usuario logueado).
  - **Ver mis faltas**: listado de faltas que ese profesor registró (o sus materias).
  - **Cerrar sesión**: vuelve a la pantalla principal.

---

## 4. Cómo mostrar listados: tablas

Para **listar** profesores, alumnos, materias o faltas, lo más claro es usar **tablas**:

- **Widget**: `QTableWidget` (más simple) o `QTableView` + modelo (más flexible).
- **Columnas** según lo que ya devuelven tus servicios:
  - **Profesores**: ID, DNI, Nombre, Apellido, Correo.
  - **Alumnos**: ID, DNI, Nombre, Apellido, Correo.
  - **Materias**: ID, Nombre, Profesor (nombre o ID).
  - **Faltas (admin/listado general)**: ID, Profesor, Materia, Fecha, Motivo (y opcional Alumno si lo tienes en el repo).
  - **Faltas (alumno)**: ID, Materia, Fecha, Motivo.
  - **Faltas (profesor)**: ID, Alumno, Materia, Fecha, Motivo (según lo que expongas en el servicio).

En cada pantalla de “gestión” puedes tener:

- Una **tabla** que se rellena con los datos del servicio (listar).
- Botones: **Agregar**, **Editar** (fila seleccionada), **Eliminar** (fila seleccionada). Editar/Eliminar pueden abrir diálogos o pedir confirmación.

No hace falta “dibujar” la tabla a mano: solo definir columnas y rellenar filas con los datos que ya tienes en tus repositorios/servicios.

---

## 5. Uso de “tildes” (checkmarks)

Las **tildes** (marcar/desmarcar) sirven cuando quieres indicar **sí/no** sobre cada ítem. Algunos usos que encajan con tu sistema:

1. **Listado de faltas (admin/profesor)**  
   - Columna extra con un **checkbox** (“¿Eliminar?” o “Seleccionada”) para marcar varias faltas y, por ejemplo, eliminarlas en lote.

2. **Registrar falta (profesor)**  
   - En vez de elegir solo una materia, podrías mostrar la **lista de materias del profesor** con un **checkbox por materia**: “Marco las materias en las que falta este alumno hoy”. Luego guardas una falta por cada materia marcada (misma fecha/motivo).

3. **Gestión materias / alumnos**  
   - Checkbox para “seleccionar” filas y luego “Eliminar seleccionados” o “Exportar seleccionados”.

4. **Asistencia por materia (si en el futuro agregas “asistió sí/no”)**  
   - Una columna con checkbox “Asistió” por cada alumno/materia/fecha.

Recomendación inicial: usar **tabla con datos** (sin checkmarks) para listar y, en “Registrar falta”, usar **combos o listas** para elegir alumno/materia/fecha. Si quieres, en “Registrar falta” puedes añadir **checkmarks por materia** (marcar varias materias para el mismo alumno/fecha) usando `QCheckBox` por cada materia en un formulario.

---

## 6. Imágenes de fondo (resumen)

- **No dibujar fondos a mano** con primitivas de Qt; usar **imágenes**.
- **Dónde**: carpeta `assets/` (o `recursos/`, `img/`) en la raíz del proyecto, por ejemplo:
  - `assets/fondo_inicio.png`
- **Cómo**:
  - Opción A: `QLabel` de fondo con `setPixmap()` y escalado (mantener relación de aspecto si quieres).
  - Opción B: en la ventana o en el widget de la pantalla, usar **Qt Style Sheets**:  
    `background-image: url(assets/fondo_inicio.png);`  
    (usar rutas relativas al ejecutable o absolutas para desarrollo).
- Los **botones, títulos y campos** se crean encima con Qt; la imagen es solo decorativa y no tiene que ser “funcional”.

---

## 7. Estructura de carpetas sugerida

```
ITES-ACADEMICO/
├── main.py                 # Punto de entrada; inicia app PyQt6 y carga pantalla principal
├── db/
├── repositorio/
├── servicios/
├── modelos/
├── assets/                 # Imágenes (fondo_inicio.png, etc.)
├── ui/                     # Módulos de interfaz
│   ├── __init__.py
│   ├── ventana_principal.py   # QMainWindow + QStackedWidget de pantallas
│   ├── pantalla_inicio.py     # Título + imagen + 3 botones
│   ├── pantalla_alumno.py     # Menú alumno
│   ├── pantalla_admin.py     # Menú admin
│   ├── pantalla_profesor.py   # Menú profesor
│   ├── dialogo_login.py
│   ├── dialogo_registro.py
│   ├── dialogo_*_formulario.py  # Alta/edición según entidad
│   └── widgets_tablas.py     # Opcional: tablas reutilizables
└── docs/
    └── DISENO_INTERFAZ_PYQT6.md  # Esta guía
```

La lógica de negocio (login, listar, registrar falta, etc.) se sigue llamando desde la UI a tus **servicios** existentes (`UsuarioServicio`, `FaltaServicio`, etc.); la UI solo muestra datos y reacciona a clics.

---

## 8. Resumen de decisiones

| Tema | Decisión |
|------|----------|
| Pantalla principal | Título + imagen de fondo (archivo) + 3 botones (Iniciar sesión, Registrarse, Cerrar programa). |
| **Tamaño ventana** | **Por defecto 800×800 px; mínimo 400×400 px; redimensionable; layouts para que no se deforme.** |
| Navegación | Una ventana principal; pantallas por rol como “páginas” (QStackedWidget) o ventanas/diálogos. |
| Listados | Tablas (QTableWidget o QTableView) para profesores, alumnos, materias y faltas. |
| Tildes | Checkboxes para marcar materias al registrar varias faltas, o para seleccionar filas (eliminar/acciones en lote). |
| Fondos | Imágenes en `assets/`; mostradas por QLabel o Style Sheet; en Qt solo botones y controles funcionales. |

Cuando tengas claro este diseño (y si quieres cambiar algo de roles, pantallas o tildes), se puede bajar a código: primero pantalla principal + login + menús por rol, y después cada gestión con sus tablas y formularios.
