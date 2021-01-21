from typing import List


def get_known_list_from_str(string: str, known_list: List[str]):
    string_list = string.split()
    if not all(item in known_list for item in string_list):
        print("One of the words entered was misspelled or is not a known word")
        return None
    elif len(string_list) == 0:
        print("No words were entered")
        return None
    else:
        return string_list
