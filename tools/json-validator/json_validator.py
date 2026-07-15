import json
import sys


def validate_json(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            json.load(file)

        print("✅ JSON validation successful")
        print("Payload structure is valid")

    except json.JSONDecodeError as error:

        print("❌ JSON validation failed")
        print()
        print(f"Error: {error.msg}")
        print(f"Line: {error.lineno}")
        print(f"Column: {error.colno}")

    except FileNotFoundError:

        print("❌ File not found")
        print(f"Path: {file_path}")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(
            "Usage: python json_validator.py <json_file>"
        )
        sys.exit(1)

    validate_json(sys.argv[1])