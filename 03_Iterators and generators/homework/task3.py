import os


def count_python_files(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    count = 0
                    for line in lines:
                        if line.strip() and not line.strip().startswith('#'):
                            count += 1
                    yield count


for count in count_python_files('.'):
    print(count)
