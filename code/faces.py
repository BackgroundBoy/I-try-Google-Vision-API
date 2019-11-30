# create the service object
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw



# face detection request
def detect_face(face_file, max_result=4):
    client = vision.ImageAnnotatorClient()

    content = face_file.read()
    image = types.Image(content=content)

    return client.face_detection(image=image, max_results=max_result).face_annotations

# Process the response
def highlight_faces(image, faces, output_filename):
    im = Image.open(image)
    draw = ImageDraw.Draw(im)

    for face in faces:
        box = [(vertex.x, vertex.y) \
               for vertex in face.bounding_poly.vertices]
        draw.line(box + [box[0]], width=5, fill='#00ff00')

        draw.text(((face.bounding_poly.vertices)[0].x,
                   (face.bounding_poly.vertices)[0].y-10),
                  str(format(face.detection_confidence, '.3f')) + '%',
                  fill='#FF0000')
        im.save(output_filename)

    im.show()

def main(input_filename, output_filename, max_results):
    with open(input_filename, 'rb') as image:
        faces = detect_face(image, max_results)
        print(faces)##
        print('Found {} face{}'.format(
            len(faces), '' if len(faces) == 1 else 's'))
        print('Writing to file {}'.format(output_filename))
        image.seek(0)
        highlight_faces(image, faces, output_filename)

if __name__ == '__main__':
    file_name = input('Image name(.jpg, .png, etc.): ')
    output_name = input('Output name(.jpg, .png, etc.): ')
    max_results = int(input('Number of max result: '))

    main(file_name, output_name, max_results)
    
    
