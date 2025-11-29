from datetime import datetime

INPUT_FILE = "hblog.txt"
KEY = "TSTFEED0300|7E3E|0400"


def extract_timestamp(line: str) -> datetime:
    pos = line.find("Timestamp ")
    if pos == -1:
        return None
    time_str = line[pos + len("Timestamp "): pos + len("Timestamp ") + 8]
    return datetime.strptime(time_str, "%H:%M:%S")


def filter_lines_by_key(filepath: str, key: str):
    filtered = []
    with open(filepath, "r") as f:
        for line in f:
            if key in line:
                filtered.append(line.strip())
    return filtered


def analyze_heartbeats(lines):
    results = []
    timestamps = [extract_timestamp(line) for line in lines]
    timestamps = [t for t in timestamps if t is not None]

    for i in range(len(timestamps) - 1):
        current_ts = timestamps[i]
        next_ts = timestamps[i + 1]

        diff = abs((current_ts - next_ts).total_seconds())

        if 31 < diff < 33:
            results.append(f"WARNING: heartbeat = {diff} sec at {current_ts.time()}")
        elif diff >= 33:
            results.append(f"ERROR: heartbeat = {diff} sec at {current_ts.time()}")

    return results

filtered = filter_lines_by_key(INPUT_FILE, KEY)
analysis_results = analyze_heartbeats(filtered)

for line in analysis_results:
    print(line)