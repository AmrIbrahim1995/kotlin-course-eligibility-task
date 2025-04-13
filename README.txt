Sensor Data Simulation & Analysis
=================================

Overview:
---------
This project simulates random sensor data, evaluates it, and outputs important statistics about the rear turn assist in
autonomous cars.
It can be useful for testing data pipelines.

Features:
---------
- Generate random sensor data
- Evaluate the data
- Output statistics

Technologies Used:
------------------
- Python 3.x
- NumPy
- Pandas

Installation:
-------------
1. Clone the repository:
   git clone https://github.com/yourusername/sensor-data-sim.git
   cd sensor-data-sim

How to Use:
-----------
Basic usage:

Run everything at once:
   main.py


Output Example:
---------------
Sample statistics output (as JSON):

{
    "Sensor Software Version": "Z76.01.01",
    "Date of Recording": "2025-04-11 14:58:08.111799",
    "Measurement Duration [s]": 4.95,
    "Distance Travelled [m]": 450.0,
    "Number of Occurrences of 1st criticality level": 18,
    "Number of Occurrences of 2nd criticality level": 15,
    "Number of Occurrences of 3rd criticality level": 15,
    "Number of Occurrences of 4th criticality level": 23
}


