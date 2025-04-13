import pandas as pd
import json
import matplotlib.pyplot as pyplt
from capture_additional_signal_data  import capture_additional_signal_data

def process_sensor_data():
    try:
        try:
            df = pd.read_csv('SensorData.csv')
        except FileNotFoundError:
            print(f"[Error] Couldn't find the sensor data csv file")
        except Exception as e:
            print(f"[Error] An error happened while trying to read the sensor data")

        #Calculate measurement duration
        timestamp = df['Timestamp']

        #Duration = (number of samples - 1) * Frequency
        #first we get the number of samples
        number_of_samples = len(timestamp)
        #Then we apply the equation knowing that the frequency is 50ms
        measurement_duration_in_milliseconds = (number_of_samples - 1) * 50
        measurement_duration_in_seconds = measurement_duration_in_milliseconds/1000

        #Get recording start time
        start_timestamp = df['Timestamp'].iloc[0]

        #Calculate the number of occurrences for each criticality level
        #for example a sequence 0f [1,1,1] counts as 1 occurrence of criticality level 1
        # meanwhile a sequence of [1,2,1] counts as 2 occurrences of criticality level 1 and 1 occurrence of criticality level 2
        Criticality_level = df['rear_turn_assist_criticality']
        #we need to get the difference between successive elements and ignore indices where the difference is equal to zero
        diff = Criticality_level.diff()
        indices_not_zero = df[diff.ne(0)].index.tolist()

        criticality_level_1 = 0
        criticality_level_2 = 0
        criticality_level_3 = 0
        criticality_level_4 = 0

        for i in indices_not_zero:
            criticality_level_value = df['rear_turn_assist_criticality'].iloc[i]
            if criticality_level_value == 1:
                criticality_level_1 = criticality_level_1 + 1
                capture_additional_signal_data(df, i)
            if criticality_level_value == 2:
                criticality_level_2 = criticality_level_2 + 1
                capture_additional_signal_data(df, i)
            if criticality_level_value == 3:
                criticality_level_3 = criticality_level_3 + 1
                capture_additional_signal_data(df, i)
            if criticality_level_value == 4:
                criticality_level_4 = criticality_level_4 + 1
                capture_additional_signal_data(df, i)

        #Generate an overview of the most important statistics
        statistics_overview =    {
            "Sensor Software Version": "Z76.01.01",
                   "Date of Recording": start_timestamp,
                   "Measurement Duration [s]": measurement_duration_in_seconds,
                   "Distance Travelled [m]": df['distance_travelled[m]'].iloc[-1],
                   "Number of Occurrences of 1st criticality level": criticality_level_1,
                   "Number of Occurrences of 2nd criticality level": criticality_level_2,
                   "Number of Occurrences of 3rd criticality level": criticality_level_3,
                   "Number of Occurrences of 4th criticality level": criticality_level_4,
        }
        return statistics_overview
    except Exception as e:
        print(f"[ERROR] An Error occured in proccess_sensor_data script: {e}")






