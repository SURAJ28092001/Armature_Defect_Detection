from confluent_kafka import Producer
import os

producer = Producer({'bootstrap.servers': 'localhost:9092'})


image_dir = 'C:/Users/athar/OneDrive/Pictures/Payal/'  # Replace with the path to your image directory
print("ja na <3day")
for i in range (10000):
    producer.produce('Jaa_na_lavdee', key=str(i),value=str(i))
    producer.flush()



