# 20.1. Constructor

**PDF: páginas 85–85** (libro: 81–81)

---

El constructor no es un método del ciclo de vida, sino que es algo propio de las clases de JavaScript.

Este método solo es necesario si:

- Tenemos que inicializar el estado

- Tenemos que enlazar handlers a la instancia del componente

constructor(props) {
```tsx
super(props);

    this.state = {...};
    this.handleEvent = this.handleEvent.bind(this);
}
```
Evita añadir al estado directamente el valor de las propiedades. No tiene sentido,
ya que puedes acceder a ellas con this.props.
Otra cosa es cuando el estado se deriva del valor de estas. Para ello usaremos el
método getDerivedStateFromProps.
