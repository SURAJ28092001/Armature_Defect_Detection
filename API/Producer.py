from confluent_kafka import Producer
import os

producer = Producer({'bootstrap.servers': 'localhost:9092'})
from PIL import Image
import json

# Open the JPG image
image = Image.open('input.jpg')

def produce_messages(producer, topic):
    i = 1
    while True:
        message = f"Message {i}"
        producer.produce(topic, key=str(i), value=message)
        producer.flush()
        print(f"Produced message: {message}")
        i += 1
        
# Convert the image to RGB mode (if it's not already)
if image.mode != 'RGB':
    image = image.convert('RGB')
image=image.resize((200,200))

# Get the dimensions of the image
width, height = image.size
# Get the pixel data as a list of RGB tuples
pixel_data = list(image.getdata())

# Create a dictionary to store the pixel data and image dimensions
data = {
    "width": width,
    "height": height,
    "pixels": pixel_data
}

# Convert the dictionary to a JSON string
json_data = json.dumps(data)
producer.produce('image',json_data)
producer.flush()

  #producer.produce('Jaa_na_lavdee', key=str(i),value=str(i))
  #producer.flush()
#image_dir = 'C:/Users/athar/OneDrive/Pictures/Payal/'  # Replace with the path to your image directory
#print("ja na <3day")
#for i in range (10000):
 # 



from PIL import Image
import numpy

# Open an image (provide the full path to an actual image file)
#image = Image.open("C:\Users\athar\OneDrive\Documents\Final year project\Armature_Defect_Detection\API\20230919162116_IMG_9377.JPG")

# Convert the image to a NumPy array
pixel = numpy.array(image)