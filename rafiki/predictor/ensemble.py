import numpy as np
from collections import Iterable

from rafiki.constants import TaskType

def ensemble_predictions(predictions_list, task):
    if len(predictions_list) == 0 or len(predictions_list[0]) == 0:
        return []

    if task == TaskType.IMAGE_CLASSIFICATION:
        # Compute mean of probabilities across predictions 
        predictions = []
        for preds in np.transpose(predictions_list, axes=[1, 0, 2]):
            predictions.append(np.mean(preds, axis=0))
    else:
        # By default, just return some trial's predictions
        index = 0
        predictions = predictions_list[index]

    predictions = _simplify_predictions(predictions)

    return predictions

def _simplify_predictions(predictions):
    # Convert numpy arrays to lists
    if isinstance(predictions, np.ndarray):
        predictions = predictions.tolist()

    if isinstance(predictions, Iterable):
        for i in range(len(predictions)):
            if isinstance(predictions[i], np.ndarray):
                predictions[i] = predictions[i].tolist()

    return predictions