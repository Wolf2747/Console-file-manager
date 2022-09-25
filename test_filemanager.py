import os
from Functions.folders_and_files import output_folders_and_files

def test_output_folders():
    text =  output_folders_and_files(os.path.isdir,[])
    assert text == ['.git', '.idea', '.pytest_cache', 'Functions', '__pycache__']
def test_output_files():
    text = output_folders_and_files(os.path.isfile,[])
    assert text == ['Console-file-manager.py', 'LICENSE', 'README.md', 'test_filemanager.py', 'test_python.py']