import numpy as np

TAU = 2*np.pi

def get_data(n:int = 100, freq: float = 1) -> tuple[np.ndarray, np.ndarray]:
    x = np.linspace(0, 10, n)
    y = np.sin(TAU*x*freq)
    return x,y