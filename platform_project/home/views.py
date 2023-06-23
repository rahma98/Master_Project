from django.shortcuts import render
import pandas as pd 
import csv 
from django.core.files import File
from .models import Document
from datetime import datetime
import os 
import matplotlib.pyplot as plt
from pyspark.sql import SparkSession
from pyspark.sql.functions import col



# Create your views here.
def index(request):
    #return HttpResponse('this is the home page')
    return render(request, 'index.html')



def about(request):
    return render(request, 'about.html')



def history(request):
    return render(request, 'history.html')



def features(request):
         
    if request.method == "POST":
        csv_file = request.FILES["csv_file"]
        csv_path = handle_uploaded_csv(csv_file)
        csv_data, csv_headers = read_csv_data(csv_path)  # Read all columns from the CSV
        return render(request, "features.html", {"csv_path": csv_path, "csv_data": csv_data, "csv_headers": csv_headers})
    return render(request, "features.html")


    

def handle_uploaded_csv(csv_file):
    # Generate a unique filename for the CSV file, e.g., using a timestamp
   
    filename = "df.csv"

    # Save the CSV file to the desired location
    with open(filename, "wb") as file:
        for chunk in csv_file.chunks():
            file.write(chunk)

    # Return the path of the saved CSV file
    return filename

def read_csv_data(csv_path):
    csv_data = []
    csv_headers = []
    with open(csv_path, "r") as file:
        csv_reader = csv.reader(file)
        csv_headers = next(csv_reader, [])  # Read the first row as headers
        for row in csv_reader:
            csv_data.append(row)
    return csv_data, csv_headers



def statics(request):

   # Specify the path to your CSV file
    csv_path = 'df.csv'

    # Read the CSV file using pandas
    df = pd.read_csv(csv_path)
    
    # Generate the DataFrame Information
    df_info = str(df.info(verbose=True, null_counts=True))
    # Generate the summary statistics
    summary_stats = df.describe()
    context = {'summary_stats': summary_stats,'df_info': df_info}
    return render(request, 'statics.html', context)





def eda_1(request):
    # Specify the path to your CSV file
    csv_path = 'df.csv'

    df = pd.read_csv(csv_path)

    selected_columns = []

    if request.method == "POST":
        # Get the selected columns from the form data
        selected_columns = request.POST.getlist("columns")

        # Filter the DataFrame based on selected columns
        new_dataframe = df[selected_columns].copy()
        new_dataframe.to_csv('new_dataframe.csv', index=False)
        

    # Pass the DataFrame, selected columns, and missing value options to the template context
    context = {
        "df": df,
        "selected_columns": selected_columns if selected_columns else [],
    }

    return render(request, 'eda_1.html', context)

def eda_2(request):
    # Specify the path to your CSV file
    csv_path = 'new_dataframe.csv'

    df = pd.read_csv(csv_path)

    selected_columns = []

    if request.method == "POST":
        # Get the selected columns from the form data
        selected_columns = request.POST.getlist("columns")

        for column in selected_columns:
            if column in df.columns and df[column].dtype == 'object':
                try:
                    df[column] = pd.to_datetime(df[column])
                except ValueError:
                    # Handle the case when the column cannot be converted to datetime
                    pass

        df.to_csv('new_dataframe.csv', index=False)

    # Pass the DataFrame, selected columns, and missing value options to the template context
    context = {
        "df": df,
        "selected_columns": selected_columns if selected_columns else [],
    }

    return render(request, 'eda_2.html', context)




def eda_3(request):
    # Specify the path to your CSV file
    csv_path = 'new_dataframe.csv'

    df = pd.read_csv(csv_path)

    selected_columns = []

    if request.method == "POST":
        # Get the selected columns from the form data
        selected_columns = request.POST.getlist("columns")

        # Handling missing values
        missing_value_option = request.POST.get("missing_value_option")

        for column in selected_columns:
            if column == 'column3':
                if missing_value_option == "replace_with_zero":
                    df[column] = df[column].fillna(0)
            else:
                df.dropna(subset=[column], inplace=True)

        # Save the DataFrame with missing values removed
        df.to_csv('new_dataframe.csv', index=False)

        for column in selected_columns:
            if column == 'column3':
                if missing_value_option == "replace_with_zero":
                    df[column] = df[column].fillna(0)

        # Save the DataFrame with missing values replaced by zero
        df.to_csv('new_dataframe.csv', index=False)

    # Pass the DataFrame, selected columns, and missing value options to the template context
    context = {
        "df": df,
        "selected_columns": selected_columns if selected_columns else [],
    }

    return render(request, 'eda_3.html', context)



def eda_4(request):
    # Specify the path to your CSV file
    csv_path = 'new_dataframe.csv'

    df = pd.read_csv(csv_path)

    selected_columns = []

    if request.method == "POST":
        # Get the selected columns from the form data
        selected_columns = request.POST.getlist("columns")

        # Filter the DataFrame based on selected columns
        new_dataframe = df[selected_columns].copy()
        new_dataframe.to_csv('new_dataframe.csv', index=False)
        # Handling missing values
        missing_value_option = request.POST.get("missing_value_option")

        for column in selected_columns:
            if column == 'column3':
                if missing_value_option == "replace_with_zero":
                    new_dataframe[column] = new_dataframe[column].fillna(0)
                elif missing_value_option == "remove_missing_values":
                    new_dataframe[column].dropna(inplace=True)
            else:
                new_dataframe.dropna(subset=[column], inplace=True)

        new_dataframe.to_csv('new_dataframe.csv', index=False)

    # Pass the DataFrame, selected columns, and missing value options to the template context
    context = {
        "df": df,
        "selected_columns": selected_columns if selected_columns else [],
    }

    return render(request, 'eda_4.html', context)



def eda_5(request):
    # Specify the path to your CSV file
    csv_path = 'new_dataframe.csv'

    df = pd.read_csv(csv_path)

    selected_columns = []

    if request.method == "POST":
        # Get the selected columns from the form data
        selected_columns = request.POST.getlist("columns")

        # Filter the DataFrame based on selected columns
        new_dataframe = df[selected_columns].copy()
        new_dataframe.to_csv('new_dataframe.csv', index=False)
        # Handling missing values
        missing_value_option = request.POST.get("missing_value_option")

        for column in selected_columns:
            if column == 'column3':
                if missing_value_option == "replace_with_zero":
                    new_dataframe[column] = new_dataframe[column].fillna(0)
                elif missing_value_option == "remove_missing_values":
                    new_dataframe[column].dropna(inplace=True)
            else:
                new_dataframe.dropna(subset=[column], inplace=True)

        new_dataframe.to_csv('new_dataframe.csv', index=False)

    # Pass the DataFrame, selected columns, and missing value options to the template context
    context = {
        "df": df,
        "selected_columns": selected_columns if selected_columns else [],
    }

    return render(request, 'eda_5.html', context)



def eda_6(request):
    # Specify the path to your CSV file
    csv_path = 'new_dataframe.csv'

    # Read the CSV file using pandas
    df = pd.read_csv(csv_path)
    
    # Generate the DataFrame Information
    df_info = str(df.info(verbose=True, null_counts=True))
    # Generate the summary statistics
    summary_stats = df.describe()
    # check the Nane values
    null_values=df.isnull().values.any()
    context = {'summary_stats': summary_stats,'df_info': df_info,'null_values':null_values}


    return render(request, 'eda_6.html', context)






