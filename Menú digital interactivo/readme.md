# SmartRoast — Menú Digital Interactivo ☕

Proyecto académico desarrollado para la materia Desarrollo Web.

## Integrantes

* Fer
* Magalí

---

# Descripción del Proyecto

SmartRoast es una cafetería ficticia que necesita un sistema digital interactivo para Take Away.

El proyecto consiste en desarrollar un subsitio web responsive con:

* Página de inicio
* Catálogo digital de cafés
* Carrito / Checkout

El sistema permitirá:

* visualizar productos
* agregar cafés al carrito
* actualizar un contador dinámicamente
* visualizar un resumen de compra

---

# Tecnologías Utilizadas

* HTML5
* CSS3
* JavaScript
* Bootstrap 5

---

# Estructura del Proyecto

```txt

style.css


main.js

/imagenes

index.html
catalogo.html
carrito.html
```

---

# Historias de Usuario (HU)

# Semana 6

## HU — Fer

**Como** desarrollador del proyecto SmartRoast,
**quiero** crear la estructura inicial del sitio y configurar la base técnica del proyecto,
**para** permitir el desarrollo del catálogo interactivo y del sistema de carrito mediante HTML, CSS y JavaScript.

### Tareas realizadas

* Creación de:

  * `index.html`
  * `catalogo.html`
  * `carrito.html`
* Integración de Bootstrap
* Integración de tipografía Montserrat
* Configuración inicial de colores
* Desarrollo de navbar compartida
* Configuración inicial de archivos globales

---

## HU — Magalí

**Como** responsable visual del proyecto SmartRoast,
**quiero** definir la identidad visual inicial y organizar la información de los productos,
**para** construir una experiencia moderna y coherente con la temática de cafetería especializada.

### Tareas realizadas

* Definición inicial de:

  * paleta de colores
  * estilo visual
  * referencias gráficas
* Organización de productos:

  * nombres
  * precios
  * categorías
  * métodos de preparación
  * notas de cata

---

# Semana 7

## HU — Fer

**Como** desarrollador del proyecto SmartRoast,
**quiero** comenzar la implementación funcional del catálogo y preparar la lógica inicial del carrito,
**para** permitir futuras interacciones dinámicas mediante JavaScript y manipulación del DOM.

### Tareas

* Crear estructura HTML del catálogo
* Preparar botones “Agregar al carrito”
* Crear estructura inicial del checkout
* Inicializar variables:

  * cantidadProductos
  * total
  * detalle
* Vincular `main.js`
* Preparar IDs y clases para DOM

---

## HU — Magalí

**Como** responsable visual del proyecto SmartRoast,
**quiero** diseñar la interfaz visual del catálogo y del carrito,
**para** construir una experiencia moderna, responsive y coherente con la identidad de la marca.

### Tareas

* Diseñar cards de productos
* Agregar imágenes
* Implementar estilos responsive
* Diseñar visualmente el carrito
* Mejorar experiencia visual general

---

# Issues

# Semana 6

## Issues — Fer

### #1 Crear estructura base del proyecto

* Crear páginas HTML
* Organizar estructura inicial

### #2 Configurar Bootstrap

* Integrar Bootstrap CSS y JS

### #3 Integrar tipografía Montserrat

* Vincular fuente y aplicar estilos

### #4 Crear navbar compartida

* Navegación entre páginas
* Ícono carrito
* Badge contador

### #5 Crear archivo global de estilos

* Variables CSS
* Colores iniciales
* Navbar

### #6 Vincular archivos globales

* `style.css`
* `main.js`

---

## Issues — Magalí

### #1 Definir identidad visual inicial

* Paleta de colores
* Referencias visuales

### #2 Seleccionar estilos base

* Tipografía
* Botones
* Links

### #3 Diseñar navbar inicial

* Estilos visuales del header

### #4 Organizar contenido de productos

* Cafés
* Categorías
* Precios
* Métodos

---

# Semana 7

## Issues — Fer

### #7 Crear estructura HTML del catálogo

* Contenedor de productos
* Cards

### #8 Preparar botones “Agregar al carrito”

* Botones e IDs para JS

### #9 Crear estructura inicial del checkout

* Productos
* Total
* Botón continuar

### #10 Inicializar variables del carrito

```javascript
let cantidadProductos = 0;
let total = 0;
let detalle = "";
```

### #11 Vincular lógica inicial del carrito

* Actualización dinámica del contador

### #12 Organizar estructura para DOM

* IDs y clases necesarias

---

## Issues — Magalí

### #5 Diseñar cards del catálogo

* Diseño visual de productos

### #6 Agregar imágenes de productos

* Organización en `/imagenes`

