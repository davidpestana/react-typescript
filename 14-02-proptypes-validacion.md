# 14.2. Proptypes Validacion

**PDF: páginas 47–48** (libro: 43–44)

---

[← Índice](README.md) | [← Anterior: 14.1. Valores Por Defecto](14-01-valores-por-defecto.md) | [Siguiente: 14.3. Validacion Propiedades Personalizadas →](14-03-validacion-propiedades-personalizadas.md)

---

En React clásico (sin TypeScript) se usaba la librería **prop-types** para validar en tiempo de
ejecución los tipos de las props de un componente. En este curso, al trabajar con **TypeScript**,
esa validación se hace en **tiempo de compilación** mediante interfaces y tipos, así que **no vamos
a usar PropTypes en nuestros proyectos**.

## PropTypes vs TypeScript

La idea detrás de PropTypes era parecida a lo que hacemos con los tipos en TypeScript:

- **PropTypes.string** ⟶ `prop: string`
- **PropTypes.number** ⟶ `prop: number`
- **PropTypes.bool** ⟶ `prop: boolean`
- **PropTypes.object** ⟶ `prop: Record<string, unknown>`
- **PropTypes.array** ⟶ `prop: unknown[]`
- **PropTypes.func** ⟶ `prop: () => void`
- **PropTypes.oneOfType([PropTypes.number, PropTypes.string])** ⟶ `prop: number | string`
- **PropTypes.arrayOf(PropTypes.string)** ⟶ `prop: string[]`
- **PropTypes.objectOf(PropTypes.number)** ⟶ `prop: Record<string, number>`
- **PropTypes.shape({ nombre: PropTypes.string, edad: PropTypes.number })** ⟶
  `prop: { nombre: string; edad: number }`
- **PropTypes.oneOf(['Gato', 'Perro', 'Canario'])** ⟶ `prop: 'Gato' | 'Perro' | 'Canario'`

En PropTypes, si una validación no se cumple se muestra un **warning en consola** pero la aplicación
sigue funcionando (aunque con datos erróneos). En TypeScript, en cambio, el error se detecta antes
de ejecutar el código.

## Qué hacemos en este curso

En los ejemplos y labs de este material:

- **No instalamos** la dependencia `prop-types`.
- **No definimos** `MiComponente.propTypes`.
- Usamos **interfaces o types** para describir las props, como en el capítulo de
  [Propiedades (props) con tipos](../react-tsx/10-props-con-tipos.md) del material resumido.

De esta forma, mantenemos una única fuente de verdad para los tipos (TypeScript) y evitamos
duplicar la información entre PropTypes y las definiciones de tipos.