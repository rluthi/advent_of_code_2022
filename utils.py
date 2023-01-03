def read_txt_file(path: str):
    with open(path) as f:
        string = f.read()
    return string
