def generate_telemetry(last_name, seed_num, favorite_artist):
    base = seed_num + len(last_name)

    values = [
        base,
        seed_num * 2,
        len(favorite_artist),
        base + seed_num,
        "INVALID",
        base + seed_num * 2
    ]

    for value in values:
        yield value


def validate_reading(value):
    try:
        value = float(value)

        if value < 0:
            return False

        return True

    except (ValueError, TypeError):
        return False


def process_reading(value):
    return float(value) * 2