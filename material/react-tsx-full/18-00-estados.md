# 18. Estados

**PDF: páginas 66–67** (libro: 62–63)

---

[← Índice](README.md) | [← Anterior: 17.2. Lab Eventos](17-02-lab-eventos.md) | [Siguiente: 18.1. Lab Estado →](18-01-lab-estado.md)

---

## Estados

Como hemos dicho antes, las propiedades no cambian, y necesitamos un mecanismo por el que
podamos volver a renderizar los componentes con una propiedades nuevas. Este mecanismo son
los estados, y una vez que el estado cambia vuelve a lanzar el render para mostrar esos cambios.

El estado es mutable sólo por el propio componente donde se ha definido, ni el componente padre
ni los componentes hijos podrán modificar su valor.

Podemos enviarle datos que tenemos en el estado de un componente a los componentes hijos en
forma de props.

En React los estados son opcionales, y podemos diferenciar los componentes en componentes que
no tienen estado y aquellos que si lo tienen.

Una buena práctica es mantener la mayor parte de los componentes sin estado.

El estado de un componente de clase se inicializa en el constructor del componente y es un objeto
de JavaScript en el que le vamos a dar unos valores por defecto. El método constructor() recibe
como paŕametro las props que le envía el componente padre. Dentro del constructor usamos
super() para inicializar la instancia del componente y Component le va a añadir funcionalidad
para poder manejar los cambios de estado.

```tsx
class MiComponente extends Component {
  constructor(props) {
    super(props);
    this.state = {
      clave: 'valor'
    }
  }

    render() {
      return (
        <div>Contador: {this.state.clave}</div>
      )
    }
}
```
Para cambiar el estado hay que usar el método setState() que recibe un objeto con los atributos
que se van a modificar, y una vez que se ha realizado la modificación del estado, lanza un nuevo
render para actualizar la interfaz de usuario.

this.setState({
```tsx
   clave: 'nuevoValor'
})
```
Para ver como añadir el estado en los componentes funcionales tenemos que ir al

```tsx
tema de React Hooks, concretamente al hook de useState.
```