from typing_extensions import ParamSpec

P = ParamSpec('P')

def identity(*args: P.args) -> P.args:
    return args