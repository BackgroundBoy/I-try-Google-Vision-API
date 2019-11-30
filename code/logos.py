from google.cloud import vision
import io
from PIL import Image, ImageDraw

def detect_logos(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path,'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    
    response = client.logo_detection(image=image)  
    im = Image.open(path)
    draw = ImageDraw.Draw(im)
    logos = response.logo_annotations
    
    #print(response)#

    print('Logos: ')

    for logo in logos:
        print(logo.description)
        box = [(vertex.x, vertex.y) \
               for vertex in logo.bounding_poly.vertices]
        draw.line(box + [box[0]], width=5, fill='#00ff00')
        draw.text(((logo.bounding_poly.vertices)[0].x,
                   (logo.bounding_poly.vertices)[0].y-20),
                  logo.description,
                  fill='#FF0000')
    im.show()


def main(path):
    detect_logos(path)

if __name__ == '__main__':
    input_path = input('Image name(.jpg, .png, etc.): ')
    main(input_path) 

    