# 14.2. Proptypes Validacion

**PDF: páginas 47–48** (libro: 43–44)

---

[← Índice](README.md) | [← Anterior: 14.1. Valores Por Defecto](14-01-valores-por-defecto.md) | [Siguiente: 14.3. Validacion Propiedades Personalizadas →](14-03-validacion-propiedades-personalizadas.md)

---

Las propiedades que reciben los componentes se pueden validar para asegurarnos de que nuestros
componentes reciben los tipos de datos esperados.

Antiguamente se podían validar los tipos de las propiedades con la librería prop-
 types, pero esto se deprecó, y ya no funciona. Ahora habría que utilizar
TypeScript para las validaciones de tipos.

Algunas de las validaciones que podemos utilizar son:

Validador Descripción

PropTypes.isRequired La propiedad tiene que ser obligatoria

PropTypes.string La propiedad tiene que ser un string

PropTypes.number La propiedad tiene que ser un número

PropTypes.bool La propiedad tiene que ser un booleano

PropTypes.object La propiedad tiene que ser un objeto

PropTypes.array La propiedad tiene que ser un array

PropTypes.func La propiedad tiene que ser una función

PropTypes.oneOfType([PropTypes.number, La propiedad tiene que ser de uno de esos tipos
PropTypes.string])

PropTypes.arrayOf(PropTypes.string) La propiedad tiene que ser un array de string

PropTypes.objectOf(PropTypes.number) La propiedad tiene que ser un objeto cuyos
atributos sean números

PropTypes.shape({nombre: PropTypes.string, La propiedad tiene que ser un objeto que tiene
edad: PropTypes.number}) que tener un atributo nombre de tipo string y un
atributo edad de tipo número

PropTypes.oneOf(['Gato', 'Perro', 'Canario']) La propiedad tiene que ser uno de los valores del
enumerado

Cuando una validación no se cumple, se muestra un warning por la consola, y la
aplicación seguirá funcionando aunque esto no quiere decir que funcione como se
espera ya que puede ser que el tipo de dato no sea el esperado.

Para utilizar las validaciones necesitamos la siguiente dependencia:

```tsx
$ npm install --save prop-types
```
Estas validaciones se asignan a la propiedad propTypes del componente:

```tsx
import PropTypes from 'prop-types';
```
// ...

MiComponente.propTypes = {
```tsx
  miPropiedad: PropTypes.string.isRequired
}
```
Las proptypes también nos sirven de documentación, ya que podremos ver en todo momento que
propiedades puede recibir un componente, si son obligatorias u opcionales, el tipo…