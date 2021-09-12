from collections import ChainMap


def normalize_json(list_of_json: list) -> dict:

    return dict(
        ChainMap(
            *[{json.get("name"): json.get(key) for key in json.keys() if "Val" in key} for json in list_of_json]
        )
    )