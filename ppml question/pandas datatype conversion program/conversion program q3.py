import pandas as pd
s = pd.Series(['1.000','2.500','3.1415','not a number'])
s_numeric = pd.to_numeric(s, errors='coerce')
print(s_numeric)



