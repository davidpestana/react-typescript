# 16. Listas

**PDF: páginas 56–56** (libro: 52–52)

---

[← Índice](README.md) | [← Anterior: 15. Renderizado Condicional](15-00-renderizado-condicional.md) | [Siguiente: 16.1. Atributo Key →](16-01-atributo-key.md)

---

## Listas

Cuando queremos iterar una lista de datos y generar un componente por cada item que se
encuentra dentro de la lista, tenemos que utilizar el método map de los arrays.

```tsx
Al método map se le pasa como parámetro una función de callback como (item, index) ⇒ {…},
```
donde el primer parámetro será cada elemento del array y el index la posición en la que se
encuentra. Esta función de callback tiene que devolver por cada item un componente o etiqueta de
HTML.

```tsx
items.map(item => <li>{item}</li>)
```