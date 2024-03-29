import sys
from importlib import import_module
from utils.utils import get_input
from datetime import datetime


if __name__ == "__main__":
    year = sys.argv[1]
    day = sys.argv[2]
    part = sys.argv[3]
    test = sys.argv[4] if len(sys.argv) > 4 else None
    script = import_module(f"y{year}.{day}.part{part}")
    module = f"y{year}/{day}"
    try:
        keep_whitespace = script.WHITESPACE
    except AttributeError:
        keep_whitespace = False

    # run test
    test_time = None
    if not test or test == "t":
        input_data = get_input(module, prefix="test", keep_whitespace=keep_whitespace)

        start = datetime.now()
        result = script.run(input_data, is_test=True)
        end = datetime.now()
        test_time = end - start
        print(result)

    # run main
    input_time = None
    if not test or test == "m":
        input_data = get_input(module, keep_whitespace=keep_whitespace)
        start = datetime.now()
        result = script.run(input_data, is_test=False)
        end = datetime.now()
        input_time = end - start
        print(result)

    if test_time:
        print(f"Test time: {test_time}")
    if input_time:
        print(f"Full input time: {input_time}")
