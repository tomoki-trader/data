import optuna
import plotly
import time
import random
import os
from joblib import Parallel, delayed

def _func(x, y):
    return (x - 2)**2

def objective(trial):
    x = trial.suggest_float('x', -10, 10)
    y = trial.suggest_float('y', -3, 3)
    return _func(x, y)

def main():
    start = time.time()
    study = optuna.create_study()
    study.optimize(objective, n_trials=100)
    print("best_params of x, y:{}".format(study.best_params))
    print("best_values of z:{}".format(study.best_value))
    print("best_trial of x, y, z:{}".format(study))
    print("total time is {}".format(time.time() - start))

if __name__ =="__main__":
    main()