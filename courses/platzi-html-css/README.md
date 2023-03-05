# Curso Definitivo de HTML y CSS

https://platzi.com/clases/2008-html-css/


## Frontend

Frontend es la parte de un programa o dispositivo a la que un usuario puede acceder directamente. Son todas las tecnologías de diseño y desarrollo web que corren en el navegador y que se encargan de la interactividad con los usuarios.

Un programador Frontend debe saber de código que entienda el navegador (HTML, CSS y JavaScript) para poder usar algunos frameworks o librerías que expanden sus capacidades para crear cualquier tipo de interfaces de usuarios. React, Redux, Angular, Bootstrap, Foundation, LESS, Sass, Stylus y PostCSS son algunos de ellos.

Herramientas que maneja un frontend
Debido a que un frontend es el desarrollador (que puede ser o no Full Stack) que va a manejar las cosas del lado del cliente, las tecnologías con las que va a trabajar son:

HTML: https://devdocs.io/html/
CSS: https://devdocs.io/css/
JavaScript: https://devdocs.io/javascript/
Frameworks de CSS para frontend:
Bootstrap: https://getbootstrap.com/
Foundation CSS: https://get.foundation/
Materialize CSS: https://materializecss.com/
Los frameworks de JavaScript para frontend:

React JS: https://es.reactjs.org/
Angular JS: https://angular.io/
Vue JS: https://vuejs.org/
Preprocesadores de CSS:
Stylus: https://stylus-lang.com/
SASS: https://sass-lang.com/
Compiladores / empaquetadores de JS:
BABEL: https://babeljs.io/
Webpack: https://webpack.js.org/
Aporte creado por: Christian Tambo, Manuel Duarte.

Herramientas

Mediaqueri: Algunas ideas sobre como deberíamos implementar el diseño responsive en nuestro sitio.
Coolors: Paletas de colores.
Unsplash: Imagenes gratis (Da los créditos a los fotógrafos 😉).
FontPair: Ver cuales fuentes puedes combinar. Y obviamente Google Fonts para obtener esas fuentes.
Icons8: Iconos, vectores, música y algunos recursos más…

Documentaciones:
CSS
HTML
Browserdiet: Optimizar sitios web (Perder peso en la web 😛). Recuerda que Platzi tiene también un curso de Web Performance
WCAG: Guía para mejorar la accesibilidad de nuestro sitio. Recuerda que Platzi tiene el curso de accesibilidad web.

Practica jugando:
Grid Layout
Flexbox

## Backend

Backend en programación corresponde al lado opuesto a un Front-end en un sitio web o aplicación, ya que el Backend trabaja en el lado del servidor, mientras el Frontend lo hace en el lado del cliente. Es el responsable de manejar toda la lógica que existe detrás de una petición dada por el navegador hacia el servidor. Existen programadores que manejan ambas especialidades y se les conoce como full stack.

Una característica que lo diferencia del Frontend es que no tiene estándares, puesto que tiene varios lenguajes de programación (Node.js, Python, PHP, Ruby, GO, Java, .NET entre otros) con los que debe trabajar. Cada uno de estos lenguajes tiene sus propios frameworks como:

Django (Python)
Lavarel (PHP)
Rails (Ruby)
Express (JavaScript)
Spring (Java)
El Backend también tiene en cuenta la infraestructura donde va a realizarse el deploy de su aplicación (esto también puede ser tarea de un DevOps, un perfil dedicado a la infraestructura), con tecnologías como:

Google Cloud
DigitalOcean
AWS
Heroku, entre otras.
¿Qué es deploy?
Deploy es un término famoso entre los desarrolladores web. Puede significar muchas cosas, dependiendo del ambiente y de la tecnología usada. Sin embargo, los significados que más se refieren a la práctica y pueden resumir su función son: implantar, colocar en posición, habilitar para uso o, simplemente, publicar.

Por último, entramos en bases de datos, que son las encargadas de almacenar toda la información del proyecto. Los principales tipos son:

Bases de datos relacionales (como MySQL)
Bases de datos no relacionales (como mongoDB).
Aporte creado por: Matías Wasiak, Pedro Moreno.

## Páginas Estáticas vs. Dinámicas


Los sitios web se comportan de forma diferente dependiendo de la forma en que fueron diseñados desde su concepción, tomando en cuenta la interacción con el usuario. Aquí veremos las diferencias entre sitios web estáticos y dinámicos:

