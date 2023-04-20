class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    import turtle
    t = turtle.Turtle()
    t.speed(0);
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


if __name__ == '__main__':
    # drawtree(deserialize('[1,2,3,null,null,4,null,null,5]'))
    drawtree(deserialize('[428,46,239,494,281,147,null,null,142,25,325,155,482,246,232,331,164,461,221,220,293,252,297,null,null,null,null,238,null,null,null,404,460,71,null,225,483,null,148,null,null,null,402,null,null,217,265,400,null,null,null,406,305,null,null,null,196,null,null,236,null,361,108,458,149,407,256,371,302,41,null,null,null,null,161,null,351,245,224,null,475,null,null,null,null,null,null,278,null,null,null,null,null,null,null,303,null,null,240,null,320,310,null,24,74,null,null,null,null,null,48,null,285,null,null,null,23,null,399]'))
