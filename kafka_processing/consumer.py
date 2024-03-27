from kafka import KafkaConsumer

def consume_from_kafka(topic):
    consumer = KafkaConsumer(topic, group_id='mygroup', bootstrap_servers='localhost:9091')

    for message in consumer:
        print(f'Received message: {message.value}')
    print(f"We have Consumed {len(consumer)} items in Kafka topic cao")