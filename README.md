# Realtime Vitals Feed v2

This project continuously produces realistic human vitals data to a Kafka topic.

## Usage

1.  Clone the repository:
   ```bash
   git clone https://github.com/Gautam0610/realtime-vitals-feed-v2-data.git
   cd realtime-vitals-feed-v2-data
   ```
2.  Create a `.env` file based on the `.env.template` file and fill in the required configurations.
3.  Build the Docker image:
   ```bash
   docker build -t realtime-vitals-feed .
   ```
4.  Run the Docker container:
   ```bash
   docker run realtime-vitals-feed
   ```

## Configuration

The following configurations are required in the `.env` file:

*   `KAFKA_BROKER`: The address of the Kafka broker.
*   `KAFKA_TOPIC`: The name of the Kafka topic to send data to.

## Vitals Data

The following vitals data is generated:

*   Body Temperature (°C)
*   Heart Rate (bpm)
*   Systolic Blood Pressure (mmHg)
*   Diastolic Blood Pressure (mmHg)
*   Breaths per Minute
*   Oxygen Saturation (%)
*   Blood Glucose (mg/dL)