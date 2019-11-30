from google.cloud import vision
import io

def detect_label(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    # print(response)#

    print('Labels: ')
    for label in  labels:
        print(label.description , '\t' , label.score )

def main(path):
    detect_label(path)

if __name__ == '__main__':
    input_path = input('Image name(.jpg, .png, etc.): ')
    main(input_path) 