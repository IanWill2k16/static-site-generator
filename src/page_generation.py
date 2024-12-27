from block_markdown import markdown_to_html_node
import os
import pathlib

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            line = line.lstrip("# ").strip()
            return line
    raise ValueError("There is no title!!!")

def generate_page(from_path, template_path, dest_path):
    with open(from_path) as from_file:
        markdown = from_file.read()
        from_file.close()

    with open(template_path) as template_file:
        template = template_file.read()
        template_file.close()

    content_nodes = markdown_to_html_node(markdown)
    content_html = content_nodes.to_html()
    title = extract_title(markdown)

    template = template.replace('{{ Title }}', title)
    template = template.replace('{{ Content }}', content_html)
    
    return template

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    content_files = os.listdir(dir_path_content)
    for file in content_files:
        source_file_dir = os.path.join(dir_path_content, file)
        dest_file_dir = os.path.join(dest_dir_path, file)
        if os.path.isfile(source_file_dir):
            dest_file_html = dest_file_dir.split('.md')[0] + '.html'
            print(f"Generating page from {source_file_dir} to {dest_file_html} using {template_path}...")
            with open(dest_file_html, 'x') as content:
                content.write(generate_page(source_file_dir, template_path, dest_file_dir))
                content.close()
        else:
            os.mkdir(dest_file_dir)
            generate_page_recursive(source_file_dir, template_path, dest_file_dir)