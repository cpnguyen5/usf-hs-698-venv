from api import app
import pandas as pd
import json
from flask import jsonify
import flask
import os


def get_data():
    f_name = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
            'data',
            'breast-cancer-wisconsin.csv'
        )
    print f_name
    columns = ['code', 'clump_thickness', 'size_uniformity', 'shape_uniformity',
               'adhesion', 'cell_size', 'bare_nuclei', 'bland_chromatin',
               'normal_nuclei', 'mitosis', 'class']

    df = pd.read_csv(f_name, sep=',', header=None, names=columns, na_values='?')
    return df.dropna()


@app.route('/')
def index():
    return "Hello, I'm an API!"


@app.route('/head') #head - url
def head(): #head - function to access url
    df = get_data().head() #head - dataframe
    data = json.loads(df.to_json()) #exports data frame as string --> data is python object containing it with loads
    return jsonify(data)

print head()