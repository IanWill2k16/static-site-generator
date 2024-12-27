from textnode import TextNode
from htmlnode import *
from copy_static import static_to_public
from page_generation import generate_page_recursive
import os
import shutil

def main():
    if os.path.exists('public'):
        shutil.rmtree('public')
        print('Deleting public directory...')
    os.mkdir('public')  
    static_to_public('static', 'public')
    generate_page_recursive('content',  'template.html', 'public')


if __name__ == '__main__':
    main()
