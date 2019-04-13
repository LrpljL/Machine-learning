
## coding=utf-8
# 递归实现，二叉树为有序树
# 根节点，左子树，右子树

class Node(object): # This is the Class Node with constructor that contains data variable to type data and left,right pointers.
    def __init__(self, data="#"):
        self.data = data
        self.left = None
        self.right = None


def display(tree):  # In Order traversal of the tree
    """ 中序遍历  4 2 6 5 1 8 9 7 3"""
    if tree is None:
        return

    if tree.left is not None:
        display(tree.left)

    print(tree.data)

    if tree.right is not None:
        display(tree.right)

    return

# 构造二叉排序树
def bst(tree, item):
    flag=False
    if tree.data=="#":
        tree.data=item
    else:
        while not flag:
            while (tree.data > item):
                if (tree.left)==None:
                    tree.left=Node(item)
                    flag=True
                tree = tree.left
            while (tree.data < item):
                if(tree.right)==None:
                    tree.right=Node(item)
                    flag=True
                tree = tree.right

#当值相等时==为True，而只有当id相同时为True
#二叉排序树的查找
def bst_search(tree,item):
    search_flag=False
    while not search_flag:
        if (tree.data==item):
            search_flag=True
            return search_flag
        elif (tree.data>item):
            tree=tree.left
        else:
            tree=tree.right
        if tree is None:
            break

    return search_flag
#二叉排序树的插入
def insert(tree,item):
    insert_flag=False
    while not insert_flag:
        if tree.data=="#":
            tree.data=item




tree=Node()
item=[int(i) for i in input().split(",")]
# item1=int(input())
for i in item[:-1]:
    bst(tree,i)
# display(tree)
# print(tree.left.data)
print(bst_search(tree,item[-1]))
# display(tree)


# 非递归中序遍历 从根节点不断遍历每个节点的左子树，将遍历的每一个节点压栈，
# 出栈时检测右子树，同上不断循环遍历
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                t = stack.pop()
                print(t.data)
                ret.append(t.data)
                root = t.right
        return ret


# 非递归中序遍历
# def display_(tree):
#     list1=[]
#     while()


def depth_of_tree(tree): #This is the recursive function to find the depth of binary tree.
    if tree is None:
        return 0
    else:
        depth_l_tree = depth_of_tree(tree.left)   # 左子树
        print(depth_l_tree)
        depth_r_tree = depth_of_tree(tree.right)  # 右子树
        print(depth_r_tree)
        if depth_l_tree > depth_r_tree:
            return 1 + depth_l_tree
        else:
            return 1 + depth_r_tree


def is_full_binary_tree(tree): # This functions returns that is it full binary tree or not?
    if tree is None:
        return True
    if (tree.left is None) and (tree.right is None):
        return True
    if (tree.left is not None) and (tree.right is not None):
        return (is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right))
    else:
        return False



# def main():
#     tree = Node(1)
#     tree.left = Node(2)
#     tree.right = Node(3)
#     tree.left.left = Node(4)
#     tree.left.right = Node(5)
#     tree.left.right.left = Node(6)
#     tree.right.left = Node(7)
#     tree.right.left.left = Node(8)
#     tree.right.left.left.right = Node(9)
#     s=Solution()
#     print(s.inorderTraversal(tree ))


    # print("Tree is: ")
    # display(tree)
    # print(is_full_binary_tree(tree))
    # print(depth_of_tree(tree))
    # print("Tree is: ")
    # display(tree)

# if __name__ == '__main__':
#     main()


