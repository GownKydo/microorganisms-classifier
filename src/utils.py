#  Cargar datos y preprocesar

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def get_data_generators(train_dir, test_dir, target_size=(128, 128), batch_size=4):
    datagen = ImageDataGenerator(rescale=1./255, rotation_range=20,
                                 width_shift_range=0.1, height_shift_range=0.1,
                                 zoom_range=0.1, horizontal_flip=True)

    train_generator = datagen.flow_from_directory(
        train_dir,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='categorical'
    )

    test_generator = datagen.flow_from_directory(
        test_dir,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=False
    )

    return train_generator, test_generator
