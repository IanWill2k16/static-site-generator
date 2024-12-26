from htmlnode import ParentNode, LeafNode, HTMLNode
from textnode import TextNode
from inline_markdown import text_to_textnodes

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(('#', '##', '###', '####', '#####', '######')):
        return block_type_heading
    if len(lines) > 1 and lines[0] == "```" and lines[-1] == "```":
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        for i in range(len(lines)):
            if not lines[i].startswith(f"{i + 1}. "):
                return block_type_paragraph
        return block_type_olist
    return block_type_paragraph

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_heading:
            heading = block.split(" ")[0].count("#")
            new_text = " ".join(block.split(" ")[1:])
            nodes.append(ParentNode(f"h{heading}", text_to_textnodes(new_text)))
        if block_type == block_type_paragraph:
            lines = block.split("\n")
            new_line = ""
            for line in lines:
                new_line += f"{line.strip()} "
            nodes.append(ParentNode("p", text_to_textnodes(new_line.strip())))
        if block_type == block_type_code:
            new_text = []
            block = block.lstrip('```')
            block = block.rstrip('```')
            lines = block.split("\n")
            for line in lines:
                if line == "":
                    continue
                line += "\n"
                new_text.append(text_to_textnodes(line.strip())[0])
            blocknode = ParentNode("code", new_text)
            nodes.append(ParentNode("pre", blocknode))
        if block_type == block_type_quote:
            new_text = []
            lines = block.split("\n")
            for line in lines:
                line = line.lstrip("> ")
                new_text.append(text_to_textnodes(line.strip())[0])
            nodes.append(ParentNode("blockquote", new_text))
        if block_type == block_type_ulist:
            child_nodes = []
            lines = block.split("\n")
            for line in lines:
                line = line.lstrip('- ')
                line = line.lstrip('* ')
                child_nodes.append(ParentNode("li", text_to_textnodes(line)))
            nodes.append(ParentNode("ul", child_nodes))
        if block_type == block_type_olist:
            child_nodes = []
            lines = block.split("\n")
            for i in range(len(lines)):
                line = lines[i].lstrip(f"{i + 1}. ")
                child_nodes.append(ParentNode("li", text_to_textnodes(line)))
            nodes.append(ParentNode("ol", child_nodes))
    fin = ParentNode("div", nodes, None)
    # print(fin.tag)
    return fin
    