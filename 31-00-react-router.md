# 31. React Router

**PDF: páginas 215–215** (libro: 211–211)

---

[← Índice](README.md) | [← Anterior: 30.6. Middleware](30-06-middleware.md) | [Siguiente: 31.1. Instalacion Router →](31-01-instalacion-router.md)

---

## React Router

El routing es lo que nos va a permitir cambiar entre las distintas páginas de nuestra aplicación,
pero recordad que estamos ante aplicaciones de una sola página (SPAs), es decir, aplicaciones que
solo tienen una única página de HTML, por lo que no tiene sentido cambiar de página cada vez que
cambiamos de URL. En este caso, el routing funciona un poco diferente a como se hacía con las
MPAs (Multi-Page Applications), ahora, lo que se cambia es el contenido a mostrar por la página
index.html, que serán nuestros componentes.

React al ser una librería y no un framework no lo trae consigo, pero para poder añadirlo a nuestras
aplicaciones usaremos la librería de React Router que nos permitirá añadir rutas a nuestra
aplicación y se encargará de cambiar entre los distintos componentes asociados a estas rutas.