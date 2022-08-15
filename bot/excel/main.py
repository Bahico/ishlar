import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


excel = "one.xlsx"

df_first_shift = pd.read_excel(excel, sheet_name='first')
df_second_shift = pd.read_excel(excel, sheet_name='second')