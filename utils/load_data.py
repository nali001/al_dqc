import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_train_test(split_type, float_number): 
    TRAIN_DIR = f'./data/{split_type}split/train/'
    TEST_DIR = f'./data/{split_type}split/test/'

    TRAIN_FILE = os.path.join(TRAIN_DIR, f'PR_PF_{float_number}.csv')
    TEST_FILE = os.path.join(TEST_DIR, f'PR_PF_{float_number}.csv')

    train_df = pd.read_csv(TRAIN_FILE)
    test_df = pd.read_csv(TEST_FILE)
    # train_data.drop(['ID', 'Date'], axis=1, inplace=True)
    # test_data.drop(['ID', 'Date'], axis=1, inplace=True)
    X_train = train_df.drop(columns=['ID', 'Date', 'Label'])  # Replace 'label_column' with the actual label column name
    X_test = test_df.drop(columns=['ID', 'Date', 'Label'])

    # Standardize the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)
    return X_train_scaled, X_test_scaled