from celery import shared_task
import shutil
import os

PERM_DIR = "/Users/dave/projects/music-player/cdn"


@shared_task
def process_uploaded_file(file_path, user):
    try:
        filename = os.path.basename(file_path)
        new_dir = f"{PERM_DIR}/{user}/{filename}"

        new_dir = f"{PERM_DIR}/dave"
        new_full_path = f"{new_dir}/{filename}"
        os.makedirs(new_dir, exist_ok=True)
        shutil.move(file_path, new_full_path)

        return f"Processed and moved the file to {new_full_path}."
    except Exception as e:
        return f"Error processing the file: {str(e)}"
