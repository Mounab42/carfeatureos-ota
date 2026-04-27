# AEB Basic v1.0 — distance 50m
import json

def activate():
    config = {
        "feature": "AEB",
        "plan": "basic",
        "distance_m": 50,
        "can_id": "0x101",
        "data": [0x01, 0x32, 0x00, 0x00]
    }
    print(f"AEB Basic activé — distance: {config['distance_m']}m")
    return config

if __name__ == "__main__":
    result = activate()
    print(json.dumps(result))
