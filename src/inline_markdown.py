from htmlnode import *
from textnode import *
import re

def split_nodes_delimeter(old_nodes, delimeter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if delimeter not in node.text:
            new_nodes.append(node)
            continue
        split_nodes = []
        split_text = node.text.split(delimeter)
        if len(split_text) % 2 == 0:
            raise ValueError(f'{node} does not contain a closing {delimeter}')
        for i in range(len(split_text)):
            if split_text[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split_text[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(split_text[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        image = extract_markdown_images(node.text)
        working_text = node.text
        for i in range(len(image)):
            split_text = working_text.split(f'![{image[i][0]}]({image[i][1]})')
            split_nodes.append(TextNode(split_text[0], TextType.TEXT))
            split_nodes.append(TextNode(f'{image[i][0]}', TextType.LINK, f'{image[i][1]}'))
            if i < len(image):
                working_text = split_text[1]
                continue
            split_nodes.append(TextNode(split_text[1], TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        links = extract_markdown_links(node.text)
        working_text = node.text
        for i in range(len(links)):
            split_text = working_text.split(f'[{links[i][0]}]({links[i][1]})')
            split_nodes.append(TextNode(split_text[0], TextType.TEXT))
            split_nodes.append(TextNode(f'{links[i][0]}', TextType.LINK, f'{links[i][1]}'))
            if i < len(links):
                working_text = split_text[1]
                continue
            split_nodes.append(TextNode(split_text[1], TextType.TEXT))
        new_nodes.extend(split_nodes)
    print(new_nodes)
    return new_nodes

