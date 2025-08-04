# Red neuronal para la deteccion y clasificacion de micro organismos

## Objetivo

El objetivo de este proyecto es desarrollar un sistema de inteligencia artificial basado en redes neuronales convolucionales (CNN) capaz de detectar y clasificar diferentes tipos de microorganismos a partir de imágenes microscópicas.

<br>


## Tech Stack

General
* Python: Lenguaje principal para el desarrollo del modelo.
* Git / GitHub: Para el control de versiones y la colaboración en el código.


## Análisis de Imágenes

* TensorFlow / Keras: Framework para la creación y entrenamiento de redes neuronales.
* OpenCV: Biblioteca para el procesamiento de imágenes (opcional para preprocesamiento).

## Resultados Esperados

* Alta precisión en la clasificación de microorganismos.
* Reducción del tiempo de análisis manual.
* Base funcional para la integración en sistemas de monitoreo ambiental.


## Uso del programa

### Organizamiento del dataset

Mover las imagenes dentro de la carpeta **_"data/train/"_** y correr el codigo en python con el nombre de **"restructure_dataset.py"**, con la finalidad de poder hacer un cambio de nombre para el correcto entrenamiento de la red convolucional.

```bash
python3 restructure_dataset.py
```

### Crear una carpeta virtual para el uso de las dependencias 

```python
python3 -m venv venv
```

> Instalacion de venv: `sudo apt install python3-venv`

### Iniciar la carpeta virtual del proyecto

```bash
source venv/bin/activate
```

### Instalar paquetes necesarios dentro de la carpeta virtual

```bash
pip install --upgrade pip
pip install tensorflow matplotlib opencv-python numpy scikit-learn nvidia-cuda-runtime-cu12
```
