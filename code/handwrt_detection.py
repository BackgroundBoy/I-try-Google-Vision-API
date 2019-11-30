from google.cloud import vision
import io
from PIL import Image, ImageDraw

def detect_document(path):
    """Detects document features in an image."""

    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image, **{'image_context':{"language_hints": ["th-handwrit"]}})
    im = Image.open(path)
    draw = ImageDraw.Draw(im)
    # print(response)#
    # print(response.text)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                print('Paragraph confidence: {}'.format(
                    paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))

                    # for symbol in word.symbols:
                    #     print('\tSymbol: {} (confidence: {})'.format(
                    #         symbol.text, symbol.confidence))
                    box = [(vertex.x, vertex.y) \
                            for vertex in word.bounding_box.vertices]
                    draw.line(box + [box[0]], width=5, fill='#00ff00')
    im.show()

def main(path):
    detect_document(path)\

if __name__ == '__main__':
    input_path = input('Image name(.jpg, .png, etc.): ')
    main(input_path)