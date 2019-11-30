from google.cloud import vision
import io

def safe_search(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path,'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.safe_search_detection(image=image)
    
    ##print(response)#

    safe = response.safe_search_annotation
    likelihood_name = ('UNKNOW', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY')
    print('Safe Search: ')

    print('adult: {}'.format(likelihood_name[safe.adult]))
    print('medical: {}'.format(likelihood_name[safe.medical]))
    print('spoofed: {}'.format(likelihood_name[safe.spoof]))
    print('violence: {}'.format(likelihood_name[safe.violence]))
    print('racy: {}'.format(likelihood_name[safe.racy]))


def main(path):
    safe_search(path)

if __name__ == '__main__':
    input_path = input('Image name(.jpg, .png, etc.): ')
    main(input_path) 