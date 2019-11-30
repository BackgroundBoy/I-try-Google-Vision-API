from google.cloud import vision
import io
from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype("arial.ttf", 14)

def detect_multi_obj(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    
    image  = vision.types.Image(content=content)
    response = client.object_localization(image=image, max_results=100, timeout=10)

    im = Image.open(path)
    w,h = im.size
    draw = ImageDraw.Draw(im)

    #print(response)#

    objs = response.localized_object_annotations

    for obj in objs:
        print('\n{} (confidence: {})'.format(obj.name, obj.score))
        # print('Normalized bounding polygon vertices: ')
        # for vertex in obj.bounding_poly.normalized_vertices:
        #     print(' - ({}, {})'.format(vertex.x,vertex.y))
        box = [(vertex.x*(w-1), vertex.y*(h-1)) \
               for vertex in obj.bounding_poly.normalized_vertices]
        draw.line(box + [box[0]], width=2, fill='#00ff00')
        try:
            draw.text(((obj.bounding_poly.normalized_vertices)[0].x*(w-1),
                    (obj.bounding_poly.normalized_vertices)[0].y*(h-1) -20),
                    obj.name,
                    fill='#FF0000', font=font)
        except:
            print("None English character")
    
    im.show()
    im.save('obj_out.jpg')


def main(path):
    detect_multi_obj(path)

if __name__ == '__main__':
    input_path = input('Image name(.jpg, .png, etc.): ')
    main(input_path) 