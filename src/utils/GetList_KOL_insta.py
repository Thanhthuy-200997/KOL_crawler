import os

def load_list_KOL(path:str)->list:
    with open(path) as file_in:
        lines = []
        for line in file_in:
            line = line.replace('\n', '')
            lines.append(line)
    return lines