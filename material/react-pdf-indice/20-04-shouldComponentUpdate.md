# 20.4. Shouldcomponentupdate

**PDF: páginas 88–88** (libro: 84–84)

---

El método shouldComponentUpdate es un método que se ejecuta justo antes del render.

Este método nos permite indicarle a React si hace falta volver a renderizar el componente o no. Es
un método que se utiliza para mejorar el rendimiento de las aplicaciones ahorrando renderizados
innecesarios de algunos componentes.

Para indicarle a React si tiene que volver a pintar el componente o no, este método tiene que
devolver un valor booleano:

- true: se renderiza

- false: no se renderiza

Para saber si es necesario renderizar el componente vamos a recibir las siguientes propiedades y el
siguiente estado que podremos utilizar para comparar con los valores actuales (antes del render).

shouldComponentUpdate(nextProps, nextState) {
```tsx
  return nextProps.valor !== this.props.valor ? true : false;
}

Si se devuelve false, al no actualizar el componente tampoco se ejecutarán los
```
métodos de render y componentDidUpdate.
