# Pruebas de Software

### Bárbara Uribe Cataldo - 201673074-5 - barbara.uribe@sansano.usm.cl

## Instalación

Para poder utilizar este programa se debe instalar [Python 3.9.4](https://www.python.org) en su última versión. En el link indicado se puede descargar y seguir los pasos indicados para su instalación.

Además, se debe instalar la libreria boto3, esto se realiza mediante ingresar la siguiente línea de comandos en nuestra terminal:

`
pip install boto3
`

## Ejecución

Para poder ejecutar este programa tenemos varias opciones, pero antes de ver estas debemos asegurarnos de que dentro del directorio donde se encuentra nuestro programa debemos tener una carpeta llamada imgs que contenga las imágenes a ser probadas por nuestro código, estas deben tener extensión ".png" o ".jpg"

### Ejecución mediante IDLE de Python:

Para ello debemos abrir el archivo TareaPdS.py en nuestro IDLE de Python instalado y presionar F5, también podemos ejecutarlo presionando en el menú "Run" en la parte superior del IDLE y presionando a continuación en el menú desplegado "Run Module".

### Ejecución mediante consola o terminal:

Podemos ejecutar el programa directamente en la consola de nuestro computador, o en la terminal de nuestro editor de código favorito.

Para ello, establecemos nuestro directorio en donde se encuentre nuestro archivo TareaPdS.py, luego ejecutamos:

`
python TareaPdS.py
`

## Uso

Este programa se ejecuta sin necesidad de inputs directos del usuario, durante su ejecución genera logs especificando qué archivos se está comparando con cuál, si estos poseen un match de caras o no y si es que ocurrió un error durante la ejecución. 