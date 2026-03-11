# 11.2. Componentes Funcionales

**PDF: páginas 42–42** (libro: 38–38)

---

[← Índice](README.md) | [← Anterior: 11.1. Componentes De Clase](11-01-componentes-de-clase.md) | [Siguiente: 12. Expresiones →](12-00-expresiones.md)

---

Los componentes funcionales, como su nombre indica, son funciones. Estas funciones reciben como
parámetro las propiedades y tienen que devolver la estructura de TSX que le indica a React que
tiene que pintar en el navegador cuando utilizamos este componente.

```tsx
const HolaMundo = (props) => (
  <h1>Hola mundo</h1>
)

export default HolaMundo;
```
Antiguamente estos componentes eran únicamente presentacionales, es decir, que solo se usaban
para pintar datos en el navegador ya que no podían gestionar un estado ni se podía utilizar los
métodos del ciclo de vida con ellos.

Esto ha cambiado con los React Hooks, ya que podemos tener todo lo que tenemos con los
componentes de clase pero en una función.

Ahora estos componentes son los más utilizados ya que además de poder hacer lo mismo que con
los de clase tenemos otras ventajas:

- Evitamos el uso del objeto this que puede dar problemas.

- Escribimos mucho menos código por lo tanto son más legibles.

- Más fáciles de entender para alguien que empieza a usar React.