import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline


def pipeline(data):
    pipeline = [StandardScaler()]
    tr = make_pipeline(*pipeline)
    X = tr.fit_transform(data)
    X = pd.DataFrame(X,columns=data.columns)
    return X

def clean_columns(data):
    data["cut_numeric"] = data.cut.map( {"Ideal": 5, "Premium": 4, "Very Good": 3, "Good": 2, "Fair": 1} )
    data["color_numeric"] = data.color.map( {"D": 7, "E": 6, "F": 5, "G": 4, "H": 3, "I": 2, "J": 1} )
    data["clarity_numeric"] = data.clarity.map( {"IF": 8,"VVS1": 7, "VVS2": 6, "VS1": 5, "VS2": 4, "SI1": 3, "SI2": 2, "I1": 1} )
    return data
