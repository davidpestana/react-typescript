# 7.3. Estructura Proyecto

**PDF: páginas 20–20** (libro: 16–16)

---

[← Índice](README.md) | [← Anterior: 7.2. Scripts Proyecto](07-02-scripts-proyecto.md) | [Siguiente: 7.4. Vite (React con TypeScript) →](07-04-vite.md)

---

El proyecto que nos genera la herramienta CRA tiene la siguiente estructura:

- node_modules: carpeta donde se encuentran todas las dependencias del proyecto.

- public: carpeta de distribución donde encontraremos el código final de la aplicación para
llevarlo a producción.

◦ index.html: única página HTML del proyecto, en la que se inyectará nuestra aplicación.

◦ manifest.json: archivo que habilita el uso de nuestra aplicación como PWA.

◦ robots.txt: archivo para indicar si la web tiene que indexarse o no.

- src: carpeta en la que trabajaremos nosotros para ir generando la aplicación.

◦ App.css: archivo de estilos para el componente App.

◦ App.test.js: archivo de testing del componente App.

◦ App.js: componente App de la aplicación, en este caso es el componente raíz.

◦ index.css: archivo de estilos globales.

◦ index.js: archivo de entrada a la aplicación, encargado de indicar donde se tiene que
inyectar el componente raíz dentro de la página HTML.

◦ serviceWorker.js: archivo en el que configurar algunas funcionalidades de las PWAs como el
uso de notificaciones.

◦ setupTests.js: archivo en el que podemos añadir nuestros propios métodos de expect para
los tests.

- .gitignore: archivo que le indica a Git que archivos y carpetas tiene que ignorar.

- package.json: archivo con la información del proyecto (versión, dependencias, scripts…).