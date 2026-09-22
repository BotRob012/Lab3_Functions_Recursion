import telemetry
import diagnostics


LAST_NAME = "AYUDTUD"
SEED_NUM = 9
FAVORITE_ARTIST = "IV OF SPADES"


telemetry_data = telemetry.generate_telemetry(
    LAST_NAME,
    SEED_NUM,
    FAVORITE_ARTIST
)


processed_results = []
valid_results = []
invalid_results = []
abnormal_results = []


# Lambda function for transforming the data
transform = lambda value: value * 2


try:

    for reading in telemetry_data:

        if telemetry.validate_reading(reading):

            valid_results.append(reading)

            processed_value = telemetry.process_reading(reading)

            # Lambda transformation
            processed_value = transform(processed_value)

            processed_results.append(processed_value)

            if diagnostics.detect_abnormal(processed_value):
                abnormal_results.append(processed_value)

        else:

            invalid_results.append(reading)

except (ValueError, TypeError) as e:

    print("Telemetry Error:", e)


# Recursive analysis of the first abnormal condition
recursive_result = None

if len(abnormal_results) > 0:

    recursive_result = diagnostics.recursive_analysis(
        abnormal_results[0]
    )


# Generate final diagnostic report
final_report = diagnostics.create_report(
    processed_results,
    abnormal_results
)


# Final Output
print("\n" + "=" * 55)
print("INTELLIGENT EQUIPMENT MONITORING PIPELINE")
print("=" * 55)

print("\nStudent-Specific Inputs:")
print("LAST_NAME:", LAST_NAME)
print("SEED_NUM:", SEED_NUM)
print("FAVORITE_ARTIST:", FAVORITE_ARTIST)

print("\nGenerated Telemetry Data:")
print(valid_results + invalid_results)

print("\nValid/Invalid Results:")
print("Valid:", valid_results)
print("Invalid:", invalid_results)

print("\nProcessed Results:")
print(processed_results)

print("\nRecursive Analysis:")
print("Trace:", diagnostics.recursive_trace)
print("Recursive Calls:", diagnostics.recursive_calls)
print("Recursive Result:", recursive_result)

print("\nFinal Diagnostic Summary:")
print(final_report)

print("\nExecution Log:")
print(diagnostics.execution_log)

print("\nFinal Output:")
print("Overall Equipment Status:", final_report["Overall Equipment Status"])

print("=" * 55)