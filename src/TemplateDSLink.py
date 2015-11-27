import dslink
import random
from twisted.internet import reactor


class TemplateDSLink(dslink.DSLink):
    def __init__(self, config):
        self.random = random.Random()
        dslink.DSLink.__init__(self, config)

    def start(self):
        reactor.callLater(0.1, self.poll)

    def get_default_nodes(self):
        root = self.get_root_node()

        test_one = dslink.Node("test_one", root)
        test_one.set_attribute("@type", "data")
        test_one.set_type("number")
        test_one.set_value(0)

        test_two = dslink.Node("test_two", root)
        test_two.set_attribute("@type", "data")
        test_two.set_type("number")
        test_two.set_value(0)

        root.add_child(test_one)
        root.add_child(test_two)

        return root

    def poll(self):
        # Poll data here
        for child_name in self.super_root.children:
            child = self.super_root.children[child_name]
            if "@type" in child.attributes and child.attributes["@type"] == "data":
                child.set_value(self.random.random())

        reactor.callLater(0.1, self.poll)

if __name__ == "__main__":
    TemplateDSLink(dslink.Configuration(name="template", responder=True))
