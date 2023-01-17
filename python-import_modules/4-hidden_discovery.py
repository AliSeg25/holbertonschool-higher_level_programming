#!/usr/bin/python3
import importlib.util
import pkgutil

if __name__ == "__main__":
    hidden_4 = importlib.util.find_spec("hidden_4")
    hidden_4 = importlib.util.module_from_spec(hidden_4)
    hidden_4.__loader__.exec_module(hidden_4)
    names = [name for name in dir(hidden_4) if not name.startswith("__")]
    names.sort()
    for name in names:
        print(name)
