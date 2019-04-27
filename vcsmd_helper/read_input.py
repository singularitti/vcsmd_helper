import json

# import crystals


__all__ = ['read_input', 'Input']


class Input(object):
    def __init__(self, settings: dict):
        self._settings = settings

    @property
    def title(self):
        return self._settings['title']

    @property
    def calculation_type(self):
        return self._settings['calc']

    @property
    def initialization_id(self):
        return self._settings['ic']

    @property
    def output_id(self):
        return self._settings['iio']


def read_input(filename: str):
    with open(filename) as f:
        settings = json.load(f)
    return settings
