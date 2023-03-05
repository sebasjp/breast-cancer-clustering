import json
import polars as pl
import seaborn as sns
import matplotlib.pyplot as plt

# Opening JSON file
f = open('./output/result_polars.json')
# returns JSON object as a dictionary
results_polars = json.load(f)
f.close()

f = open('./output/result_pandas.json')
results_pandas = json.load(f)
f.close()

# result in dataframe format
results_pandas = pl.DataFrame(results_pandas)
results_polars = pl.DataFrame(results_polars)
# concat results
results = pl.concat([results_pandas, results_polars])
results = results.with_columns(
    pl.when(pl.col("use_polars"))
    .then("polars")
    .otherwise("pandas")
    .alias("library")
)
results = results.with_columns(pl.col("nrows") / 10**6)

# plot results
# results.columns: # ['time_reading', 'time_mean', 'time_groupby_mean', 'time_sorting', 'moving_average']
feature_str="moving_average"
sns.lineplot(
    x="nrows",
    y=feature_str, 
    hue="library",
    style="library",
    markers=True,
    data=results.filter(pl.col("nrows") < 5)
)
plt.title(feature_str + ": seconds")
plt.show()

sns.lineplot(
    x="nrows",
    y=feature_str, 
    hue="library",
    style="library",
    markers=True,
    data=results.filter(pl.col("nrows") >= 5)
)
plt.title(feature_str + ": seconds")
plt.show()
