# 7.1. Lab Create React App

**PDF: páginas 17–18** (libro: 13–14)

---

[← Índice](README.md) | [← Anterior: 7. Create React App](07-00-create-react-app.md) | [Siguiente: 7.2. Scripts Proyecto →](07-02-scripts-proyecto.md)

---

En este laboratorio vamos a ver como crear un proyecto de React con la herramienta create-react-
app sin la necesidad de tener que configurar nada.

Tenemos dos formas de crear un proyecto con esta herramienta:

- Forma 1: creamos el proyecto directamente usando npx:

```tsx
$ npx create-react-app reactjs-create-react-app-lab
```
- Forma 2: instalamos la herramienta y creamos el proyecto:

```tsx
$ npm install -g create-react-app
$ create-react-app reactjs-create-react-app-lab
```
Una vez lanzados los comandos anteriores, se genera el proyecto de React con el nombre que le
hemos dado (reactjs-create-react-app-lab), y en la consola se nos muestran los distintos comandos
que podemos lanzar:

Success! Created reactjs-create-react-app-lab at /reactjs-create-react-app-lab
Inside that directory, you can run several commands:

yarn start
Starts the development server.

yarn build
Bundles the app into static files for production.

yarn test
Starts the test runner.

yarn eject
Removes this tool and copies build dependencies, configuration files
and scripts into the app directory. If you do this, you can’t go back!

We suggest that you begin by typing:

cd reactjs-create-react-app-lab
yarn start

Happy hacking!

Ahora ya podemos levantar la aplicación lanzando uno de los siguientes comandos dentro de la
carpeta del proyecto:

```tsx
$ yarn start
$ npm start
```
Ahora ya deberíamos de poder ver la aplicación en http://localhost:3000/.