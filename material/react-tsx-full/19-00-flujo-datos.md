# 19. Flujo Datos

**PDF: páginas 83–83** (libro: 79–79)

---

[← Índice](README.md) | [← Anterior: 18.1. Lab Estado](18-01-lab-estado.md) | [Siguiente: 19.1. Lab Flujo Datos →](19-01-lab-flujo-datos.md)

---

## Flujo de datos

En las aplicaciones de React, los datos que van recibiendo los componentes (las propiedades)
siempre viajan desde arriba hacia abajo, es decir, de componentes padres a componentes hijos.

Estos datos nunca irán en dirección contraria.

Cuando se necesita cambiar el valor de una propiedad que proviene del estado de un componente
definido varios niveles por encima, necesitamos llamar al método setState de dicho componente.
Pero este método no es accesible directamente desde los componentes inferiores, por lo que
pasaremos en forma de propiedades la referencia a las funciones encargadas de cambiar el estado.

Desde el componente inferior que necesite realizar el cambio de estado ejecutará la referencia de la
función que ha recibido como propiedad.