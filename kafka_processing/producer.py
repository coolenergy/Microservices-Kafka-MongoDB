import json
from kafka import KafkaProducer


def insert_data_into_kafka(data,topic):
    producer = KafkaProducer(bootstrap_servers='localhost:9091')

    for item in data:
        producer.send(topic, value=json.dumps(item).encode('utf-8'))
    print(f"We have Published {len(data)} items in Kafka topic cao")
    producer.flush()