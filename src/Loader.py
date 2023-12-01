def LoadInputs(path: str) -> str:
    txt = ""
    with open(path) as f:
        txt = f.read()
    return txt