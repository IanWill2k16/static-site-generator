from textnode import TextNode
from htmlnode import *
from copystatic import static_to_public
from page_generation import generate_page

def main():
    
    static_to_public()
    
    content_html = generate_page('content/index.md',  'template.html', 'public/index.html')
    with open('public/index.html', 'x') as content:
        content.write(content_html)
        content.close()

if __name__ == '__main__':
    main()
