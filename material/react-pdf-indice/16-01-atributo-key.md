# 16.1. Atributo Key

**PDF: páginas 57–58** (libro: 53–54)

---

A la hora de generar listas de componentes o etiquetas con React hay que tener en cuenta otro
concepto más, el atributo key.

Si hemos generado una lista podremos ver en la consola un warning que dice Warning: Each child
in a list should have a unique "key" prop..

Aquí nos indican que hay que ponerle a cada componente que generamos en la lista un atributo
key y dicho valor tiene que ser único dentro de la lista.

```tsx
items.map((item, pos) => <li key={pos}>{item.texto}</li>)
```
En el código de encima estamos usando la posición de los elementos como valor
 del atributo key, y esto es algo que soluciona el warning pero que no está bien del
todo.

En React nos recomiendan que no utilicemos la posición como key, por tanto lo mejor sería utilizar
un identificador único (que normalmente suelen tener todos los objetos).

```tsx
items.map(item => <li key={item.id}>{item.texto}</li>)
```
Tenemos que utilizar este atributo para ayudar a React a que cualquier cambio sobre la lista se
realice de la forma más eficiente posible.

Cada vez que se modifique la lista, React va a ir comparando los valores de los atributos key para
saber si ese elemento ya estaba pintado o si es el que hay que pintar, o si hay que eliminar un
elemento de esta, evitando tener que volver a pintar la lista entera desde 0 cada vez que cambia.

Podemos comprobar en los siguientes enlaces los problemas que pueden ocasionarnos no poner

bien las keys:

- Usando la posición: https://es.reactjs.org/redirect-to-codepen/reconciliation/index-used-as-key

- Usando un identificador único: https://es.reactjs.org/redirect-to-codepen/reconciliation/no-
index-used-as-key
