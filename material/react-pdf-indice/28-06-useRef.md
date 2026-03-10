# 28.6. Useref

**PDF: páginas 168–168** (libro: 164–164)

---

El hook useRef nos permite crear una referencia a etiquetas HTML del componente para así poder
acceder a sus propiedades y métodos internos.

Este hook recibe como parámetro el valor inicial con el cual queremos inicializar la propiedad
current de la referencia. Y devuelve la referencia para asignarla a aquella etiqueta HTML con la
que queramos interactuar.

```tsx
const ref = useRef(valorInicial)
```
Para asignarla a una etiqueta y poder acceder a sus atributos internos, solo hay que darle esta
variable como valor del atributo ref de la etiqueta.

```tsx
<video src="video.mp4" ref={ref} />
```
El objeto que nos devuelve el hook es mutable y cualquier cambio sobre el no hace que se renderice
el componente de nuevo.
