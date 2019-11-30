from google.cloud import vision
import io
from PIL import Image, ImageDraw
def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    im = Image.open(path)
    draw = ImageDraw.Draw(im)

    response = client.text_detection(image=image,**{'image_context':{"language_hints": ["th"]}})
    texts = response.text_annotations
    # print(response)#
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])
        box = [(vertex.x, vertex.y) \
               for vertex in text.bounding_poly.vertices]
        draw.line(box + [box[0]], width=5, fill='#00ff00')
    im.show()
    # im.save('out.jpg')

    print('bounds: {}'.format(','.join(vertices)))


def main(path):
    detect_text(path)


if __name__ == '__main__':
    file_name = input('Image name(.jpg, .png, etc.): ')
    main(file_name)