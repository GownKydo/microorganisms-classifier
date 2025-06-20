from model.train import train_model
from model.evaluate import plot_history
from model.predict import predict_image

def main():
    print("Entrenando modelo...")
    model, history = train_model()

    print("Mostrando resultados...")
    plot_history(history)

    print("Haciendo una predicción de prueba...")
    predict_image("data/train/cat.0.jpg", model)

if __name__ == "__main__":
    main()
