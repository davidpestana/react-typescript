# 28.4. Usecontext

**PDF: páginas 157–157** (libro: 153–153)

---

```tsx
El hook useContext nos permite acceder al contexto creado con React para pasar valores
```
directamente de un componente a otro cuando hay demasiados niveles entre medias de estos
componentes.

Este hook es una función a la que le vamos a pasar como parámetro el contexto que hemos tenido
```tsx
que haber creado con React.createContext, y nos devolverá el valor que se ha dado inicialmente al
```
contexto o el que se ha pasado en la propiedad value del Provider del contexto creado.

```tsx
const Ctx = React.createContext(1);

const num = useContext(Ctx)
```
