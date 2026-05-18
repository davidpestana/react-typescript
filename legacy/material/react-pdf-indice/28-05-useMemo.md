# 28.5. Usememo

**PDF: páginas 162–162** (libro: 158–158)

---

El hook useMemo va a permitirnos memorizar un valor que se usará en los renderizados de tal
forma que solo se va a volver a calcular cuando alguna de las dependencias que se le han pasado
como segundo parámetro haya sufrido cambios. Como primer parámetro recibe la función que
calcula el valor y lo devuelve, y el hook nos devuelve dicho valor, memorizado o calculado de
nuevo.

```tsx
const valorCalculado = useMemo(() => {
  // val = ...
  return val;
}, [dep1])
```
Este hook sería equivalente a usar el método del ciclo de vida shouldComponentUpdate.
