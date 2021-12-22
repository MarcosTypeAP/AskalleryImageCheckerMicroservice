"""Askallery utilities."""

# Requets
import requests

# BeautifulSoup
from bs4 import BeautifulSoup


def is_asuka_picture(image_url):
    """Validates that the image is a asuka picture."""

    google_search_url = 'https://www.google.com/searchbyimage'
    extra_query_params = '&encoded_image=&image_content=&filename=&hl=en-AR'

    search_by_image_url = '{}?image_url={}{}'.format(
        google_search_url, image_url, extra_query_params
    )

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
        'Accept': 'text/html',
    }
    response = requests.get(search_by_image_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    target = soup.find('input', {'aria-label': 'Search', 'name': 'q'})
    print(str(target))
    print(type(target))

    if target is None:
        return False
    result = target.get('value').upper()
    print(result)
    wrong_words = ('WWE', 'LUCHADORA', 'WRESTLER')
    if 'ASUKA' not in result or any([x in result for x in wrong_words]):
        return False
    return True