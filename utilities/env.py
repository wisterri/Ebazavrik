import os


class EnvironmentVariables(object):
    def __init__(self):
        pass


def load():
    env = EnvironmentVariables()

    with open(f'{os.getcwd()}/.env') as f:
        for line in f:
            # Skip comments.
            if line.startswith('#') or not line.strip():
                continue

            key, value = line.strip().split('=', 1)

            if value == '':
                value = None

            setattr(env, key, value)

    return env