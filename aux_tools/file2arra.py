def file2array(file):
    with open(file) as input_txt:
        values = [s.strip() for s in input_txt.readlines()]
    return values