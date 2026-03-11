# 7.2. Scripts Proyecto

**PDF: páginas 19–19** (libro: 15–15)

---

[← Índice](README.md) | [← Anterior: 7.1. Lab Create React App](07-01-lab-create-react-app.md) | [Siguiente: 7.3. Estructura Proyecto →](07-03-estructura-proyecto.md)

---

Dentro del proyecto de create-react-app podemos lanzar una serie de comandos que vamos a ver a
continuación. Estos comandos los podemos encontrar en el archivo package.json.

"scripts": {
```tsx
  "start": "react-scripts start",
  "build": "react-scripts build",
  "test": "react-scripts test",
  "eject": "react-scripts eject"
}
```
- start

Podemos lanzar el siguiente comando para levantar la aplicación en el servidor de desarrollo:

```tsx
$ npm start
```
- build

Podemos lanzar el siguiente comando para generar el código que pondremos en producción:

```tsx
$ npm run build
```
- test

Podemos lanzar el siguiente comando para ejecutar todos los archivos de testing con Jest:

```tsx
$ npm test
```
- eject

Podemos lanzar el siguiente comando para sacar los archivos de configuración fuera de los
módulos donde se encontraban:

```tsx
$ npm run eject
```