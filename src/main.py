from textnode import TextNode
from htmlnode import *
from copystatic import static_to_public
from page_generation import generate_page
import os

def main():
    
    static_to_public()
    content_html = generate_page('content/index.md',  'template.html', 'public/index.html')
    content = open('public/index.html', 'x')
    print(content_html)
    content.write(content_html)
    content.close()

if __name__ == '__main__':
    main()
