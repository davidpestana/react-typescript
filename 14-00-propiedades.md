# 14. Propiedades

**PDF: páginas 45–45** (libro: 41–41)

---

[← Índice](README.md) | [← Anterior: 13. Estilos](13-00-estilos.md) | [Siguiente: 14.1. Valores Por Defecto →](14-01-valores-por-defecto.md)

---

## Propiedades

Trabajar con componentes nos permite tener piezas de código que podemos reutilizar en nuestra
aplicación. Pero necesitamos conocer otro concepto más para poder hacer que estos componentes
se puedan reutilizar a un mayor nivel, pudiendo configurarlos para que reciban ciertos valores que
se utilizarán internamente en ellos.

Estos valores que van a recibir desde el exterior son las propiedades, unos atributos que podemos
poner en los componentes (al igual que los atributos de las etiquetas HTML) y que nos permiten
pasar valores desde componentes que están por encima del componente que las va a recibir.

```tsx
<MiComponente prop1="Un texto" prop2={3} prop3 />
```
Los valores de las propiedades no se pueden modificar. Entonces si necesitamos cambiar el valor
de una propiedad que ha recibido nuestro componente, no podremos hacerlo. Lo que si podemos
hacer es enviarle el nuevo valor a la propiedad para que el componente se actualice con dicho
valor.

Los componentes de clase las reciben como parámetro del constructor y usaremos this.props para
acceder a las propiedades.

```tsx
class MiComponente extends Component {
  constructor(props) {
    super(props);
    // ...
  }

    render() {
      const { prop1, prop2, prop3 } = this.props;
      return (...)
    }
}
```
Mientras que en los componentes funcionales las recibiremos como parámetros de la función.

```tsx
const MiComponente = (props) => {
  const { prop1, prop2, prop3 } = props;

    return (...)
}
```
Cada vez que se produce un cambio en una propiedad, se vuelven a renderizar los componentes a
los que afecta dicho cambio.