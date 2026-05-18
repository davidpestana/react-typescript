# 8.1. Lab Proyecto Inicial Desde 0

**PDF: páginas 22–33** (libro: 18–29)

---

En este laboratorio vamos a crear un primer proyecto de React configurando desde 0 webpack y
babel.

Empezamos creando una carpeta reactjs-proyecto-inicial-lab, entramos en ella y vamos a
inicializar un proyecto de NPM.

```tsx
$ mkdir reactjs-proyecto-inicial-lab
$ cd reactjs-proyecto-inicial-lab
$ npm init -y
```
Ahora vamos a instalar con NPM las dependencias que vamos a necesitar en nuestro proyecto. Para
un proyecto de React, como mínimo necesitaremos tener las siguientes:

- React y ReactDOM

- Babel

- Webpack

De React y ReactDOM las vamos a instalar como dependencias de producción con el siguiente
comando:

```tsx
$ npm install --save react react-dom
```
Una vez instaladas estas, vamos a instalar las que necesitaremos de la parte de webpack, estas
como dependencias de desarrollo:

```tsx
$ npm install --save-dev webpack webpack-cli webpack-dev-server
```
Ahora es el turno de las dependencias de Babel, también como dependencias de desarrollo:

```tsx
$ npm install --save-dev @babel/core @babel/preset-env @babel/preset-react @babel/plugin-transform-runtime
```
Y por último, vamos a instalar los loaders y plugins que necesitaremos utilizar con Webpack/Babel
también como dependencias de desarrollo:

```tsx
$ npm install --save-dev babel-loader css-loader style-loader html-webpack-plugin
```
Una vez que tenemos instaladas todas las dependencias que necesitaremos durante el curso, vamos
a empezar a configurar webpack y a explicar para que sirven estas dependencias.

Lo primero que haremos será crear un archivo webpack.config.js en la raíz de la carpeta en el que
vamos a empezar importando el módulo path de node y exportando un módulo en el que
añadiremos la configuración de webpack.

**Archivo:** `/reactjs-proyecto-inicial-lab/webpack.config.js`

```tsx
const path = require('path');

module.exports = {
```
Webpack necesita que le indiquemos cual va a ser el punto de entrada a nuestra aplicación y cual
será la salida. Con punto de entrada me refiero al archivo por el que webpack tiene que empezar a
procesar el código de la aplicación, mientras que con punto de salida estaríamos indicando en que
lugar va a dejar webpack los archivos finales que genera a partir del punto de entrada.

Utilizaremos el paquete path para generar la ruta a los directorios de estos dos puntos, el de
entrada y el de salida. Y luego dentro de la configuración, indicaremos que archivo es el principal y
que archivo tiene que generar.

**Archivo:** `/reactjs-proyecto-inicial-lab/webpack.config.js`

```tsx
const path = require('path');

const entryPath = path.join(__dirname, 'src'),
      outputPath = path.join(__dirname, 'dist');

module.exports = {
  entry: path.join(entryPath, 'index.js'),
  output: {
     path: outputPath,
     filename: 'bundle.js'
  },
}
```
Ahora vamos a añadir el modo por defecto para el que queremos que webpack procese los archivos
de la aplicación, podemos utilizar development o production. Dejaremos como valor por defecto,
development, y luego añadiremos un script de NPM para poder generar también la versión de
producción.

**Archivo:** `/reactjs-proyecto-inicial-lab/webpack.config.js`

```tsx
const path = require('path');

const entryPath = path.join(__dirname, 'src'),
      outputPath = path.join(__dirname, 'dist');

module.exports = {
  mode: 'development',
  entry: path.join(entryPath, 'index.js'),
  output: {
    path: outputPath,
    filename: 'bundle.js'

    },
}
```
Ahora toca añadir la configuración de los loaders que queremos aplicar sobre el código que va a
```tsx
procesar webpack. Estos loaders se configuran en module.rules que es un array en el que
```
pasaremos como valores objetos donde definiremos que loaders queremos utilizar y sobre que
archivos queremos utilizarlos.

Empezaremos indicándole que tiene que aplicar el babel-loader sobre los archivos que tengan la
extensión js o jsx. Este loader se encargará de transformar el código de JSX a JavaScript, y de pasar
el código de JavaScript moderno a código más antiguo para que los navegadores puedan ejecutarlo
sin problemas.

