from src.train import train_model

if __name__ == "__main__":
    train_model("data/train", "data/test", epochs=10)
