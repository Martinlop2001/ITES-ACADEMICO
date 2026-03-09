# Cómo personalizar posiciones de botones y elementos en la UI

Tu interfaz está construida **en código Python** (PyQt6), no con archivos `.ui` de Qt Designer. Para cambiar la posición de botones y demás elementos, se hace editando los **layouts** y propiedades en los archivos de `ui/`.

---

## 1. Conceptos básicos: layouts

Los elementos no se posicionan con coordenadas fijas (`x, y`). Se usan **layouts** que organizan todo automáticamente y permiten redimensionar bien:

| Layout | Uso |
|--------|-----|
| **QVBoxLayout** | Coloca widgets **uno debajo del otro** (vertical). |
| **QHBoxLayout** | Coloca widgets **uno al lado del otro** (horizontal). |
| **QGridLayout** | Coloca widgets en **filas y columnas** (rejilla). |
| **QFormLayout** | Etiqueta + campo por fila (formularios). |

Para cambiar **posiciones**, lo que haces es:
- Cambiar el **orden** en que añades widgets al layout.
- Usar **stretch**, **espaciado** y **márgenes**.
- En `QGridLayout`, cambiar la **fila y columna** (`addWidget(widget, fila, columna)`).

---

## 2. Ajustes útiles en cualquier pantalla

### Márgenes (espacio alrededor)

```python
layout.setContentsMargins(izquierda, arriba, derecha, abajo)  # en píxeles
# Ejemplo: más espacio a los lados
layout.setContentsMargins(40, 20, 40, 20)
```

### Espacio entre elementos

```python
layout.setSpacing(16)   # píxeles entre cada widget
```

### Stretch (empujar elementos hacia un lado)

- **addStretch()** antes de un widget: lo empuja hacia la **derecha** (en horizontal) o **abajo** (en vertical).
- **addStretch()** después: lo empuja hacia la **izquierda** o **arriba**.

```python
layout.addStretch(1)      # flexibilidad 1
layout.addWidget(mi_boton)
layout.addStretch(1)      # centra el botón
```

### Alineación dentro del layout

```python
layout.addWidget(boton, 0, Qt.AlignmentFlag.AlignCenter)  # centrado
layout.addWidget(boton, 0, Qt.AlignmentFlag.AlignRight)   # derecha
layout.addWidget(boton, 0, Qt.AlignmentFlag.AlignLeft)     # izquierda
```

---

## 3. Ejemplo: pantalla de inicio (`pantalla_inicio.py`)

Ahora los botones están en una **fila horizontal** al final, alineados a la derecha por el `addStretch()` delante.

**Para centrar los botones:**

```python
botones_layout = QHBoxLayout()
botones_layout.setSpacing(16)
# Stretch a ambos lados = centrado
botones_layout.addStretch(1)
botones_layout.addWidget(self.btn_iniciar)
botones_layout.addWidget(self.btn_registrarse)
botones_layout.addWidget(self.btn_salir)
botones_layout.addStretch(1)
layout.addLayout(botones_layout)
```

**Para poner los botones en columna (uno debajo de otro):**

```python
botones_layout = QVBoxLayout()  # vertical en vez de QHBoxLayout
botones_layout.setSpacing(16)
botones_layout.addWidget(self.btn_iniciar)
botones_layout.addWidget(self.btn_registrarse)
botones_layout.addWidget(self.btn_salir)
layout.addLayout(botones_layout)
```

**Para mover el título más arriba o más abajo:**

- Menos espacio arriba: quitar o reducir el primer `addStretch(1)` o poner otro antes del título.
- Más espacio entre título y botones: aumentar el valor en `addStretch(1)` o añadir otro `addStretch(1)`.

---

## 4. Ejemplo: menú admin (`pantalla_admin.py`)

Ahí se usa **QGridLayout**: cada botón está en una **fila** y **columna**.

```python
grid.addWidget(widget, fila, columna)
# Fila y columna empiezan en 0
```

**Cambiar posición de un botón:** cambia los números de fila y columna.

Ejemplo actual:
- (0,0) Gestión profesores   (0,1) Gestión alumnos  
- (1,0) Gestión materias     (1,1) Gestión faltas  
- (2,0) Crear usuario        (2,1) Cerrar sesión  

**Para poner "Cerrar sesión" solo abajo a la derecha:**

```python
grid.addWidget(self.btn_cerrar, 2, 1)  # ya está en (2,1)
# Para que no esté en la misma “celda” que otro, usa más filas:
grid.addWidget(self.btn_crear_profesor, 2, 0)
grid.addWidget(self.btn_cerrar, 3, 1)  # fila 3, columna 1
```

**Para centrar todo el grid:**

```python
layout.addLayout(grid)   # por defecto suele ocupar todo el ancho
# Si el layout principal es QVBoxLayout, puedes añadir stretch arriba y abajo:
layout.addStretch(1)
layout.addLayout(grid)
layout.addStretch(1)
```

---

## 5. Resumen rápido

| Quieres… | Dónde / Cómo |
|----------|----------------|
| Más o menos espacio alrededor | `setContentsMargins(izq, arr, der, abj)` |
| Más o menos espacio entre botones | `setSpacing(n)` |
| Centrar algo | `addStretch(1)` a ambos lados (o antes y después) |
| Subir/bajar elementos | Añadir o quitar `addStretch()` en un QVBoxLayout |
| Cambiar orden de botones | Cambiar el orden de los `addWidget(...)` |
| Rejilla (admin, etc.) | Cambiar `fila, columna` en `grid.addWidget(widget, fila, columna)` |
| Botones en columna en vez de fila | Usar `QVBoxLayout` en vez de `QHBoxLayout` para esos botones |

---

## 6. Si en el futuro usas Qt Designer (.ui)

1. Creas/editas el `.ui` en **Qt Designer** y guardas.
2. En Python cargas el archivo con `QUiLoader` o generas código con `pyuic6`.
3. **Desde Qt Designer** puedes arrastrar y soltar para cambiar posiciones y usar los layouts en la propia herramienta.
4. **Desde código**, después de cargar el `.ui`, puedes seguir accediendo a los widgets por nombre y, si es necesario, meter algunos en layouts adicionales o cambiar márgenes/espaciado por código.

Mientras todo siga en Python (como ahora), cualquier cambio de posición se hace editando los archivos en `ui/` como en los ejemplos de arriba.
