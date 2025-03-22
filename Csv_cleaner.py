import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns   
from datetime import datetime
import sys
import os

file = sys.argv[1]

def df_loader(file):
    df = pd.read_csv(file)
    return df

def basic_info(df):
    print('Dataframe dimension: ', df.shape)
    print('\n')
    print('Basics Statistics')
    if 'ID' in df.columns:
        print('id column removed')
        print(df.drop(columns=['ID']).describe())

    else:
        print(df.describe())
    print('\n')
    print('Data Types')
    print(df.dtypes)
    print('\n')
    print('Missing or Null Values')
    print(df.isnull().sum())
    print('\n')

def first_nLines(df):
    n = int(input('Enter the number of lines you want to see: '))
    print(df.head(n))

def null_cleaner(df):
    colunm = input('Enter the name of the column you want to remove null values: ')
    df[colunm] = df[colunm].dropna()
    print('Null values removed successfully!')

def duplicate_cleaner(df):
    colunms = []
    while input == 'y':
        colunm = input('Enter the name of the column you want to remove duplicates: ')
        colunms.append(colunm.lower())
        input = input('Do you want to remove more columns? y/n: ')

    df = df.drop_duplicates(subset=colunms, keep='first', inplace=True)
    print('Duplicates removed successfully!')

def outlier_checker(df):
    colunm = input("Enter the name of the column you want to check for outliers:")
    Q1 = df[colunm].quantile(0.25)
    Q3 = df[colunm].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    print('Lower Bound: ', lower_bound)
    print('Upper Bound: ', upper_bound)
    print('Remove Outliers??')
    input = input('y/n: ')
    if input == 'y':
        df = df[(df[colunm] >= lower_bound) & (df[colunm] <= upper_bound)]
        print("Outliers removed successfully!")
    else:
        print("Operation canceled!")

def correlation_matrix(df):
    df_numeric = df.select_dtypes(include=['number'])
    corr = df_numeric.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()


def histogram(df):
    colunm = input("Enter the name of the column you want to visualize the histogram for: ")
    plt.figure(figsize=(10, 6))
    sns.histplot(df[colunm], bins=30, kde=True, color='blue')
    plt.title(f'Histogram of {colunm}')
    plt.show()

def csv_exporter(df):
    output_filename = input('Enter the file name to save (e.g., file.csv): ')
    current_directory = os.getcwd()
    output_path = os.path.join(current_directory, output_filename)
    df.to_csv(output_path, index=False)
    print('File exported successfully!')

def menu():
    print('1. Basic Info')
    print('2. First n lines')
    print('3. Null Cleaner')
    print('4. Duplicate Cleaner')
    print('5. Outlier Checker')
    print('6. Correlation Matrix')
    print('7. Histogram')
    print('8. Export to CSV')
    print('9. Exit')
    choice = int(input('Enter your choice: '))
    return choice

def main():
    df = df_loader(file)
    while True:
        choice = menu()
        if choice == 1:
            basic_info(df)
        elif choice == 2:
            first_nLines(df)
        elif choice == 3:
            null_cleaner(df)
        elif choice == 4:
            duplicate_cleaner(df)
        elif choice == 5:
            outlier_checker(df)
        elif choice == 6:
            correlation_matrix(df)
        elif choice == 7:
            histogram(df)
        elif choice == 8:
            csv_exporter(df)
        elif choice == 9:
            sys.exit()
        else:
            print('Invalid choice!')

if __name__ == '__main__':
    main()