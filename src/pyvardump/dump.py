"""
This is the main code
"""
import json
import sys
from pprint import pprint


def dump_print(obj: object) -> None:
    print(obj)


def dump_pprint(obj: object) -> None:
    pprint(obj)


def dump_obj(obj: object, level: int = 0) -> None:
    try:
        for a in dir(obj):
            if a.startswith("_"):
                continue
            if a in {"adjustments", "auto_shape_type"}:
                continue
            val = getattr(obj, a)
            if type(val) in {int, float, str, list, dict, set}:
                print(level * " ", val)
            else:
                dump_obj(val, level=level + 1)
    except TypeError:
        print(str(type(obj)))
    except AttributeError:
        print(str(type(obj)))


def dump_obj_2(obj: object, level: int = 0) -> None:
    if hasattr(obj, "__dict__"):
        for key, value in obj.__dict__.items():
            if isinstance(value, (int, float, str, list, dict, set)):
                print(" " * level + f"{key} -> {value}")
            else:
                dump_obj_2(value, level + 2)


def default_func(obj: object) -> list[str] | str:
    try:
        return dir(obj)
    except TypeError:
        return str(type(obj))
    except AttributeError:
        return str(type(obj))


def dump_json(obj: object) -> None:
    json.dump(obj, fp=sys.stdout, indent=2)


def object_to_members_or_string(obj: object):
    try:
        if hasattr(obj, "__dict__"):
            return vars(obj)
        return str(obj)
    except TypeError:
        return str(obj)


def flat_dump(obj: object) -> None:
    """
    Dump object to stdout. Only dumps the immediate members of the object
    :param obj:
    """
    print("===========start dump=======")
    try:
        for x in dir(obj):
            if x.startswith("_"):
                continue
            try:
                v = getattr(obj, x)
            except AttributeError:
                v = "AttributeError"
            print(f"{x} -> {v}")
    except TypeError:
        print("Cannot flat_dump")
