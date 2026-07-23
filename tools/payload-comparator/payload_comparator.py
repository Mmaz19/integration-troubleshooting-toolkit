import json
import sys


def load_json(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def compare_json(old, new, path=""):

    differences = []

    old_keys = set(old.keys())
    new_keys = set(new.keys())

    for key in old_keys - new_keys:
        differences.append(
            f"REMOVED: {path}{key}"
        )

    for key in new_keys - old_keys:
        differences.append(
            f"ADDED: {path}{key}"
        )

    for key in old_keys & new_keys:

        current_path = f"{path}{key}"

        if isinstance(old[key], dict) and isinstance(new[key], dict):

            differences.extend(
                compare_json(
                    old[key],
                    new[key],
                    current_path + "."
                )
            )

        elif old[key] != new[key]:

            differences.append(
                f"MODIFIED: {current_path} "
                f"{old[key]} -> {new[key]}"
            )

    return differences


def main():

    if len(sys.argv) != 3:
        print(
            "Usage: python payload_comparator.py "
            "<old.json> <new.json>"
        )
        return

    old_payload = load_json(sys.argv[1])
    new_payload = load_json(sys.argv[2])

    print("\nPAYLOAD COMPARISON REPORT\n")

    results = compare_json(
        old_payload,
        new_payload
    )

    if results:
        for item in results:
            print("-", item)
    else:
        print("No differences found")


if __name__ == "__main__":
    main()