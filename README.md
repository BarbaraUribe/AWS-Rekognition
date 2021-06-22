# Pruebas de Software

### Bárbara Uribe Cataldo - 201673074-5 - barbara.uribe@sansano.usm.cl

## Instalación

Para poder utilizar este programa se debe instalar [Python 3.9.4](https://www.python.org) en su última versión. En el link indicado se puede descargar y seguir los pasos indicados para su instalación.

Además, se debe instalar la librería boto3 y la librería requests, esto se realiza mediante ingresar las siguientes líneas de comandos en nuestra terminal:

`
pip install boto3
`

`
pip install requests
`

## Ejecución

Para poder ejecutar este programa tenemos varias opciones, pero antes de ver estas debemos asegurarnos de editar la lista de urls dentro de nuestro programa, esta lista contiene las urls de cada imagen almacenada en S3. Estas deben tener extensión ".png" o ".jpg"

### Ejecución mediante IDLE de Python:

Para ello debemos abrir el archivo TareaPdS.py en nuestro IDLE de Python instalado y presionar F5, también podemos ejecutarlo presionando en el menú "Run" en la parte superior del IDLE y presionando a continuación en el menú desplegado "Run Module".

### Ejecución mediante consola o terminal:

Podemos ejecutar el programa directamente en la consola de nuestro computador, o en la terminal de nuestro editor de código favorito.

Para ello, establecemos nuestro directorio en donde se encuentre nuestro archivo TareaPdS.py, luego ejecutamos:

`
python TareaPdS.py
`

## Uso

Este programa se ejecuta sin necesidad de inputs directos del usuario, durante su ejecución genera logs especificando qué archivo se está comparando con cuál, si estos poseen un match de caras o no y si es que ocurrió un error durante la ejecución. 

## Pruebas

Las pruebas realizadas se encuentran [aquí](https://pruebas-de-software.ontestpad.com/script/2/report/HT?auth=1df2ba77c24de1e45b2af3c2f92798c3) y [aquí](https://aws-usm.ontestpad.com/script/2/report/?auth=13f66e08450803bce654d631f3d6abb9). Las pruebas correspondientes a este código son aquellas que aparecen primero en la tabla representada. Las otras pruebas corresponden a las pruebas realizadas al código de mi compañera Valerie.

Finalmente, los criterios de aceptación utilizados para ellas fueron los siguientes:

Para considerar uno de los siguientes casos a probar como fallido o exitoso se deben cumplir lo siguiente:

Si en la imagen aparece la cara del personaje Luke Skywalker el programa debe arrojar que existe una coincidencia y suministrar el porcentaje de seguridad que tiene al hacer esta aseveración.

Por otro lado, si en la imagen no aparece la cara del personaje Luke Skywalker pero si existen caras distintas a la suya, el programa deberá arrojar que no se encontró coincidencia entre las imágenes.

Finalmente, si la imagen ingresada no posee ningún rostro el programa arrojará un error, ya que compareFaces no encontró ninguna cara y no tiene con qué comparar nuestra imagen base.
