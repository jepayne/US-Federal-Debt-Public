import pandas as pd
import numpy as np
#-Set up idx for indexing-#
idx = pd.IndexSlice

#----------------------------------------#
#-CUSTOM IMPORT FILES-#
#----------------------------------------#
#-List of columns that have dates-#
colsfinaldates = [  "Authorizing Act Date",
                    "First Issue Date",
                    "First Redemption Date",
                    "Final Redemption Date",
                    "Redeemable After Date",
                    "Payable Date"
                 ]

def import_csv_BondList(filename):
    """
    This function imports BondList.

    Args:
    ----------
        filename (string):      File to be imported

    Returns:
    ----------
        BondList (DataFrame): 	BondList data frame, formatted correctly

    """
    BondList = pd.read_csv(filename, index_col=0)
    for col in colsfinaldates:
        BondList[col] = pd.to_datetime(BondList[col])
    return BondList

def import_csv_BondTimeSeries(filename):
    """
    This function imports the BondQuant, BondPrice or MacroData data frames.

    Args:
    ----------
        filename (string):  File to be imported

    Returns:
    ----------
        df (DataFrame): 	Data frame, formatted correctly

    """
    df = pd.read_csv(filename)
    df = df.set_index(['L1 ID', 'Series'], drop = True)
    df = df.transpose()
    df.index = pd.to_datetime(df.index)
    return df
