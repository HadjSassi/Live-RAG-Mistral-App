import re

def normalize_column_name(name):
    return re.sub(r"[^\w]", "_", name)

def normalize_distinct_values(df):
    # todo compare all the distinct values of the file with the distinct values of the database and replace the incorrect ones.
    pass

def normalize_value(value):
    # todo fix the patern of the values.
    pass