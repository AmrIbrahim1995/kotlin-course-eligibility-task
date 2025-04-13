import random

import numpy as np
import pandas as pd

def generate_ideal_sensor_data():
    try:
        #Generate samples
        def generate_random_samples(number_of_samples, lowest_value, highest_value):
            random_samples = []
            try:
                for i in range(number_of_samples):
                    sample = random.randint(lowest_value, highest_value)
                    random_samples.append(sample)

                return random_samples
            except Exception as e:
                print(f"[ERROR] Failed to generate random samples: {e}")
                return f"[ERROR] Failed to generate random samples: {e}"

        def generate_position_samples(start_pos, end_pos, step):
            position_samples =[]
            try:
                for i in range(start_pos, end_pos, step):
                    position_samples.append(i)

                return position_samples
            except Exception as e:
                print(f"[ERROR] Failed to generate position samples: {e}")
                return f"[ERROR] Failed to generate position samples: {e}"

        def generate_custom_samples(start, end, number_of_samples):
            try:
                samples =np.linspace(start, end, number_of_samples)

                return samples
            except Exception as e:
                print(f"[ERROR] Failed to generate position samples: {e}")
                return f"[ERROR] Failed to generate position samples: {e}"


        #Generate vehicle velocity data in [Km/h]
        vehicle_velocity = generate_custom_samples(0,120, 100)

        #Generate distance travelled data [m]
        distance_travelled = generate_custom_samples(0,450, 100)

        #Generate timestamp data with 50ms frequency and define the start timestamp
        start_time = pd.Timestamp.now() #datetime format
        timestamps = pd.date_range(start=start_time, periods = 100, freq= '50ms')

        #Generate the criticality level values
        rear_turn_assist_criticality = generate_random_samples(number_of_samples= 100, lowest_value= 1, highest_value= 4)

        #Generate object class
        object_class = generate_random_samples(number_of_samples= 100, lowest_value= 1, highest_value= 2)

        #generate object position x in [m]
        object_pos_x = generate_position_samples(start_pos=401, end_pos=4,step=-4)

        #generate object position y [m]
        object_pos_y = generate_random_samples(number_of_samples= 100, lowest_value= 1, highest_value= 2)

        #generate object velocity in [Km/h]
        object_velocity = generate_custom_samples(0,70, 100)

        #Create a data rame with the generated sensor data
        try:
            df = pd.DataFrame({'Timestamp': timestamps, 'vehicle_velocity[Km/h]': vehicle_velocity, 'distance_travelled[m]': distance_travelled, 'rear_turn_assist_criticality': rear_turn_assist_criticality, 'object_class': object_class,
                           'object_pos_x[m]':object_pos_x, 'object_pos_y[m]': object_pos_y, 'object_velocity[Km/h]': object_velocity  })
        except Exception as e:
            print(f"[ERROR] Failed to create sensor data DataFrame: {e}")

        #write dataframe to csv
        try:
            df.to_csv('SensorData.csv', index = False)
        except Exception as e:
            print(f"[ERROR] Failed to write sensor data to csv: {e}")
    except Exception as e:
        print(f"[ERROR] An Error occured in generate_ideal_sensor_data script: {e}")