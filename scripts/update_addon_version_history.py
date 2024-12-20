import json
import os
import sys
from datetime import datetime, timedelta

def load_json(file_path):
    """Loads JSON data from a file."""
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return {}

def save_json(data, file_path):
    """Saves JSON data to a file."""
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def update_version_history(input_json, output_file):
    """Updates the version history with the input JSON."""
    # Current date
    current_date = datetime.now().date().isoformat()
    cutoff_date = (datetime.now() - timedelta(days=60)).date().isoformat()

    # Load existing history
    history = load_json(output_file)

    for component, details in input_json.items():
        if component not in history:
            history[component] = {}

        for version, count in details.get("versions", {}).items():
            if version not in history[component]:
                history[component][version] = {}

            # Add or update the entry for the current date
            history[component][version][current_date] = count

            # Remove entries older than the cutoff date
            history[component][version] = {
                date: value
                for date, value in history[component][version].items()
                if date >= cutoff_date
            }

    # Save the updated history
    save_json(history, output_file)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <input_json_file> <output_json_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        sys.exit(1)

    with open(input_file, "r") as f:
        input_data = json.load(f)

    update_version_history(input_data, output_file)
    print(f"Updated version history saved to {output_file}")
