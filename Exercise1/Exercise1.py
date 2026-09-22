LAST_NAME = "AYUDTUD"
SEED_NUM = 9
FAVORITE_ARTIST = "IV OF SPADES"


# Generate student-specific equipment readings
def generate_readings():
    readings = [
        SEED_NUM * 2,
        SEED_NUM + len(LAST_NAME),
        len(FAVORITE_ARTIST)
    ]

    return readings


# Validate equipment readings
def validate_reading(value):
    try:
        value = float(value)

        if value < 0:
            return False

        return True

    except ValueError:
        return False


# Record the diagnostic process
execution_log = []


def logger(func):
    def wrapper(*args, **kwargs):
        execution_log.append(f"Executing: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


# Calculate diagnostic result
@logger
def calculate_diagnostic(reading):
    return reading * SEED_NUM


# Classify equipment condition
@logger
def classify_diagnostic(result):
    if result >= 150:
        return "HIGH"
    elif result >= 100:
        return "NORMAL"
    else:
        return "LOW"


# Main diagnostic process
try:
    readings = generate_readings()

    validation_results = []
    diagnostic_results = []
    classification_results = []

    for reading in readings:

        if validate_reading(reading):
            validation_results.append(True)

            diagnostic = calculate_diagnostic(reading)
            diagnostic_results.append(diagnostic)

            condition = classify_diagnostic(diagnostic)
            classification_results.append(condition)

        else:
            validation_results.append(False)

except (ValueError, TypeError) as e:
    print("Diagnostic Error:", e)


# Final Output
print("\n" + "=" * 50)
print("EQUIPMENT DIAGNOSTIC SYSTEM")
print("=" * 50)

print("Student:", LAST_NAME)
print("Seed Number:", SEED_NUM)
print("Favorite Artist:", FAVORITE_ARTIST)

print("\nGenerated Equipment Data:", readings)
print("Validation Results:", validation_results)
print("Diagnostic Results:", diagnostic_results)
print("Execution Log:", execution_log)
print("Final Output:", classification_results)

print("=" * 50)


