from sklearn.datasets import make_regression
import pandas as pd
import numpy as np


def create_dataframe(
        nrows: int,
        ncols: int,
        output_path: str,        
        random_state: int=421,
    ):
    """
    https://towardsdatascience.com/generate-your-sample-dataset-a-must-have-skill-for-data-scientists-36ded8600b79
    """
    # Generate fetures and outputs of samples
    features, output = make_regression(n_samples=nrows,
                                       n_features=ncols,
                                       random_state=random_state)
    colnames = ["x" + str(i) for i in range(1, ncols+1)]
    dataframe = pd.DataFrame(features, columns=colnames)
    dataframe["id"] = np.random.randint(0, round(nrows*0.1), size=nrows)
    dataframe["target"] = output
    
    # save dataframe as parquet file
    new_ncols = dataframe.shape[1]
    dataframe.to_parquet(f"{output_path}/data_{nrows}x{new_ncols}.parquet")
    memory_ = dataframe.memory_usage(deep=True).sum()/ 1000000 
    memory_ = round(memory_)
    print(f"nrows={nrows}; memory={memory_}MB")

def create_data(
    nrows_list: list,
    ncols: int, 
    output_path: str="./data"
    ):
    
    for nrows in nrows_list:
        create_dataframe(
            nrows=nrows, 
            ncols=ncols, 
            output_path=output_path
        )

# create dataframes with diferent size
nrows_list=[
    500, 5000, 10000, 20000, 50000,
    100000, 200000, 300000, 400000,
    500000, 600000, 700000,
    800000, 1000000, 5000000, 10000000,
    15000000, 20000000, 25000000, 30000000,
]
ncols=9
# This function returns 2 columns more: id and target. 
# i.e. the result will be of ncols+2 columns
create_data(nrows_list=nrows_list, ncols=ncols)