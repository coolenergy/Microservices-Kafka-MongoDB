from ORM.create import create_cyberattacks
from transformation.transform import get_transformed_observation1,get_transformed_observation2
from ORM.insert import insert_builk_cyberattacks
from ORM.select import select_all_cyberattacks
from kafka_processing.consumer import consume_from_kafka
from kafka_processing.producer import insert_data_into_kafka

if __name__ == "__main__":
    topic_name = 'cao'
    create_cyberattacks()
    data_1 = get_transformed_observation1()
    data_2 = get_transformed_observation2()
    data = data_1 + data_2
    insert_builk_cyberattacks(data)
    insert_data_into_kafka(data,topic_name)
    consume_from_kafka(topic_name)
    total_rows = select_all_cyberattacks()
    print(f"We have counted {len(total_rows)} items in postgres")