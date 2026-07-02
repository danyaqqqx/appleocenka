from pricing import calculate

def get_price(data):
    return calculate(
        data["model"],
        data["screen"],
        data["battery"],
        data["body"],
        data["repair"]
    )