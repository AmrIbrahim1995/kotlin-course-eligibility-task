import json

def write_statistics_overview_to_json(statistics_overview):
    try:
        with open("StatisticsOverview.json", "w") as f:
            json.dump(statistics_overview, f, indent= 4)
    except Exception as e:
        print(f"[Error] An error happened while trying to write the statistics overview to json : {e}")
