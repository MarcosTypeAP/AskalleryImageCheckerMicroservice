"""Askallery image checker flask microservice."""

# Flask
from flask import Flask, request

# Utils
from utils import is_asuka_image


app = Flask(__name__)


@app.route('/api/checkimage/', methods=['GET'])
def check_image():
    """Verifies that the given image is about `Asuka Langley`."""
    image = request.args.get('image')
    if is_asuka_image(image):
        return {'message': 'Is an Asuka image.', 'bool': 1}
    return {'message': 'Is not an Asuka image.', 'bool': 0}