from logging import exception

import pandas as pd
import os

def capture_additional_signal_data(dataframe, index):
    try:
        timestamp = dataframe['Timestamp'].iloc[index]
        vehicle_velocity = dataframe['vehicle_velocity[Km/h]'].iloc[index]
        rear_turn_assist_criticality = dataframe['rear_turn_assist_criticality'].iloc[index]
        object_class = dataframe['object_class'].iloc[index]
        object_pos_x = dataframe['object_pos_x[m]'].iloc[index]
        object_pos_y = dataframe['object_pos_y[m]'].iloc[index]
        object_velocity = dataframe['object_velocity[Km/h]'].iloc[index]

        logging_dataframe = pd.DataFrame({'Timestamp': timestamp, 'vehicle_velocity': vehicle_velocity,'rear_turn_assist_criticality': rear_turn_assist_criticality, 'object_class': object_class,
                       'object_pos_x':object_pos_x, 'object_pos_y': object_pos_y, 'object_velocity': object_velocity}, index=[0])

        #we need to check if the file exists before writing to it to determine whether to write headers or not
        file_state = os.path.exists('TriggerAdditionalInfos.csv')

        if file_state:
            logging_dataframe.to_csv('TriggerAdditionalInfos.csv', header=False, mode= 'a', index=False)
        else:
            logging_dataframe.to_csv('TriggerAdditionalInfos.csv', index=False)
    except Exception as e:
        print(f"[ERROR] An error in capturing additional signal data function : {e}")

