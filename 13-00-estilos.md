# 13. Estilos

**PDF: páginas 44–44** (libro: 40–40)

---

[← Índice](README.md) | [← Anterior: 12. Expresiones](12-00-expresiones.md) | [Siguiente: 14. Propiedades →](14-00-propiedades.md)

---

## Estilos

React lo que intenta es que cada componente tenga todo lo necesario para pintarlo en el navegador,
y esto incluye también los estilos. React nos permite escribir estilos en linea usando la sintaxis de
TSX, que puede parecer un poco extraño pero tiene algunos beneficios sobre el CSS.

Por ejemplo, se evita los conflictos de especificidad, no tenemos que usar selectores, al usar
JavaScript, podemos usar variables para hacerlos más dinámicos, también funciones e incluso
estructuras de control de flujo para dar unos estilos u otros…

Los estilos van a ser objetos JavaScript, cuyos atributos son las propiedades de CSS y se escriben en
camelCase.

```tsx
const estilos = {
  backgroundColor: '#242424',
  width: '100%',
  height: '50px',
}

<div style={estilos}>
</div>
```
Por supuesto, estos estilos son locales al componente, y podemos aplicar estilos que se encuentran
definidos en un archivo externo asignando las clases (className) correctas al componente.

En este caso tenemos que tener en cuenta que el archivo de CSS se tiene que importar en el
index.html, o los tiene que gestionar Webpack con los loaders adecuados para ello:

- css-loader

- style-loader

- sass-loader

- postcss-loader

- …