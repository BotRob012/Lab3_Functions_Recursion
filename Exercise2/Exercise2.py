LAST_NAME = "AYUDTUD"
SEED_NUM = 9
FAVORITE_ARTIST = "IV OF SPADES"


def generate_fault_code():
    fault_code = SEED_NUM * len(LAST_NAME) + len(FAVORITE_ARTIST)
    return fault_code

recursive_trace = []

recursive_calls = 0

execution_log = []


def logger(func):
    def wrapper(*args, **kwargs):
        execution_log.append(f"Executing: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@logger
def trace_fault(code):
    global recursive_calls

    recursive_calls += 1
    recursive_trace.append(code)

    # Base condition
    if code <= SEED_NUM:
        return code

    return trace_fault(code - SEED_NUM)


fault_code = generate_fault_code()

final_result = trace_fault(fault_code)


print("\n" + "=" * 50)
print("RECURSIVE FAULT TRACE")
print("=" * 50)

print("Student:", LAST_NAME)
print("Seed Number:", SEED_NUM)
print("Favorite Artist:", FAVORITE_ARTIST)

print("\nGenerated Fault Data:", fault_code)
print("Recursive Trace:", recursive_trace)
print("Number of Recursive Calls:", recursive_calls)
print("Execution Log:", execution_log)
print("Final Output:", final_result)

print("=" * 50)