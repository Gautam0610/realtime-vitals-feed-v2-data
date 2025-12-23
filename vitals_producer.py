import os
import time
import random
from faker import Faker
from kafka import KafkaProducer

# Configuration from environment variables
KAFKA_BROKER = os.environ.get('KAFKA_BROKER')
KAFKA_TOPIC = os.environ.get('KAFKA_TOPIC')

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)

# Initialize Faker for realistic data generation
fake = Faker()

def generate_vitals():
    body_temperature = round(random.uniform(36.5, 37.5), 1)
    heart_rate = int(random.uniform(60, 100))
    systolic_blood_pressure = int(random.uniform(110, 140))
    diastolic_blood_pressure = int(random.uniform(70, 90))
    breaths_per_minute = int(random.uniform(12, 20))
    oxygen_saturation = int(random.uniform(95, 100))
    blood_glucose = int(random.uniform(70, 140))

    # Occasionally generate extreme values
    if random.random() < 0.01:  # 1% chance
        heart_rate = int(random.uniform(150, 220))  # Extremely high heart rate
        breaths_per_minute = int(random.uniform(30, 50))  # Extremely high breaths per minute

    vitals = {
        'body_temperature': body_temperature,
        'heart_rate': heart_rate,
        'systolic_blood_pressure': systolic_blood_pressure,
        'diastolic_blood_pressure': diastolic_blood_pressure,
        'breaths_per_minute': breaths_per_minute,
        'oxygen_saturation': oxygen_saturation,
        'blood_glucose': blood_glucose
    }
    return vitals


if __name__ == '__main__':
    while True:
        vitals_data = generate_vitals()
        # Serialize vitals data to JSON (or string)
        message = str(vitals_data).encode('utf-8')
        # Send message to Kafka topic
        producer.send(KAFKA_TOPIC, message)
        print(f"Sent: {vitals_data}")
        time.sleep(1)  # Send data every 1 second