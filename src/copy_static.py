import os
import shutil

def static_to_public(source, dest):
    print('Copying static files to public directory...')
    files = os.listdir(source)
    for file in files:
        source_filepath = os.path.join(source, file)
        dest_filepath = os.path.join(dest, file)
        print(f" * {source_filepath} -> {dest_filepath}")
        if os.path.isfile(source_filepath):
            shutil.copy(source_filepath, dest_filepath)
        else:
            os.mkdir(dest_filepath)
            static_to_public(source_filepath, dest_filepath)