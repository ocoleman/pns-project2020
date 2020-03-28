#Owen Coleman
#Project 2020
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def summary():
    with open('Analysis.txt', 'a') as f:
        f.write("TEXT GOES HERE")


def plots():
    df = pd.read_csv("iris.csv")

def main():
    summary()
    plots()




if __name__ == "__main__":
    main()