__all__ = ['translate_keys']

mapping = {
    'title': 'title',
    'calculation type': 'calc',
    'initialization id': 'ic',
    'output id': 'iio',
    'alatt': 'alatt',
    'number of primitive cells': 'nsc',
    'primitive cell vectors': 'avec',
    'fictitious cell mass': 'cmass',
    'number of atom types': 'ntype',
    'number of atoms of same type': 'natom',
    'name of each atomic type': 'nameat',
    'atomic mass in proton units': 'atmass',
    'reduced atomic position': 'rat',
    'cutoff radius': 'rcut',
    'number of neighboring supercells': 'ncell',
    'number of MD timesteps': 'nstep',
    'number of steps taken before temperature is checked or rescaled': 'ntcheck',
    'number of times the temperature is checked': 'ntimes',
    'chosen temperature': 'temp',
    'relative temperature deviation tolerance': 'ttol',
    'time step in Rydberg-like units': 'dt',
    'silence': 'silence'
}


def translate_keys(settings: dict):
    internal_settings = dict()
    for key, value in mapping.items():
        internal_settings[value] = settings.pop(key)
    return internal_settings
