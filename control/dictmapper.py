"""
dictmapper
------------------------
maps dictionaries (output/input from json files)
to model classes used to create the interface for the backend.
------------------------
"""
from model import balance, entry, result


class BalMapper():
    """Static Function class"""
    def __init__(self) -> None:
        pass

    @staticmethod
    def dictToClass(name, dictValue):
        return balance.Balance(name, dictValue["init_value"],
                               dictValue["value"])

    @staticmethod
    def classToDict(balInstance):
        dict = {}
        dict[balInstance.name] = {"init_value": balInstance.initValue,
                                  "value": balInstance.value}
        return dict


class ResMapper():
    "Static Function class"
    def __init__(self) -> None:
        pass

    @staticmethod
    def dictToClass(key, value):
        return result.Result(key, value)

    @staticmethod
    def classToDict(resInst):
        dict = {}
        dict[resInst.name] = resInst.value
        return dict


class EntryMapper():
    "static class for entries"
    def __init__(self) -> None:
        pass

    @staticmethod
    def dictToClass(dict):
        return entry.Entry(dict["month"], dict["value"],
                           dict["post"], dict["payBy"], dict["comment"])

    @staticmethod
    def classToDict(res):
        return {"month": res.month, "value": res.value,
                "post": res.post, "payBy": res.payBy, "comment": res.comment}


if __name__ == "__main__":
    balanceEntry = BalMapper.dictToClass("bank", {"init_value": 5000,
                                         "value": 6000})
    print(f"class: {balanceEntry.name}, {balanceEntry.value}")
