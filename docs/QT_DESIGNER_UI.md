# Uso de Qt Designer con ITES Académico

La interfaz está definida en **archivos .ui** (Qt Designer) en la carpeta `ui/forms/`. Podés abrirlos en **Qt Designer** para editar el diseño de forma visual (posiciones, tamaños, textos, estilos) sin tocar el código Python.

---

## Dónde está cada pantalla

| Archivo .ui | Descripción |
|-------------|-------------|
| `ventana_principal.ui` | Ventana principal (tamaño 800×800, mínimo 400×400). Contiene el `QStackedWidget` donde se muestran el resto de pantallas. |
| `pantalla_inicio.ui` | Inicio: título y botones Iniciar sesión, Registrarse, Cerrar programa. |
| `pantalla_admin.ui` | Menú administrador (grid de botones). |
| `pantalla_alumno.ui` | Menú alumno: Consultar faltas y tabla. |
| `pantalla_profesor.ui` | Menú profesor: Registrar falta, Ver faltas, tabla. |
| `pantalla_gestion_*.ui` | Gestión de profesores, alumnos, materias y faltas (tabla + botones). |
| `dialogo_login.ui` | Diálogo usuario/contraseña. |
| `dialogo_registro.ui` | Registro de alumno. |
| `dialogo_crear_usuario_profesor.ui` | Crear usuario para un profesor. |
| `dialogo_registrar_falta.ui` | Registrar falta (profesor). |
| `formulario_profesor.ui` / `formulario_alumno.ui` | Alta/edición profesor o alumno. |
| `formulario_materia.ui` / `formulario_falta.ui` | Alta materia o falta (admin). |

---

## Cómo editar en Qt Designer

1. **Abrir Qt Designer** (viene con Qt o con PyQt; en Windows suele estar en el menú de inicio o en la ruta de instalación de Qt/Python).
2. **Abrir un .ui**: Archivo → Abrir y elegir, por ejemplo, `ui/forms/pantalla_inicio.ui`.
3. **Cambiar lo que quieras**:
   - Tamaño de la ventana o del formulario: seleccionar el widget raíz y en el panel de propiedades ajustar **geometry** o **minimumSize** / **maximumSize**.
   - Posición de botones y layouts: arrastrar widgets, usar los layouts (horizontal, vertical, grid) desde la barra superior.
   - Textos: doble clic en etiquetas o botones, o editar la propiedad **text** en el panel de propiedades.
   - Estilos: propiedad **styleSheet** del widget.
4. **Guardar** el .ui (Ctrl+S). Al volver a ejecutar la aplicación, los cambios se verán sin tocar Python.

---

## Resolución y tamaño de la ventana

- **Ventana principal**: tamaño por defecto y mínimo se definen en `ventana_principal.ui`. Abrí ese archivo en Qt Designer, seleccioná el widget raíz (VentanaPrincipal) y en el panel de propiedades modificá:
  - **geometry** (ancho y alto por defecto),
  - **minimumSize** (tamaño mínimo al redimensionar).
- Cualquier otra pantalla o diálogo: mismo criterio (widget raíz → geometry / minimumSize).

---

## Qué no conviene cambiar en el .ui

- **Nombres de objeto (objectName)** de los widgets que el código Python usa (por ejemplo `btn_iniciar`, `tabla_faltas`, `input_usuario`). Si los renombrás, tenés que actualizar el mismo nombre en el .py que hace `loadUi` y usa ese widget.
- **Tipo de widget** (por ejemplo pasar de `QPushButton` a `QToolButton`): puede requerir cambios en el código si se usan métodos específicos del botón.

---

## Flujo del proyecto

- Los **.ui** definen solo la estructura visual (widgets y layouts).
- El **código Python** en `ui/*.py` carga cada .ui con `uic.loadUi(ruta_ui("archivo.ui"), self)` y se encarga de:
  - Conectar señales (clics, aceptar/cancelar),
  - Rellenar tablas y combos con datos,
  - Validar formularios y llamar a los servicios.

Así podés seguir editando el diseño en Qt Designer y la lógica en el editor de código.
