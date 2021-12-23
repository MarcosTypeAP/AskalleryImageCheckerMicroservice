"""Askallery utilities."""

# Requets
import requests

# BeautifulSoup
from bs4 import BeautifulSoup

# Python
import time


def is_asuka_picture(image_name):
    """Validates that the image is a asuka picture."""

    google_search_url = 'https://www.google.com/searchbyimage'
    extra_query_params = '&encoded_image=&image_content=&filename=&hl=en'
    askallery_media_url = 'https://askallery.herokuapp.com/media/'

    search_by_image_url = '{}?image_url={}{}{}'.format(
        google_search_url, askallery_media_url, image_name, extra_query_params
    )

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
        'Accept': 'text/html',
    }
    print(search_by_image_url)
    for x in range(3):
        response = requests.get(search_by_image_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        target = soup.find('input', {'aria-label': 'Search', 'name': 'q'})
        result = target.get('value').upper()
        if result:
            break
        time.sleep(5)

    print(result)
    WRONG_WORDS = ('WWE', 'LUCHADORA', 'WRESTLER')
    ASUKA = ('ASUKA', 'アスカ')

    check_1 = any([x not in result for x in ASUKA])
    check_2 = any([x in result for x in WRONG_WORDS])

    if check_1 or check_2:
        return False
    return True
