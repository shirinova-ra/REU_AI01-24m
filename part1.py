import pandas as pd
import numpy as np

data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04',
             '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08',
             '2023-01-09', '2023-01-10'],
    'CoordinatesX': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    'CoordinatesY': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    'Amount_taken': [5, 10, 15, 20, 5, 10, 15, 20, 5, 10],
    'Amount_put': [50, 40, 30, 20, 60, 70, 80, 90, 100, 110],
    'Amount_taken_dispercion': [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
    'Amount_put_dispercion': [3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Responsible': ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    'Max_banknotes': [47, 80, 70, 60, 50, 40, 250, 100, 350, 400]
}

# Create the DataFrame
df = pd.DataFrame(data)
print(df)

def stress_test(df):
    must_visit = pd.DataFrame(columns=list(df.columns) + ["needed_funds"])

    for index, row in df.iterrows():
        Amount_taken = row['Amount_taken']
        Amount_put = row['Amount_put']
        Amount_taken_dispersion = row['Amount_taken_dispercion']
        Amount_put_dispersion = row['Amount_put_dispercion']
        Max_banknotes = row['Max_banknotes']

        # Calculate stress test values
        stress_test_min = Amount_put - np.sqrt(Amount_put_dispersion) - (Amount_taken + np.sqrt(Amount_taken_dispersion))
        stress_test_max = Amount_put + np.sqrt(Amount_put_dispersion) - (Amount_taken - np.sqrt(Amount_taken_dispersion))

        # Check conditions
        if stress_test_min <= 0 or stress_test_max >= Max_banknotes:
            # Calculate needed funds
            current_balance = Amount_put - Amount_taken
            target_balance = Max_banknotes / 2
            needed_funds = target_balance - current_balance

            # Create a new row with the needed_funds
            new_row = row.copy()  # Copy the current row
            new_row['needed_funds'] = needed_funds  # Add the needed_funds value

            # Append the new row to must_visit
            must_visit.loc[len(must_visit)] = new_row

    return must_visit

# Execute the function
result = stress_test(df)
print(result)
