import pandas as pd

ravi = pd.read_html('https://en.wikipedia.org/wiki/Rajeev_Ravi')
print(ravi[3])
# print(pd.__version__)
