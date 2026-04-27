# AEB Premium v2.0 — distance 30m + alertes avancées
import json

def activate():
    config = {
        "feature": "AEB",
        "plan": "premium",
        "distance_m": 30,
        "alert": True,
        "can_id": "0x101",
        "data": [0x02, 0x1E, 0x01, 0x00]
    }
    print(f"AEB Premium activé — distance: {config['distance_m']}m avec alertes")
    return config

if __name__ == "__main__":
    result = activate()
    print(json.dumps(result))
