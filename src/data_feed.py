import json
import time

def load_mock_data(path='data/mock_live_timing.json'):
    with open(path, 'r') as file:
        return json.load(file)

def simulate_live_feed(data, delay=2):
    """
    Simulates streaming data by yielding one frame at a time
    with a delay in between.
    """
    for frame in data:
        yield frame
        time.sleep(delay)  # simulate real-time delay