**Sitos Web Estáticos**
La información que contiene se mantiene constante y estática. No se actualiza con la interacción del usuario. Es conveniente para realizar landing pages (páginas informativas o de aterrizaje) o blogs. Se mostrarán siempre iguales para todos los usuarios.

**Sitios Web Dinámicos**
También conocidos como aplicaciones web, actualizan su información con respecto a la interacción del usuario. Dependen de una base de datos, de donde extrae e ingresa información. Serán diferentes, dependiendo del usuario que la use y la información que se ingrese.

Ejemplo de páginas estáticas:

Menú de un restaurante
Blog de viajes
Página informativa de un negocio
Ejemplo páginas dinámicas:

Sistema de reporte de ventas
Linkedin
Banca en línea

## HTML: anatomía de una página web

HTML (HyperText Markup Language) es un lenguaje de marcado de texto. Se utiliza para darle una estructura al sitio web que estás visitando.

Estructura básica de HTML en una página Web
Container: contenedor principal
Header: cabecera de la página. Aquí usualmente encuentras el logo y el menú de navegación del sitio.
Main content: estructura principal. Por ejemplo, el feed o lista de publicaciones de una red social.
Sidebar: contenido secundario de una página, que usualmente se encuentra a los lados del contenido principal (o main).
Footer: pie de página. Esto se encuentra al fondo del sitio web, salvo en casos de sitios web donde el scroll (o navegación hacia abajo) es infinito, por ende, no tendría sentido ponerlo al fondo.

Las etiquetas en HTML nos ayudan a diferenciar en qué parte del contenido nos encontramos.

La web se conforma de tres conceptos:

