import numpy as np
import pandas as pd


def create_dataframe(in_data, in_labels): 
    data_dict = {}  # Create a blank dictionary
    data_item_number = 0  # Initialize item number for data
    total_data = 10000  # A total number of data points (calculate value from in_data
    some_data = 100     # Get value from in_data
    
    # Create an zeros/ones numpy array. If you are going to perfrom statistical analysis, you can initiate as nan
    # Then add data values to each element
    data_row = np.zeros(len(labels), np.object) * np.nan
    for d in range(total_data):
        for i in range(len(labels)):
            data_row[i] = some_data
        # Add numpy array to dictionary
        data_dict[data_item_number] = data_row
        data_item_number += 1
    
    data_df = pd.DataFrame.from_dict(data_dict, orient='index', columns=in_labels)
    return data_df


if __name__ == '__main__':
    labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G' 'H', 'I', 'J', 'K']
    data = []  # Data array 
    df = create_dataframe(data, labels)
