import os


def gen_files_path(target_dir='/', target_subdir=''):
    for root, dirs, files in os.walk(target_dir):
        if target_subdir in dirs:
            subdir_path = os.path.join(root, target_subdir)
            for dirpath, dirnames, filenames in os.walk(subdir_path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    yield file_path


files = gen_files_path('/usr', 'bin')
for file in files:
    print(file)