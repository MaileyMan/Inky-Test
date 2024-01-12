from flask import Flask
from inky.auto import auto
from PIL import Image

app = Flask(__name__)

@app.route("/")
def hello_world():
    display = auto()
    image = Image.new("RGB", display.resolution, (255, 0, 0))
    display.set_image(image)
    display.show()
    return "<p>Hello, World!</p>"