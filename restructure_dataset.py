import os
import shutil
import unicodedata
import re

# --- Configuración global ---
SOURCE_DIR = "data/train/Micro_organismos_images"
TARGET_DIR = "data/train"
INVALID_DIR = "data/invalid_files"
VALID_EXTENSIONS = {'.jpg', '.jpeg', '.png'}


# --- Función que regula nombres de carpetas ---
def normalize_name(name):
    name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('utf-8')
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[\s.]+', '_', name)
    return name.strip().lower()


# --- Función que mueve y renombra carpetas ---
def move_and_rename_folders():
    if not os.path.exists(SOURCE_DIR):
        print(f"No existe la carpeta fuente: {SOURCE_DIR}")
        return

    for folder in os.listdir(SOURCE_DIR):
        old_path = os.path.join(SOURCE_DIR, folder)
        if os.path.isdir(old_path):
            new_folder_name = normalize_name(folder)
            new_path = os.path.join(TARGET_DIR, new_folder_name)
            if not os.path.exists(new_path):
                shutil.move(old_path, new_path)
                print(f"Movido: {old_path} → {new_path}")
            else:
                print(f"Ya existe: {new_path}, omitiendo...")

    # Si quieres eliminar el directorio original solo si queda vacío, descomenta:
    # if not os.listdir(SOURCE_DIR):
    #     os.rmdir(SOURCE_DIR)
    #     print(f"Carpeta original eliminada: {SOURCE_DIR}")


# --- Función que mueve archivos inválidos ---
def move_invalid_files(base_dir):
    os.makedirs(INVALID_DIR, exist_ok=True)
    
    for root, _, files in os.walk(base_dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext not in VALID_EXTENSIONS:
                full_path = os.path.join(root, file)
                target_path = os.path.join(INVALID_DIR, file)
                shutil.move(full_path, target_path)
                print(f"Movido archivo inválido: {full_path} → {target_path}")


# --- Función que renombra las imágenes válidas ---
def rename_images_in_folders(base_dir):
    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)
        if not os.path.isdir(folder_path):
            continue

        image_counter = 1
        for filename in sorted(os.listdir(folder_path)):
            ext = os.path.splitext(filename)[1].lower()
            if ext in VALID_EXTENSIONS:
                new_name = f"image{image_counter:03d}{ext}"
                old_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, new_name)
                os.rename(old_path, new_path)
                print(f"Renombrado: {old_path} → {new_path}")
                image_counter += 1


# --- Ejecución principal ---
if __name__ == "__main__":
    print("🔁 Renombrando carpetas y moviendo imágenes...")
    move_and_rename_folders()
    
    print("\n🧹 Moviendo archivos no válidos...")
    move_invalid_files(TARGET_DIR)

    print("\n📝 Renombrando imágenes dentro de cada carpeta...")
    rename_images_in_folders(TARGET_DIR)