Cada una de las reglas en las que pondremos los loaders tienen una serie de propiedades que
pondremos. Estas son:

- test: expresión regular para indicar a que archivos aplicar la regla.

- exclude: expresión regular para indicar que carpetas excluir para no aplicar las modificaciones
que se indican con esta regla.

- use: el loader o los loaders que queremos utilizar.

**Archivo:** `/reactjs-proyecto-inicial-lab/webpack.config.js`

```tsx
const path = require('path');

const entryPath = path.join(__dirname, 'src'),
      outputPath = path.join(__dirname, 'dist');

module.exports = {
  mode: 'development',
  entry: path.join(entryPath, 'index.js'),
  output: {
     path: outputPath,
     filename: 'bundle.js'
  },
  module: {
     rules: [
       {
          test: /\.(js|jsx)$/,
          exclude: /node_modules/,
          use: 'babel-loader'
       },
     ]
  }
}
```
Una vez que tenemos la regla configurada, cuando ejecutemos webpack y se encuentre con que
tiene que aplicar el babel-loader, webpack buscará la configuración babel para saber que
transformaciones tiene que realizar sobre el código de JavaScript.

Vamos a crear un archivo .babelrc con la configuración de babel. Dentro de este archivo vamos a
indicarle que utilice los presets de @babel/preset-env y @babel/preset-react, además del plugin
@babel/plugin-transform-runtime.

- @babel/preset-env: conjunto de plugins que se encargan de transformar el código moderno de
JavaScript a otras versiones más antiguas del lenguaje para que se pueda ejecutar en los
distintos navegadores.

- @babel/preset-react: conjunto de plugins que se encargan de transformar el JSX en JavaScript.

◦ La opción runtime: automatic la añadimos para no tener que importar React en los
distintos componentes de la aplicación.

- @babel/plugin-transform-runtime: nos permitirá utilizar la sintaxis async/await dentro del
```tsx
hook useEffect.
```
/reactjs-proyecto-inicial-lab/.babelrc

```tsx
{
    "presets": [
       "@babel/preset-env",
       [
         "@babel/preset-react",
         {
           "runtime": "automatic"
         }
       ]
    ],
    "plugins": [
       "@babel/plugin-transform-runtime"
    ]
}
```
Con esto ya tendríamos configurada la parte de babel.

Ahora toca añadir una nueva regla que se va a encargar de coger los archivos de CSS que procese
webpack para añadir este CSS en la cabecera del index.html.

Esta nueva regla apuntará a los archivos de CSS y utilizaremos dos loaders:

- style-loader: coge el código de CSS y lo añade dentro de etiquetas style en el head de la página
de HTML.

- css-loader: permite importar CSS como si fueran módulos de JavaScript, de esta forma webpack
podrá procesar este código.

**Archivo:** `/reactjs-proyecto-inicial-lab/webpack.config.js`

```tsx
const path = require('path');

const entryPath = path.join(__dirname, 'src'),
      outputPath = path.join(__dirname, 'dist');

module.exports = {
  mode: 'development',
  entry: path.join(entryPath, 'index.js'),
  output: {
     path: outputPath,
     filename: 'bundle.js'
  },
  module: {
     rules: [
       {
          test: /\.(js|jsx)$/,
          exclude: /node_modules/,
          use: 'babel-loader'
       },
       {
          test: /\.css$/,
          exclude: /node_modules/,
          use: ['style-loader', 'css-loader']
       },
     ]
  }
}
```
Es probable que utilicemos algún archivo de video en alguno de los laboratorios que haremos
durante el curso, así que vamos a añadir una regla más con la que se copiarán estos archivos a la
carpeta de distribución. Esta vez no utilizaremos un loader sino una de las nuevas funcionalidades
añadidas en webpack 5, los asset modules.

**Archivo:** `/reactjs-proyecto-inicial-lab/webpack.config.js`

```tsx
const path = require('path');

const entryPath = path.join(__dirname, 'src'),
      outputPath = path.join(__dirname, 'dist');

module.exports = {
  mode: 'development',
  entry: path.join(entryPath, 'index.js'),
  output: {
     path: outputPath,
     filename: 'bundle.js'
  },
  module: {
     rules: [
       {
          test: /\.(js|jsx)$/,
          exclude: /node_modules/,
          use: 'babel-loader'
       },
       {

                test: /\.css$/,
                exclude: /node_modules/,
                use: ['style-loader', 'css-loader']
            },
            {
                test: /\.(mp3|mp4)$/,
                exclude: /node_modules/,
                type: 'asset/resource'
            }
        ]
    }
}
```
Con esto ya hemos terminado con las reglas de webpack, ahora vamos a añadir la configuración del
plugin html-webpack-plugin.