### #7 Implementar estilos responsive iniciales

* Mobile First

### #8 Diseñar visualmente la página del carrito

* Layout checkout
* Botones
* Total

### #9 Mejorar experiencia visual del sitio

* Hover effects
* Consistencia visual

---

# Estado Actual del Proyecto

✅ Estructura base creada
✅ Navegación funcional
✅ Bootstrap integrado
✅ Tipografía integrada
✅ CSS global inicial
✅ Preparación para carrito dinámico

---

# Funcionalidades Futuras

* Carrito dinámico con JavaScript
* Actualización automática del contador
* Persistencia con localStorage
* Checkout visual
* Confetti al finalizar compra


# Semana 8

## Historia de Usuario — Fer

**Como** desarrollador del proyecto SmartRoast,

**quiero** completar el funcionamiento del carrito entre las distintas páginas del sitio,

**para** que el usuario pueda conservar sus productos seleccionados y visualizar correctamente el resumen de compra.

### Tareas

* Guardar información del carrito en localStorage.
* Recuperar información al cargar las páginas.
* Mantener actualizado el contador de la navbar.
* Mostrar productos agregados en `carrito.html`.
* Mostrar total calculado automáticamente.
* Implementar botón "Vaciar carrito".
* Corregir errores y probar flujo completo.

### Criterios de aceptación

* El contador se actualiza correctamente al agregar productos.
* Los productos permanecen al navegar entre páginas.
* El carrito muestra el detalle completo de la compra.
* El total se calcula automáticamente.
* El usuario puede vaciar el carrito.

---

## Issues — Fer

### #13 Guardar datos del carrito en localStorage

* Guardar:

  * cantidadProductos
  * total
  * detalle

### #14 Recuperar datos al cargar la página

* Leer datos desde localStorage.
* Inicializar variables.

### #15 Mantener actualizado el contador global

* Actualizar el contenido de `#cart-count`.

### #16 Mostrar detalle de compra

* Completar el contenido de `#detalle-carrito`.

### #17 Mostrar total de compra

* Completar el contenido de `#total-carrito`.

### #18 Implementar botón Vaciar carrito

* Reiniciar variables.
* Limpiar localStorage.
* Actualizar interfaz.

### #19 Probar flujo completo

* Agregar productos.
* Cambiar entre páginas.
* Verificar persistencia.
* Verificar cálculo del total.

---

# Historia de Usuario — Magalí

**Como** responsable visual del proyecto SmartRoast,

**quiero** mejorar la presentación visual del catálogo y del carrito,

**para** ofrecer una experiencia de usuario clara, moderna y adaptable a distintos dispositivos.

### Tareas

* Mejorar el diseño de las tarjetas de productos.
* Revisar la presentación de imágenes.
* Mejorar la apariencia de los botones.
* Diseñar la visualización del carrito.
* Revisar el comportamiento responsive del sitio.
* Mantener coherencia visual entre las páginas.
* Preparar estilos para el estado vacío del carrito.

### Criterios de aceptación

* El catálogo presenta productos de forma clara y atractiva.
* Las imágenes mantienen una apariencia uniforme.
* El carrito tiene una presentación visual organizada.
* Los botones poseen feedback visual.
* El sitio se adapta correctamente a celular y escritorio.
* La estética es consistente en todas las páginas.

---

## Issues — Magalí

### #10 Mejorar diseño de las cards del catálogo

* Revisar márgenes y espaciados.
* Mejorar alineación del contenido.
* Revisar tamaños de títulos y precios.

### #11 Unificar imágenes de productos

* Revisar proporciones.
* Mantener altura uniforme en todas las cards.
* Corregir imágenes que deformen el diseño.

### #12 Mejorar diseño de botones

* Personalizar botón "Agregar al carrito".
* Personalizar botones del checkout.
* Agregar estados hover.

### #13 Diseñar visualmente el carrito

* Mejorar presentación de productos agregados.
* Mejorar presentación del total.
* Mejorar acciones del usuario.

### #14 Implementar responsive del catálogo

* Revisar visualización en móvil.
* Revisar visualización en tablet.
* Ajustar separación entre cards.

### #15 Implementar responsive del carrito

* Revisar comportamiento de botones.
* Revisar contenedor principal.
* Ajustar textos y espaciados.

### #16 Crear estado vacío del carrito

Mostrar un mensaje cuando no existan productos agregados:

> Tu carrito está vacío. Explorá nuestro catálogo para comenzar tu pedido.

### #17 Mejorar coherencia visual general

* Revisar colores.
* Revisar tipografías.
* Revisar espaciados.
* Mantener identidad visual SmartRoast.
