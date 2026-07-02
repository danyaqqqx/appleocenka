BASE = {
    "12": 20000,
    "13": 28000,
    "14": 38000,
    "15": 50000
}

def battery_mult(b):
    if b >= 90: return 1.0
    if b >= 80: return 0.92
    if b >= 70: return 0.85
    if b >= 60: return 0.75
    return 0.6


SCREEN = {
    "screen_perfect": 1.0,
    "screen_scratches": 0.9,
    "screen_cracked": 0.75,
    "screen_broken": 0.55
}

BODY = {
    "body_perfect": 1.0,
    "body_light": 0.95,
    "body_heavy": 0.85
}

REPAIR = {
    "repair_no": 1.0,
    "repair_yes": 0.85,
    "repair_water": 0.7
}

def calculate(model, screen, battery, body, repair):
    price = BASE[model]

    price *= SCREEN[screen]
    price *= battery_mult(battery)
    price *= BODY[body]
    price *= REPAIR[repair]

    return int(price)