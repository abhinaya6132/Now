import json

def save_candidate_info(data, filename='data/candidates.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_candidate_info(filename='data/candidates.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

