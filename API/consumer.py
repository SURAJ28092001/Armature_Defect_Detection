from confluent_kafka import Consumer, KafkaError

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'image-consumer-group',
    'auto.offset.reset': 'earliest'
})
consumer.subscribe(['Jaa_na_lavdee'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(f"Error: {msg.error()}")
            break

    data = msg.value()
    print(data)
    # Process image_data (e.g., save to disk, analyze, etc.)

consumer.close()
