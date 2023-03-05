import time
from collections import defaultdict
import json

from process_functions import read_file
from process_functions import compute_mean
from process_functions import compute_groupby
from process_functions import compute_sort_values
from process_functions import compute_moving


nrows_list=[
    500, 5000, 10000, 20000, 50000,
    100000, 200000, 300000, 400000,
    500000, 600000, 700000,
    800000, 1000000, 5000000, 10000000,
    15000000, 20000000, 25000000, 30000000,
]
ncols=9

# process data
path_base = "./data"
new_ncols=ncols+2
results = defaultdict(list)

use_polars = True
# use_polars = False

for nrows in nrows_list:

    print(f"nrows={nrows}, use_polars={use_polars}")
    results["nrows"].append(nrows)
    results["ncols"].append(new_ncols)
    results["use_polars"].append(use_polars)

    path = f"{path_base}/data_{nrows}x{new_ncols}.parquet"
    start = time.time()
    df = read_file(path, use_polars=use_polars)
    finish = time.time()
    results["time_reading"].append(finish - start)

    start = time.time()
    _ = compute_mean(df, use_polars=use_polars)
    finish = time.time()
    results["time_mean"].append(finish - start)

    start = time.time()
    _ = compute_groupby(df, use_polars=use_polars)
    finish = time.time()
    results["time_groupby_mean"].append(finish - start)

    start = time.time()
    df = compute_sort_values(df, use_polars=use_polars)
    finish = time.time()
    results["time_sorting"].append(finish - start)

    start = time.time()
    df = compute_moving(df, use_polars=use_polars)
    finish = time.time()
    results["moving_average"].append(finish - start)

    del df
    del _
    with open("./output/result.json", "w") as fp:
        json.dump(results, fp)  # encode dict into JSON


import polars as pl
df.select("id", "moving")