URL: Uniform Resource Locator. El identificador único del sitio en el navegador (por ejemplo: https://platzi.com).
HTTP: Protocolo de transferencia de hipertexto. Es el estándar que se utiliza para enviar datos a través de paquetes entre el cliente y el servidor.
HTML: es el código que se emplea para estructurar el contenido de tu web, y darle sentido y propósito.
HTML son siglas que corresponden a Hyper Text Markup Language (Lenguaje de Marcado de Hipertexto).

Hyper Text significa que el texto tiene interactividad, conexión con otros documentos.
Markup significa que le pone etiquetas a los elementos. Por eso también se le conoce como un lenguaje de etiquetas.
HTML es un lenguaje interpretado. Además, HTML es un estándar, así que no importa desde qué navegador o dispositivo se ejecute, el código sigue siendo el mismo en cualquier sitio.
Aporte creado por: Obed Paz, Christian Tambo, Marcelo Chavarría

## Tipos de imagenes

Lossless (sin pérdida):
* Capturan todos los datos del archivo original.
* No se pierde nada del archivo original.
* Puede comprimirse, pero podrá reconstruir su imagen al estado original

Lossy (con pérdida):
* Se aproximan a su imagen original.
* Podría reducir la cantidad de colores en su imagen o analizar la imagen en busca de datos innecesarios.
* Por consiguiente puede reducir su tamaño, lo que mejora el tiempo de carga de la página, pero pierde su calidad.
* Los archivos tipo lossy son mucho más livianos que los archivos tipo lossless, por lo que son ideales para usar en sitios en donde el tamaño del archivo y la velocidad de descarga son importantes.

Algunos repositorios de interes:
Para Iconos: FlatIcon
Para imágenes: Freepik

Imagenes de 3MB en adelante son muy pesadas para renderizar en un sitio web.
Cual es el tamaño optimo?: una imagen debe pesar en promedio 70KB.
Que opciones hay para trabajar con las imagenes?:
* Mejorar el tamaño de la imagen: **Tiny PNG** 
* Retirar los metadatos de las imagenes: **Verexif**

Compañeros les comparto las paginas que yo uso en mis proyectos.
Compressor.io Comprime sin perder calidad (mejor todavia Tinypng)
Picresize Comprime y recorta el tamaño de la imagen
Convertio convierte jpg, png a svg (esta pagina es muy buena puede convertir de todo a otros formatos es gratis). By Davermx


RECOMENDACIÓN PERSONAL
Yo he usado estas páginas y no se logra optimizar a esta capacidad promedio de 70kb, pero usando Photoshop cambiando el ancho de la imagen y guardandolo como una imagen para web, he podido optimizar de 12MB a 92KB, que en mí opinión ha sido mejor que usar algún sitio en internet. By: FinFonFan

## Etiqueta figure

Figure <figure><img /> </figure> es una etiqueta que permite almacenar una imagen en su interior. Es una mejor práctica comparada con usar solamente un contenedor div. Como complemento al contenedor figure, se utiliza la etiqueta figcaption <figcaption></figcaption>, que permite darle una pequeña descripción a la imagen, como el autor, fuente o algo por el estilo, que se mostrará usualmente abajo de la imagen.

Es importante considerar que la etiqueta figure no es únicamente para imágenes:
El elemento HTML <figure> representa contenido independiente, a menudo con un título. Por lo general, se trata de una imagen, una ilustración, un diagrama, un fragmento de código, o un esquema al que se hace referencia en el texto principal, pero que se puede mover a otra página o a un apéndice sin que afecte al flujo principal.

## Videos

https://www.w3schools.com/tags/tag_video.asp

## Formularios

El mejor formulario es cuando no lo hay.

Es importante tener en cuenta que no es una buena practica realizar formularios apartir de puras etiquetas <div></div>, en lugar es preferible utilizar la etiqueta nativa <form></form>

https://www.w3schools.com/html/html_form_input_types.asp

https://medium.com/@juancaferraris/dise%C3%B1ando-formularios-m%C3%A1s-efectivos-estructura-inputs-labels-y-acciones-81ac011ea05f

https://developer.mozilla.org/es/docs/Web/HTML/Elemento/input

https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete

## Select

https://css-tricks.com/dropdown-default-styling/

https://developer.mozilla.org/es/docs/Web/HTML/Element/select#:~:text=El%20elemento%20select%20

# CSS

Opciones para agregar estilos: 

1. Por medio de la etiqueta, ejemplo de agregar estilo a la etiqueta `p`:
```
p {
    color: blue;
    font-size: 30px;
}
```

2. Por medio de clases, ejemplo a la siguiente etiqueta `<p class="parrafo">Soy un texto</p>`:

```
.parrafo {
    color: red;
}
```

2. Por medio de id, ejemplo a la siguiente etiqueta `<p id="texto">Soy un texto</p>`:

```
#texto {
    color: red;
}
```

https://i.emezeta.com/weblog/css3-cheatsheet/css3-cheatsheet-2017-emezeta.pdf

## PseudoClases y PseudoElementos

PseudoClases: Define el estilo de un estado de un elemento HTML.
PSeudoElementos: Definir o cambiar un elemento de HTML.

Lecturas recomendadas

* Pseudo-classes - CSS | MDN: https://developer.mozilla.org/es/docs/Web/CSS/Pseudo-classes


* Pseudoelementos - CSS | MDN: https://developer.mozilla.org/es/docs/Web/CSS/Pseudoelementos


* FAQ / Methodology / BEM: https://en.bem.info/methodology/faq/#why-bem

Cómo nombrar las clases
Metodología **BEM cómo nombrar correctamente las clases**.

Solo usa clases. Las nombra siguiendo el siguiente patrón: BLOQUE__ELEMENTO—MODIFICADOR (son 2 guiones, se usa 1 guión para separar palabras).

Bloque: sección que puede funcionar por sí sola.
Elemento: forma una de las partes del bloque.
Modificador: variaciones de un mismo bloque/elemento.

```
<!-- BLOQUE -->
<main class="Padre">
	<!-- BLOQUE__ELEMENTO --> 
	<section class="Padre__Hijo">
		<!-- BLOQUE__ELEMENTO--MODIFICADOR -->
		<article class="Padre__Hijastro--Mayor"></article>
		<article class="Padre__Hijastro--Menor"></article>
	</section>
 </main>
 ```

 Crear estilos a etiquetas dentro de clases
Si tienes etiquetas dentro de la etiqueta a la que le estás aplicando estilos y le pones una clase, puedes aplicar estilos únicamente a las etiquetas dentro de esa clase de la siguiente manera: .clase etiqueta {}

```
/* Estilos a etiqueta "a" dentro de una clase */
.main-nav__item a {
    color: white;
}
```
Usa background-color para ver las cajas de los elementos.

Pseudo clases
Define el estilo de un estado especial de un elemento.

Agregar al final de la clase :nombreAccion

```
/* Pseudo clase */
.main-nav__item a:hover {
    color: darkblue;
}

.main-nav__item a:active {
    color: darkcyan;
}
```

Pseudo Elementos
Define el estilo de una parte específica de un elemento.

Agregar al final de la clase ::nombreAccion

```
/* Pseudo elemento */
.main-nav__item a::after {
    content: " | "; /* despues del elemento, agrega esto */
}
```

## Modelo de caja

https://www.youtube.com/watch?v=TeQgd0NS_lQ