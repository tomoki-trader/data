import optuna
from sklearn import datasets, svm, ensemble, model_selection, metrics

iris = datasets.load_iris()

target = iris.target

tr_x, va_x, tr_y, va_y = model_selection.train_test_split(data, target, random_state=0)

def objective(trial):
    classifier_category = trial.suggest_categorical("classifier", ["SVC", "RandomForest"])

    if classifier_category == "SVC":
        svc_c = trial.suggest_longuniform("SVC_C", 0.01, 100)
        svc_gamma = trial.suggest_loguniform("SVC_gamma", 0.01, 100)
