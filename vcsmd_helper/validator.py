import numpy as np

from vcsmd_helper.translator import translate_keys

__all__ = ['parameter_types', 'validate_types']

parameter_types = {
    'title': str,
    'calc': str,
    'ic': str,
    'iio': str,
    'alatt': {int, float},
    'nsc': list,
    'avec': list,
    'cmass': list,
    'ntype': int,
    'natom': list,
    'nameat': list,
    'atmass': list,
    'rat': list,
    'rcut': {int, float},
    'ncell': list,
    'nstep': int,
    'ntcheck': int,
    'ntimes': int,
    'temp': {int, float},
    'ttol': {int, float},
    'dt': {int, float},
    'silence': bool
}


def mapped_types(x: list, key: str):
    return {
        'avec': np.matrix(x, dtype=float),
        'rat': np.matrix(x, dtype=float),
        'nsc': np.asfarray(x),
        'cmass': np.asfarray(x),
        'natom': np.array(x, dtype=int),
        'nameat': np.array(x, dtype=str),
        'atmass': np.asfarray(x),
        'ncell': np.array(x, dtype=int)
    }[key]


def validate_types(settings: dict):
    for key, value in parameter_types.items():
        typ = type(settings[key])
        if isinstance(value, set):
            if typ not in value:
                raise TypeError("The type of {0} is not in type {1}!".format(key, value))
        else:
            if typ != value:
                raise TypeError("The type of {0} should be {1}!".format(key, value))


def translate_types(settings: dict):
    internal_settings = translate_keys(settings)
