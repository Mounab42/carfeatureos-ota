# ACC Premium v2.0 — vitesse max 200km/h
import json

def activate():
    config = {
        "feature": "ACC",
        "plan": "premium",
        "max_speed_kmh": 200,
        "can_id": "0x102",
        "data": [0x02, 0xC8, 0x01, 0x00]
    }
    print(f"ACC Premium activé — vitesse max: {config['max_speed_kmh']}km/h")
    return config

if __name__ == "__main__":
    result = activate()
    print(json.dumps(result))
