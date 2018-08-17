import os, json
import xlsxwriter
import pandas as pd
import numpy as np

def read_by_pandas(file):
    if file.split(".")[-1] in ["csv"]:
        df = pd.read_csv(file) 
    else:
        # Load spreadsheet
        df = pd.ExcelFile(file)

    # Load a sheet into a DataFrame by name:
    sheet_data = df.parse(0)
    data = {key: sheet_data[key] for key in sheet_data}
    
    return data

def write_df(df, file):
    writer = pd.ExcelWriter(file, engine='xlsxwriter')

    # Write your DataFrame to a file     
    df.to_excel(writer, 'Sheet1')

    # Save the result 
    writer.save()

def combine_data(files, primary_key):
    
    assert len(files) == 2, "only can merge 2 files at a time"
    frames = []
    for file in files:
        frames.append(pd.ExcelFile(file).parse(0))
    return pd.merge(*frames, on=primary_key)

if __name__ == "__main__":
    input_files = ["ranjaan.xlsx", "ranjaan2.xlsx"]
    output_file = "ranjaan_out.xlsx"
    df  = combine_data(input_files, "Id")
    write_df(df, output_file)
