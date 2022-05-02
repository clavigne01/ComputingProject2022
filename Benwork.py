import matplotlib.pyplot as plt
import pandas as pd
import csv
 
df= pd.read_csv('ComputingProject.csv')
df.plot(x='volume', y='pH')
plt.xlabel('volume')
plt.ylabel('pH')
plt.title('pH Meter')
plt.show()



