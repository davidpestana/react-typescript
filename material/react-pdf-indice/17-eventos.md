# 17. Eventos

**PDF: páginas 62–62** (libro: 58–58)

---

## Eventos

React no usa los eventos nativos, sino que utilizaremos los eventos sintéticos que han
implementado. Estos eventos son un wrapper sobre los eventos nativos y se han encargado de
normalizar los eventos para que funcionen en todos los navegadores de la misma forma.

Estos eventos tienen la misma API que los nativos, por lo que podremos acceder a las mismas
propiedades a las que accederíamos en los eventos nativos.

Para poder usar estos eventos tenemos que ponerlos en las etiquetas con forma de camelCase.

Además React se encarga de eliminar automáticamente los EventListeners una vez que se
desmonta el componente.
