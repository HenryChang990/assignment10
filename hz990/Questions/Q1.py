import numpy as np
import pandas as pd
import exception
def Run():
    '''Answers to question 1

    '''
    print '\n-------------------Answer to question 1 -------------------'
    print '\nData loading...'
    # Loading raw data
    try:
        raw_data = pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv', index_col=0)
    except:
        raise read_csv_exception('Cannot read the csv, please check the file name and path')
    print '\nData loaded...'
    return raw_data