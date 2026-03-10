# 28.2. Usestate

**PDF: páginas 147–147** (libro: 143–143)

---

```tsx
El hook useState nos permite añadir estado dentro de nuestros componentes funcionales.
```
Se trata de una función que recibe como parámetro el valor inicial del estado, y que devuelve un
array de dos posiciones, donde la primera es el valor actual del estado, y la segunda es una función
para cambiar dicho estado.

```tsx
const [estadoActual, cambiarEstado] = useState(estadoInicial)

No hace falta meter todo el estado del componente en un useState, sino que podemos usar esta
```
función las veces que lo necesitemos.

```tsx
const [estadoActual1, cambiarEstado1] = useState(estadoInicial1)
const [estadoActual2, cambiarEstado2] = useState(estadoInicial2)
```
