import io
import os
import glob

# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client
vision_client = vision.Client()


# Test Photo Input


CONFIGS = "/Users/chrisherndon/OneDrive - Seattle University/Photos"
allConfigs = sorted(os.listdir(CONFIGS),
    key=lambda p: os.path.getctime(os.path.join(CONFIGS, p)))
t1 = "%s/%s" % (CONFIGS, allConfigs[-1])
t2 = "%s/%s" % (CONFIGS, allConfigs[-2])
print t1,t2

    
# Asks user for photo to input

# filename = raw_input('Enter a filename: ')

file_name = os.path.join(
                         os.path.dirname(__file__),
                         t1)
                        


# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
    image = vision_client.image(
                                content=content)

# Performs label detection on the image file
labels = image.detect_labels()

print('Labels:')
for label in labels:
    print(label.description)

#Print Space

print('_______')

print('')

'''
# Face Detection

def detect_faces(path):
    vision_client = vision.Client()
    
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    
    image = vision_client.image(content=content)

faces = image.detect_faces()
print('Faces:')
    
for face in faces:
    ('anger: {}'.format(face.emotions.anger))
    ('joy: {}'.format(face.emotions.joy))
    ('surprise: {}'.format(face.emotions.surprise))
        
    vertices = (['({},{})'.format(bound.x_coordinate, bound.y_coordinate)
                    for bound in face.bounds.vertices])
                     
    print('face bounds: {}'.format(','.join(vertices)))
    
    

# Output Statement for the User

    if format(face.emotions.joy) == 'Likelihood.VERY_LIKELY':
            print('This person is happy!')
            
    if format(face.emotions.anger) == 'Likelihood.VERY_LIKELY':
            print('This person is angry!')
    
    if format(face.emotions.surprise) == 'Likelihood.VERY_LIKELY':
            print('This person is suprised!')
            
    if format(face.emotions.joy) == 'Likelihood.VERY_UNLIKELY':
            print('This person is not happy.')
                    
    if format(face.emotions.anger) == 'Likelihood.VERY_UNLIKELY':
            print('This person is not angry.')
                
    if format(face.emotions.surprise) == 'Likelihood.VERY_UNLIKELY':
            print('This person is not suprised.')
            
  '''      

#Standard Face Detection


#Print Space

print('_______')
print('')


#Detecting Logos

def detect_logos(path):
    vision_client = vision.Client()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_client.image(content=content)

logos = image.detect_logos()
print('Logos:')
    
for logo in logos:
    print(logo.description)
    

    if logo.description == 'Amazon' or 'Amazon Music' or 'Amazon Kindle':
        import webbrowser

        webbrowser.open('http://Amazon.com')  # Goes to Amazon
        
    elif logo.description == 'Apple':
        import webbrowser

        webbrowser.open('http://Apple.com')  # Goes to Apple
        
        
    elif logo.description == 'Starbucks':
        import webbrowser

        webbrowser.open('http://Starbucks.com')  # Goes to Starbucks
        
    elif logo.description == 'Brita GmbH' or 'Brita':
        import webbrowser

        webbrowser.open('http://Brita.com')  # Goes to Brita
        

