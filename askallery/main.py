"""Askallery image checker flask microservice."""

# Flask
from flask import Flask, request

# Utils
from askallery.utils import is_asuka_picture


app = Flask(__name__)


@app.route('/api/checkimage/', methods=['GET'])
def check_image():
    """Verifies that the given image is about `Asuka Langley`."""
    image_name = request.args.get('image_name')
    if is_asuka_picture(image_name):
        return {'message': 'Is an Asuka image.', 'bool': 1}
    return {'message': 'Is not an Asuka image.', 'bool': 0}
