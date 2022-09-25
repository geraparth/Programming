class TreeNode:

    def __init__(self, name, designation):

        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def getLevel(self):

        level = 0
        iterNode = self.parent

        while iterNode:
            level += 1
            iterNode = iterNode.parent

        return level

    def addChild(self, child):

        child.parent = self
        self.children.append(child)

    # Print tree till the level given/ and the data feature required.
    def printTree(self, feature, level):

        spaces = ' ' * self.getLevel() * 3
        prefix = spaces + "|__" if self.parent else ""
        if feature == 'name':
            print(prefix + self.name)

        elif feature == 'designation':
            print(prefix + self.designation)

        elif feature == 'both':
            print(prefix + self.name + ' (' + self.designation + ')')

        if self.children:
            for child in self.children:
                if self.getLevel() < level:
                    child.printTree(feature, level)

def buildTree():

    ceo = TreeNode("Nilupul", "CEO")
    cto = TreeNode("Chinmay", "CTO")

    infraHead = TreeNode("Vishwa", "Infra Head")
    infraHead.addChild(TreeNode("Dhaval", "Cloud Manager"))
    infraHead.addChild(TreeNode("Abhijit", "App Manager"))

    cto.addChild(infraHead)
    cto.addChild(TreeNode("Amir", "Application Head"))

    hrHead = TreeNode("Gels", "HR Head")
    hrHead.addChild(TreeNode("Peter", "Recruitment Manager"))
    hrHead.addChild(TreeNode("Waqas", "Policy Manager"))

    ceo.addChild(cto)
    ceo.addChild(hrHead)

    return ceo

if __name__ =='__main__':

    root_node = buildTree()
    root_node.printTree("name", 1)  # prints only name hierarchy till level 1
    root_node.printTree("designation", 2)  # prints only designation hierarchy till level 2
    root_node.printTree("both", 0)  # prints both (name and designation) hierarchy till level 0