Este plugin se encarga de crear un index.html en la carpeta de distribución, a partir de una
plantilla dada.

Tendremos que importarlo en nuestro archivo, y añadir una nueva sección plugins en la
configuración. En la sección de plugins, vamos a crear una instancia del plugin a la que le
pasaremos un objeto de configuración indicando donde se encuentra la plantilla del archivo y
algunas opciones extra.

**Archivo:** `/reactjs-proyecto-inicial-lab/webpack.config.js`

```tsx
const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');

const entryPath = path.join(__dirname, 'src'),
      outputPath = path.join(__dirname, 'dist');

module.exports = {
  mode: 'development',
  entry: path.join(entryPath, 'index.js'),
  output: {
     path: outputPath,
     filename: 'bundle.js'
  },
  module: {
     rules: [
       {
          test: /\.(js|jsx)$/,
          exclude: /node_modules/,
          use: 'babel-loader'
       },
       {
          test: /\.css$/,
          exclude: /node_modules/,
          use: ['style-loader', 'css-loader']

        },
        {
            test: /\.(mp3|mp4)$/,
            exclude: /node_modules/,
            type: 'asset/resource'
        }
       ]
    },
    plugins: [
       new HtmlWebpackPlugin({
          title: 'Curso de React',
          template: path.join(entryPath, 'index.html')
       })
    ],
}
```
Ahora toca añadir la sección devServer en la que indicaremos con static, donde se encuentra el
contenido que tendría que servirse, en este caso por nuestro servidor de desarrollo que es
webpack-dev-server

**Archivo:** `/reactjs-proyecto-inicial-lab/webpack.config.js`

```tsx
const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');

const entryPath = path.join(__dirname, 'src'),
      outputPath = path.join(__dirname, 'dist');

module.exports = {
  mode: 'development',
  entry: path.join(entryPath, 'index.js'),
  output: {
     path: outputPath,
     filename: 'bundle.js'
  },
  module: {
     rules: [
       {
          test: /\.(js|jsx)$/,
          exclude: /node_modules/,
          use: 'babel-loader'
       },
       {
          test: /\.css$/,
          exclude: /node_modules/,
          use: ['style-loader', 'css-loader']
       },
       {
          test: /\.(mp3|mp4)$/,
          exclude: /node_modules/,

              type: 'asset/resource'
          }
      ]
    },
    plugins: [
       new HtmlWebpackPlugin({
          title: 'Curso de React',
          template: path.join(entryPath, 'index.html')
       })
    ],
    devServer: {
       static: outputPath
    },
}
```
Y para terminar con la configuración de webpack, vamos a añadir una sección más,
resolve.extensions a la que le vamos a pasar un array de extensiones, indicando con ello que a la
hora de importar cualquier archivo pueda resolverlo automáticamente con estas extensiones, sin
que tengamos que ponerlas en la importación.

**Archivo:** `/reactjs-proyecto-inicial-lab/webpack.config.js`

```tsx
const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');

const entryPath = path.join(__dirname, 'src'),
      outputPath = path.join(__dirname, 'dist');

module.exports = {
  mode: 'development',
  entry: path.join(entryPath, 'index.js'),
  output: {
     path: outputPath,
     filename: 'bundle.js'
  },
  module: {
     rules: [
       {
          test: /\.(js|jsx)$/,
          exclude: /node_modules/,
          use: 'babel-loader'
       },
       {
          test: /\.css$/,
          exclude: /node_modules/,
          use: ['style-loader', 'css-loader']
       },
       {
          test: /\.(mp3|mp4)$/,
          exclude: /node_modules/,

              type: 'asset/resource'
          }
      ]
    },
    plugins: [
       new HtmlWebpackPlugin({
          title: 'Curso de React',
          template: path.join(entryPath, 'index.html')
       })
    ],
    devServer: {
       static: outputPath
    },
    resolve: {
       extensions: ['.js', '.jsx']
    }
}
```
Ya hemos terminado con la configuración de webpack. Ahora tenemos que crear la estructura de
carpetas y archivos en base a lo que hemos configurado aquí.

