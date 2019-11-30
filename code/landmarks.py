from google.cloud import vision
import io

def detect_landmarks(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.types.Image(content=content)
    response = client.landmark_detection(image=image)
    landmarks = response.landmark_annotations

    #print(response)#

    for landmark in landmarks:
        print(landmark.description)
        for location in landmark.locations:
            lat_lng = location.lat_lng
            print('Latitude {}'.format(lat_lng.latitude))
            print('Longitude {}'.format(lat_lng.longitude))
    
def main(path):
    detect_landmarks(path)

if __name__ == '__main__':
    input_path = input('Image name(.jpg, .png, etc.): ')
    main(input_path) 