from block_markdown import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            line = line.lstrip("# ").strip()
            return line
    raise ValueError("There is no title!!!")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")

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