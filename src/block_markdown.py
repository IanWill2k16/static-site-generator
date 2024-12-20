
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
    if block[0] == "#":
        return "heading"
    if block[:3] == '```' and block[-3:] == '```':
        return "code"
    if block[0] == ">":
        return "quote"
    if block[:2] == "* " or block[:2] == "- ":
        return "unordered list"
    if block[:2] == ". ":
        return "ordered list"
    return "paragraph"