import boto3
import os
import logging

logger = logging.getLogger("logging_tryout2")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s |:| %(levelname)s |:| %(message)s",
                              "%Y-%m-%d %H:%M:%S")
ch.setFormatter(formatter)
logger.addHandler(ch)


"""
import requests
from selenium import webdriver
n = int(input("Ingrese cantidad de imágenes que quiere descargar: "))

def fetch_image_urls(query, max_links_to_fetch, wd):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # build the google query

    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    # load the page
    wd.get(search_url.format(q=query))

    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        scroll_to_end(wd)

        # get all image thumbnail results
        thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results)

        for img in thumbnail_results[results_start:number_results]:
            # try to click every thumbnail such that we can get the real image behind it
            try:
                img.click()
            except Exception:
                continue

            # extract image urls
            actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))

            image_count = len(image_urls)

            if len(image_urls) >= max_links_to_fetch:
                break
        else:
            load_more_button = wd.find_element_by_css_selector(".mye4qd")
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")

        # move the result startpoint further down
        results_start = len(thumbnail_results)

    return image_urls


urls = fetch_image_urls("luke skywalker", n, webdriver.Chrome())
"""


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


def main():
    source_file = 'Luke_base.jpg'
    """
    c = 1
    for url in urls:
        try:
            img = requests.get(url).content
        except Exception as e:
            print(f"Error, no se pudo descargar la imagen proveniente de {url} - {e}")

        try:
            path = 'imgs/' + str(c) + '.jpg'
            with open(path, 'wb') as f:
                f.write(img)
            try:
                compare_faces(source_file, path)
            except Exception as er:
                print(f"Ocurrió un error al comparar con la imagen {path} - {er}")
        except Exception as e:
            print(f"Error, no se pudo guardar la imagen proveniente de {url} - {e}")
        c += 1
    """
    cont = os.listdir('imgs')
    for path in cont:
        try:
            logger.info(f"Se está comparando {source_file} con {path}")
            if compare_faces(source_file, 'imgs/' + path):
                continue
            else:
                logger.info(f"No se encontró coincidencia entre {source_file} y {path}")
        except Exception as er:
            logger.error(f"Ocurrió un error al comparar con la imagen {path} - {er}")


if __name__ == "__main__":
    main()
