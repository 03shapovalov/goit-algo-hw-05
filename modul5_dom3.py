import sys
import re
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    pattern = r'(?P<date>\d{4}-\d{2}-\d{2})\s(?P<time>\d{2}:\d{2}:\d{2})\s(?P<level>\w+)\s(?P<message>.+)'
    match = re.match(pattern, line)
    if match:
        return match.groupdict()
    else:
        return {}

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log = parse_log_line(line.strip())
                if log:
                    logs.append(log)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level.upper():<17} | {count:>8}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <logfile> [level]")
        print("<logfile>: Path to the log file")
        print("[level]: Optional log level to filter logs (INFO, DEBUG, ERROR, WARNING)")
        return

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    if not logs:
        return

    if len(sys.argv) > 2:
        level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level)
        counts = count_logs_by_level(filtered_logs)
        print(f"Деталі логів для рівня '{level}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
        print()
    else:
        counts = count_logs_by_level(logs)

    display_log_counts(counts)

if __name__ == "__main__":
    main()
