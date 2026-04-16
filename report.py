import pandas as pd

def generate_report(results):
    df = pd.DataFrame(results)
    df.to_csv("report.csv", index=False)