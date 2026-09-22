execution_log = []
recursive_trace = []
recursive_calls = 0


def logger(func):
    def wrapper(*args, **kwargs):
        execution_log.append(f"Executing: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@logger
def detect_abnormal(value):
    if value >= 40:
        return True

    return False


@logger
def recursive_analysis(value):
    global recursive_calls

    recursive_calls += 1
    recursive_trace.append(value)

    if value <= 0:
        return value

    return recursive_analysis(value - 10)


def create_report(processed_results, abnormal_results):
    valid_count = len(processed_results)
    abnormal_count = len(abnormal_results)

    if abnormal_count > 0:
        status = "ABNORMAL"
    else:
        status = "NORMAL"

    return {
        "Processed Readings": valid_count,
        "Detected Abnormal Conditions": abnormal_count,
        "Overall Equipment Status": status
    }