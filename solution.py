import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 464814509 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = x.size
    bias = 0.089
    return (bias + (np.max(x) - bias) / ((1 - alpha / 2)**(1/n)), bias + (np.max(x) - bias) / ((alpha / 2)**(1/n)))
