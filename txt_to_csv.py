import pandas as pd

def convert_to_csv(filename, new_filename):
    df = pd.read_csv(filename)
    df.to_csv(new_filename, index=None)