from textnode import TextNode, TextType

def main():
    deernode = TextNode("Hello this is Deer", TextType.BOLD, "https://i.etsystatic.com/27968380/r/il/5a6857/4191002630/il_570xN.4191002630_4hqh.jpg")
    print(repr(deernode))

main()