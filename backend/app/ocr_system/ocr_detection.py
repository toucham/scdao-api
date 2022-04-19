import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="se-courtinfo-882e71c1b80a.json"
def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()
    
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    output_arr = []
    print('Texts:')

    for text in texts:
        #print("{}".format(text.description))
        output_arr.append(text.description)
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        #print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return output_arr
def main():        
    texts = detect_text('test_image.png')
    print(texts[0])
    return 0

if __name__ == '__main__':
    main()