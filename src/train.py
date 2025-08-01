# Entrenamiento del modelo CNN

from src.model import build_model
from src.utils import get_data_generators

def train_model(train_dir, test_dir, epochs=10):
    train_gen, test_gen = get_data_generators(train_dir, test_dir)
    model = build_model()
    
    model.fit(train_gen, validation_data=test_gen, epochs=epochs)
    model.save("modelo_microorganismos.h5")
