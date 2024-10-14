import numpy as np
import pandas as pd

from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import recall_score
from sklearn.base import clone


def score_classifier(dataset,labels, classifiers_dict:dict)->np.ndarray:
        """Scores classifiers

        Args:
                dataset (_type_): dataset
                labels (_type_): label
                classifiers_list (_type_): dictionnaire de modèle non fittés à fitter

        Returns:
                dict: dictionnaire des scores moyens des modèles
        """
        
        results = {}
        
        for name, model in classifiers_dict.items():
                kf = StratifiedKFold(n_splits=3, shuffle=True, random_state=50)
                cross_validation_results = cross_val_score(
                        estimator=model,
                        X=dataset,
                        y=labels,
                        cv=StratifiedKFold(n_splits=3, shuffle=True, random_state=50),
                        scoring='recall'
                )
                results[name] = cross_validation_results
            
        return results