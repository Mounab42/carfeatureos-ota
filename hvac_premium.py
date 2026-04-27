# HVAC Premium v2.0 — mode automatique intelligent
import json

def activate():
    config = {
        "feature": "HVAC",
        "plan": "premium",
        "temp_c": 22,
        "mode": "auto",
        "can_id": "0x103",
        "data": [0x02, 0x16, 0x01, 0x01]
    }
    print(f"HVAC Premium activé — temp: {config['temp_c']}°C mode: {config['mode']}")
    return config

if __name__ == "__main__":
    result = activate()
    print(json.dumps(result))
