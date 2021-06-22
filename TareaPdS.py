import boto3
import logging
import requests

logger = logging.getLogger("logging_tryout2")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s |:| %(levelname)s |:| %(message)s",
                              "%Y-%m-%d %H:%M:%S")
ch.setFormatter(formatter)
logger.addHandler(ch)
logging.basicConfig(filename='Results.txt')


def compare_faces(sourceFile, targetFile):
    client = boto3.client('rekognition')

    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')

    response = client.compare_faces(SimilarityThreshold=80,
                                    SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})

    for faceMatch in response['FaceMatches']:
        similarity = str(faceMatch['Similarity'])
        logger.info('La cara en la imagen ' + targetFile +
                    ' concuerda con la cara en la imagen base con un ' +
                    similarity + '% de seguridad.')

    imageSource.close()
    imageTarget.close()
    return len(response['FaceMatches'])


"""urls = [
    "https://tareapds.s3.us-east-2.amazonaws.com/imgs/rostro_30_abajo_p.jpg",
    "https://tareapds.s3.us-east-2.amazonaws.com/imgs/rostro_30_abajo.jpg",
    "https://tareapds.s3.us-east-2.amazonaws.com/imgs/rostro_30_arriba.jpg",
    "https://tareapds.s3.us-east-2.amazonaws.com/imgs/rostro_45_arriba_p.jpg",
    "https://tareapds.s3.us-east-2.amazonaws.com/imgs/rostro_adulto.jpg",
    "https://tareapds.s3.us-east-2.amazonaws.com/imgs/rostro_blanco_negro.jpg",
    "https://tareapds.s3.us-east-2.amazonaws.com/imgs/rostro_desenfocado.jpg",
    "https://tareapds.s3.us-east-2.amazonaws.com/imgs/rostro_dibujo.jpg",
    "https://tareapds.s3.us-east-2.amazonaws.com/imgs/rostro_expresion_exagerada.jpg",
    "https://tareapds.s3.us-east-2.amazonaws.com/imgs/rostro_figura_real.jpg",
    "https://tareapds.s3.us-east-2.amazonaws.com/imgs/rostro_muchas_sombras.jpg",
    "https://tareapds.s3.us-east-2.amazonaws.com/imgs/rostro_ojos_cerrados.jpg",
    "https://tareapds.s3.us-east-2.amazonaws.com/imgs/rostro_parecido.jpg",
    "https://tareapds.s3.us-east-2.amazonaws.com/imgs/rostro_perfil.jpg",
    "https://tareapds.s3.us-east-2.amazonaws.com/imgs/rostro_poco_contraste.jpg",
    "https://tareapds.s3.us-east-2.amazonaws.com/imgs/rostro_sin_rostro.jpg"]
"""

urls = ["https://tareapds.s3.us-east-2.amazonaws.com/45arriba.jpg",
        "https://tareapds.s3.us-east-2.amazonaws.com/anakin.jpg",
        "https://tareapds.s3.us-east-2.amazonaws.com/animacion.jpg",
        "https://tareapds.s3.us-east-2.amazonaws.com/base.jpg",
        "https://tareapds.s3.us-east-2.amazonaws.com/caricatura.jpg",
        "https://tareapds.s3.us-east-2.amazonaws.com/expresion.jpg",
        "https://tareapds.s3.us-east-2.amazonaws.com/figuradeaccion.jpg",
        "https://tareapds.s3.us-east-2.amazonaws.com/lego.jpeg",
        "https://tareapds.s3.us-east-2.amazonaws.com/luke+viejo.png",
        "https://tareapds.s3.us-east-2.amazonaws.com/mirandoatras.jpg",
        "https://tareapds.s3.us-east-2.amazonaws.com/muchas+sombras.jpeg",
        "https://tareapds.s3.us-east-2.amazonaws.com/perfil.jpg",
        "https://tareapds.s3.us-east-2.amazonaws.com/sebastianstain.jpg"]


def main():
    source_file = 'Luke_base.jpg'
    c = 1
    for url in urls:
        try:
            img = requests.get(url).content
        except Exception as e:
            print(f"Error, no se pudo descargar la imagen proveniente de {url} - {e}")
        try:
            p = url.split('/')[3]
            path = 'imgs/' + p
            with open(path, 'wb') as f:
                f.write(img)
            logger.info(f"Se está comparando {source_file} con {path}")
            if compare_faces(source_file, path):
                continue
            else:
                logger.info(f"No se encontró coincidencia entre {source_file} e {path}")
        except Exception as er:
            logger.error(f"Ocurrió un error al comparar con la imagen {path} - {er}")
        c += 1


if __name__ == "__main__":
    main()
