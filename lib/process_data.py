import numpy as np
import pandas as pd
import calendar
from lib.wavelet import Wavelet
from datetime import datetime

def process_csv(file):
    """
    Processes a given csv file.

    Extracts data from a csv file with a format produced by the MDI.
    The extracted data are categorised as raw, callibrated and datetime data
    and are stored in a Wavelet object.

    Arguments:
        file -- The path to the csv file for extraction.

    Returns:
        The Wavelet object containing the processed data.
    """
    obj = Wavelet()
    datetime = []
    dataframe = pd.read_csv(file)
    datetime = get_datetime(dataframe)

    obj.raw = dataframe['raw']
    obj.datetime = datetime
    return obj

def get_datetime(dataframe):
    """
    Converts the provided dataframe date and time to Datetime objects.
    Datetime objects are required for plotting with Matplotlib.
    
    Arguments:
        dataframe -- The dataframe containing the 'time' and 'date' values.
    
    Returns:
        A list containing Datetime objects representing each date/time entry.
    """
    num_rows = len(dataframe)
    datetimes = []
    for i in range(num_rows):
        time = dataframe['time'][i]
        date = dataframe['date'][i]

        year = int(date.split(",")[-1])
        month = int(list(calendar.month_name).index(date.split(" ")[0]))
        day = int(date.split(" ")[1][:-1])
        hour, minute, second = list(map(int, time.split(":")))

        datetime_obj = datetime(year, month, day, hour, minute, second)
        datetimes.append(datetime_obj)

    return datetimes
