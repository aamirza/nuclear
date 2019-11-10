import os
import pickle


__all__ = ['loader', 'dumper']

def current_dir():
    return os.path.dirname(os.path.realpath(__file__))


def loader(filename):
    file_loc = f"{current_dir()}/{filename}.pk1"
    with open(file_loc, 'rb') as f:
        return pickle.load(f)


def dumper(value, filename):
    file_loc = f"{current_dir()}/{filename}.pk1"
    with open(file_loc, 'wb') as f:
        pickle.dump(value, f)
