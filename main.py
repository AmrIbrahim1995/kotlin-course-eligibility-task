from generate_ideal_sensor_data import generate_ideal_sensor_data
from process_sensor_data import process_sensor_data
from write_statistics_overview_to_json import write_statistics_overview_to_json

def main():
    try:
        generate_ideal_sensor_data()
        statistics_overview = process_sensor_data()
        write_statistics_overview_to_json(statistics_overview)

    except Exception as e:
        print(f"[ERROR] Unexpected Error: {e}")

if __name__ == "__main__":
    main()