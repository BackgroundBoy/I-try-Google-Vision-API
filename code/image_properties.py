from google.cloud import vision
import io

def image_properties(path):
    client = vision.ImageAnnotatorClient()
    
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.types.Image(content=content)
    response = client.image_properties(image=image)
    #print(response)#

    props = response.image_properties_annotation
    print('Properties:')

    for color in props.dominant_colors.colors:
        print('fraction: {}'.format(color.pixel_fraction))
        print('\tred: {}'.format(color.color.red))
        print('\tgreen: {}'.format(color.color.green))
        print('\tblue: {}'.format(color.color.blue))
        print('\talpha: {}'.format(color.color.alpha))


def main(path):
    image_properties(path)

if __name__ == '__main__':
    input_path = input('Image name(.jpg, .png, etc.): ')
    main(input_path) 
    