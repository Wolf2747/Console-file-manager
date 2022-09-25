def output_folders_and_files(root,dirs):
    import os

    dirname = '/py. Проекты/Console-file-manager/'
    dirfiles = os.listdir(dirname)

    fullpaths = map(lambda name: os.path.join(name), dirfiles)

    # dirs = []

    for file in fullpaths:
        if root(file):
            dirs.append(file)
    return dirs

# if os.path.isfile(file):
#     files.append(file)