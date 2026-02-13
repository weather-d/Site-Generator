import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://google.com")
        self.assertEqual(node, node2)

    def test_noteqtext(self):
        node = TextNode("This is text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_noteqtexttype(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_notequrl1(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_notequrl2(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://yahoo.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()