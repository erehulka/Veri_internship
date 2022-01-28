import pandas as pd
import numpy as np

dataset: pd.DataFrame
while True:
    print('Enter absolute path to .csv with the data')
    fname = input()
    try:
        dataset = pd.read_csv(fname, header=None)
        break
    except Exception as e:
        print('File not found, try again')

def generate_scores_v6_2(dataset: pd.DataFrame) -> np.array:
  result = []

  for i, row in dataset.iterrows():
    score: int = 0
    stddev: float = min(np.std(row[0:5]), np.std(row[1:5]))
    score = 5 - min(np.floor(stddev * 5), 5)
    for j in range(4,9):
      if np.round(row[j],1) >= np.round(row[j+1] - 0.2,1): score += 1
    
    result.append(score)
  
  return np.array(result)

while True:
    print('Where do you want to save the result? (Absolute path) wirth .csv at the end')
    result_fname: str = input()
    try:
        np.savetxt(result_fname, generate_scores_v6_2(dataset), delimiter=",")
        break
    except Exception as e:
        print('Enter correct path, with .csv at the end of the file name')