Como hemos indicado que el HTML se va a generar a partir de una plantilla index.html, vamos a
añadirla dentro de una carpeta src.

Importante poner un div con un identificador (normalmente se suele poner app o root) para
indicar donde se tiene que montar el componente raíz de la aplicación.

**Archivo:** `/reactjs-proyecto-inicial-lab/src/index.html`

```tsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title><%= htmlWebpackPlugin.options.title %></title>
</head>
<body>
  <div id="root"></div>
</body>
</html>
```
En la configuración de webpack una de las primeras opciones que hemos añadido ha sido la del
punto de entrada a la aplicación, y todavía no tenemos este archivo, así que vamos a crearlo.
```tsx
Crearemos dentro de src un archivo index.js en el que vamos a importar createRoot y lo
```
utilizaremos para renderizar un componente App, que vamos a crear después, dentro del div que
hay en el index.html con el identificador root.

**Archivo:** `/reactjs-proyecto-inicial-lab/src/index.js`

```tsx
import { createRoot } from 'react-dom/client';
import App from './components/App';

createRoot(document.getElementById('root')).render(<App />);
```
Ahora vamos a crear nuestro primer componente, un archivo App.jsx dentro de la carpeta
src/components. En un laboratorio posterior veremos que hace el siguiente código.

**Archivo:** `/reactjs-proyecto-inicial-lab/src/components/App.jsx`

```tsx
const App = () => {
  return (
    <div>
      <h1>Hola mundo!!!</h1>
    </div>
  )
}

export default App
```
Y para terminar, vamos a dejar un archivo style.css dentro de la carpeta src que vamos a importar
en el punto de entrada. Este archivo lo dejaremos creado para ver el tema de estilos con CSS en un
laboratorio más adelante.

**Archivo:** `/reactjs-proyecto-inicial-lab/src/index.js`

```tsx
import { createRoot } from 'react-dom/client';
import App from './components/App';
import './style.css';

createRoot(document.getElementById('root')).render(<App />);
```
Ya tenemos todos los archivos del proyecto, pero nos falta algo importante, probar que todo lo que
hemos hecho hasta ahora funcione. Para ello tenemos que levantar la aplicación con el servidor de
desarrollo, o generar la carpeta de distribución con el código de la aplicación.

Estas tareas las haremos mediante scripts de NPM, por lo que vamos a añadir 3 scripts dentro del
archivo package.json:

- webpack serve se encarga de levantar la aplicación en el puerto 8080 (por defecto) utilizando
webpack-dev-server.

- webpack se encarga de generar el código final en una carpeta dist con la configuración del
modo development.

- webpack --mode=production hace lo mismo que el script anterior, pero con la configuración
del modo production.

**Archivo:** `/reactjs-proyecto-inicial-lab/package.json`

```tsx
{
    "name": "reactjs-proyecto-inicial-lab",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
       "start": "webpack serve",
       "build": "webpack --mode=development",
       "build:prod": "webpack --mode=production"
    },
```
"keywords": [],
```tsx
    "author": "",
    "license": "ISC",
    "devDependencies": {
       "@babel/core": "^7.17.12",
       "@babel/preset-env": "^7.17.12",
       "@babel/preset-react": "^7.17.12",
       "babel-loader": "^8.2.5",
       "css-loader": "^6.7.1",
       "html-webpack-plugin": "^5.5.0",
       "style-loader": "^3.3.1",
       "webpack": "^5.72.1",
       "webpack-cli": "^4.9.2",
       "webpack-dev-server": "^4.9.0"
    },
    "dependencies": {
       "react": "^18.1.0",
       "react-dom": "^18.1.0"
    }
}
```
Una vez añadidos, podemos lanzar el siguiente comando y comprobar que si entramos en
http://localhost:8080/ vemos el mensaje que hemos puesto en el componente App:

```tsx
$ npm start
```
Con esto ya tenemos un proyecto de react con webpack y babel configurado desde 0. A este
proyecto se le pueden añadir muchas más opciones de webpack para que realice otro tipo de tareas
sobre el código como:

- Extracción de archivos CSS

- Optimización de imagenes

- Separar configuración de webpack por entornos

- Activar el hot module replacement

- …

Pero con lo que hemos configurado nos vale para continuar con el curso.
