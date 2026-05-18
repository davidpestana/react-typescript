# 14.1. Valores Por Defecto

**PDF: páginas 46–46** (libro: 42–42)

---

React nos permite darles valores por defecto a las propiedades que reciben los componentes de tal
forma que no sea necesario pasarselas siempre.

Para añadir los valores por defecto, hay que desestructurar las propiedades y asignarle estos
valores.

```tsx
const MiComponente = ({ miNum = 0, miTexto = 'Hola mundo!' }) => {
  // Código aquí
}
```
A la hora de pintar los componentes se utilizarán estas propiedades si no se las pasamos. En caso de
pasarle estas propiedades, las nuevas sobreescribirán a las que habíamos definido como valores
iniciales.

Antiguamente se podían añadir los valores por defecto usando defaultProps, pero
esto se deprecó en React 17, y ya no funciona.

 MiComponente.defaultProps = {
```tsx
  miNum: 0,
  miTexto: 'Hola mundo!'
}
```
