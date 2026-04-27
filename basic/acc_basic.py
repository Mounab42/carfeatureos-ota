# ACC Basic v1.0 — vitesse max 130km/h
import json

def activate():
    config = {
        "feature": "ACC",
        "plan": "basic",
        "max_speed_kmh": 130,
        "can_id": "0x102",
        "data": [0x01, 0x82, 0x00, 0x00]
    }
    print(f"ACC Basic activé — vitesse max: {config['max_speed_kmh']}km/h")
    return config

if __name__ == "__main__":
    result = activate()
    print(json.dumps(result))
