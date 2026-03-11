# 21. Referencias

**PDF: páginas 100–100** (libro: 96–96)

---

## Referencias

Las referencias de React nos permiten acceder a los elementos del DOM. Equivaldrían a utilizar
métodos como getElementById o querySelector del objeto window.document, pero como aquí
estamos trabajando con un Virtual DOM, tenemos que evitar esos métodos a toda costa ya que
pueden llegar a darnos algún problema.

Con las referencias, al poder acceder a los elementos HTML que se renderizan con los
componentes, podremos acceder y modificar los atributos de estos.

Antes de ponernos a crear referencias en nuestros componentes, para poder acceder a ellos,
tenemos que pensar en que si una etiqueta HTML necesita ser cambiada, los más recomendable
sería cambiar el valor del estado para que vuelva a renderizarse con el nuevo valor. Solo
deberíamos de usar las referencias cuando no tenemos otra forma de modificar dichos elementos.

```tsx
Para crear una referencia usaremos el método React.createRef() que asignaremos a una
```
propiedad de la clase dentro del constructor.

constructor(props) {
```tsx
  super(props);
  this.miReferencia = React.createRef();
}
```
Una vez hecho esto, tendremos que asociarla a un elemento de nuestro componente dándole esta
propiedad como valor mediante el atributo ref.

```tsx
<input type="text" ref={this.miReferencia} />
```
Una vez que tenemos una referencia asociada a uno de los elementos HTML de la vista, podemos
acceder a través de la propiedad que tiene como valor la referencia, y a través de current
podremos acceder a todos los atributos de dicho elemento HTML.

```tsx
console.log(this.miReferencia.current.value);
```
