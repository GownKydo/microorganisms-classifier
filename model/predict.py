import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

def predict_image(image_path, model=None):
    if model is None:
        model = load_model("model/modelo_perro_vs_gato.h5")

    img = image.load_img(image_path, target_size=(150, 150))
    img_tensor = image.img_to_array(img) / 255.0
    img_tensor = np.expand_dims(img_tensor, axis=0)

    prediction = model.predict(img_tensor)[0][0]

    if prediction > 0.5:
        print(f"🐶 Predicción: Perro ({prediction * 100:.2f}% confianza)")
    else:
        print(f"🐱 Predicción: Gato ({(1 - prediction) * 100:.2f}% confianza)")
