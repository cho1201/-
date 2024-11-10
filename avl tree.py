# CircularQueue.py
class CircularQueue :
    def __init__( self, capacity = 8 ) :
        self.capacity = capacity        # 용량(고정)
        self.array = [None] * capacity  # 요소들을 저장할 배열
        self.front = 0                  # 전단의 인덱스
        self.rear = 0                   # 후단의 인덱스

    def isEmpty( self ) :
       return self.front == self.rear

    def isFull( self ) :
       return self.front == (self.rear+1)%self.capacity

    def enqueue( self, item ):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item

    def dequeue( self ):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]

    def peek( self ):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]

    def size( self ) :
       return (self.rear - self.front + self.capacity) % self.capacity

    def __str__(self):
        if self.front < self.rear :
            return str(self.array[self.front+1:self.rear+1])
        else :
            return str(self.array[self.front+1:self.capacity] + \
                       self.array[0:self.rear+1] )


#======================================================================
if __name__ == "__main__":
    q = CircularQueue(8)
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    q.enqueue('D')
    q.enqueue('E')
    q.enqueue('F')
    print('A B C D E F 삽입: ', q)
    print('삭제 -->', q.dequeue())
    print('삭제 -->', q.dequeue())
    print('삭제 -->', q.dequeue())
    print('      3번의 삭제: ', q)
    q.enqueue('G')
    q.enqueue('H')
    q.enqueue('I')
    print('      G H I 삽입: ', q)


# 코드 8.1: 이진트리를 위한 노드 클래스
class TNode:
    def __init__ (self, elem, left, right):
        self.data = elem 
        self.left = left
        self.right = right

    def isLeaf(self):
        return self.left is None and self.right is None

# 코드 8.2: 이진트리의 전위순회
def preorder(n) :
    if n is not None :
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)

# 코드 8.3: 이진트리의 중위순회
def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

# 코드 8.4: 이진트리의 후위순회
def postorder(n) :
    if n is not None :
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

# 코드 8.5: 이진트리의 레벨순회

def levelorder(root) :
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

# 코드 8.6: 이진트리의 노드 수 계산
def count_node(n) :
    if n is None : 
        return 0
    else : 
        return 1 + count_node(n.left) + count_node(n.right)

# 코드 8.7: 이진트리의 단말노드 수 계산      
def count_leaf(n) :
    if n is None : return 0
    elif n.isLeaf() : return 1
    else : return count_leaf(n.left) + count_leaf(n.right)


# 코드 8.8: 이진트리의 트리의 높이 계산
def calc_height(n) :
    if n is None : return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight) : return hLeft + 1
    else: return hRight + 1

# 기타 연산들
def evaluate(n) :
    if n is None :
       return 0
    elif n.left is None and n.right is None :
       return n.data
    else :
        op1 = evaluate(n.left)
        op2 = evaluate(n.right)
        if n.data == '+' : return op1 + op2
        elif n.data == '-' : return op1 - op2
        elif n.data == '*' : return op1 * op2
        elif n.data == '/' : return op1 / op2

def calc_size(n) :
    if n is None : 
        return 0
    else : 
        return n.data + calc_size(n.left) + calc_size(n.right)

#=========================================================
#   - 이 파일이 직접 실행될 때에는 다음 문장들을 실행함.
#   - 다른 파일에서 모듈로 불려지는 경우는 실행되지 않음.
#=========================================================
# 테스트 프로그램
if __name__ == "__main__":
    print("\n======= 이진트리 테스트 ===================================") 
    d = TNode('D', None, None)
    e = TNode('E', None, None)
    b = TNode('B', d, e)
    f = TNode('F', None, None)
    c = TNode('C', f, None)
    root = TNode('A', b, c)

    print('\n   In-Order : ', end='')
    inorder(root)
    print('\n  Pre-Order : ', end='')
    preorder(root)
    print('\n Post-Order : ', end='')
    postorder(root)
    print('\nLevel-Order : ', end='')
    levelorder(root)
    print()

    print(" 노드의 개수 = %d개" % count_node(root))
    print(" 단말의 개수 = %d개" % count_leaf(root))
    print(" 트리의 높이 = %d" % calc_height(root))

def testExprTree() :
    n1 = TNode(3, None, None)
    n2 = TNode(2, None, None)
    n3 = TNode('*', n1, n2)
    n4 = TNode(5, None, None)
    n5 = TNode(6, None, None)
    n6 = TNode('-', n4, n5)
    root = TNode('+', n3, n6)

    tree = BinaryTree(root)
    tree.printInOrder   ('Evaluate Expression : ')
    print(' ==> ' + str(evaluate(root)))

def testFolderSize() :
    m4 = TNode(200, None, None)
    m5 = TNode(500, None, None)
    m3 = TNode(100, m4, m5)
    m2 = TNode(50, None, None)
    root = TNode(0, m2, m3)
    tree = BinaryTree(root)
    print("Calculate Folder Size = %d KB" % calc_size(root))

#testBinaryTree()
#testExprTree()
#testFolderSize()

# 코드 9.1: 이진탐색트리를 위한 노드 클래스 
class BSTNode:
    def __init__ (self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def isLeaf(self):
        return self.left is None and self.right is None

#################################################################

# 코드 9.2: 이진탐색트리의 탐색 연산(순환 구조)
def search_bst(n, key) :
    if n == None :
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

# 코드 9.3: 이진탐색트리의 탐색 연산(반복 구조)
def search_bst_iter(n, key) :
    while n != None :
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n = n.right
    return None

# 코드 9.4: 이진탐색트리의 값을 이용한 탐색 연산
def search_value_bst(n, value) :
    if n == None :
        return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value)
    if res is not None :
       return res
    return search_value_bst(n.right, value)


# 코드 9.5: 최대와 최소 키를 가지는 노드 탐색 연산
def search_max_bst(n) :
    while n != None and n.right != None:
        n = n.right
    return n

def search_min_bst(n) :
    while n != None and n.left != None:
        n = n.left
    return n


#################################################################

# 코드 9.6: 이진탐색트리의 삽입 연산(순환 구조) 
def insert_bst(r, n) :
    if n.key < r.key:
        if r.left is None :
           r.left = n
           return True
        else :
           return insert_bst(r.left, n)
    elif n.key > r.key :
        if r.right is None :
           r.right = n
           return True
        else :
           return insert_bst(r.right, n)
    else : 
        return False

#################################################################

# 코드 9.7: 단말노드의 삭제 연산(case1) 
def delete_bst_case1 (parent, node, root) :
    if parent is None: 			# 삭제할 단말 노드가 루트이면 
        root = None			    # 공백 트리가 됨
    else :
        if parent.left == node:	# 삭제할 노드가 부모의 왼쪽 자식이면
            parent.left = None	# 부모의 왼쪽 링크를 None
        else :				    # 오른쪽 자식이면
            parent.right = None	# 부모의 오른쪽 링크를 None
    return root

# 코드 9.8: 자식이 하나인 노드의 삭제 연산(case2)
def delete_bst_case2 (parent, node, root) :
    if node.left is not None :	# 삭제할 노드가 왼쪽 자식만 가짐 
        child = node.left		# child는 왼쪽 자식
    else :				        # 삭제할 노드가 오른쪽 자식만 가짐
        child = node.right		# child는 오른쪽 자식

    if node == root :			# 없애려는 노드가 루트이면
        root = child			# 이제 child가 새로운 루트가 됨
    else :
        if node is parent.left : 	# 삭제할 노드가 부모의 왼쪽 자식
            parent.left = child		# 부모의 왼쪽 링크를 변경
        else :				        # 삭제할 노드가 부모의 오른쪽 자식
            parent.right = child	# 부모의 오른쪽 링크를 변경
    return root

# 코드 9.9: 자식이 둘인 노드의 삭제 연산(case2)
def delete_bst_case3 (parent, node, root) :
    succp = node			    # 후계자의 부모 노드
    succ = node.right			# 후계자 노드
    while (succ.left != None) :	# 후계자와 부모노드 탐색
        succp = succ			
        succ = succ.left

    if (succp.left == succ) :	# 후계자가 왼쪽 자식이면
        succp.left = succ.right	# 후계자의 오른쪽 자식 연결
    else :				        # 후계자가 오른쪽 자식이면
        succp.right = succ.right	# 후계자의 왼쪽 자식 연결

    node.key = succ.key			# 후계자의 키와 값을
    node.value= succ.value		# 삭제할 노드에 복사
    node = succ			        # 실제로 삭제하는 것은 후계자 노드

    return root

# 코드 9.10: 이진탐색트리의 삭제 연산
def delete_bst (root, key) :
    if root == None : return None       # 공백 트리

    parent = None                       # 삭제할 노드의 부모 탐색
    node = root                         # 삭제할 노드 탐색
    while node != None and node.key != key :
        parent = node
        if key < node.key : node = node.left
        else : node = node.right;
    if node == None : return root       # 삭제할 노드가 없음

	# case 1: 단말 노드
    if node.left == None and node.right == None :
        root = delete_bst_case1 (parent, node, root)

	#  case 2: 하나의 자식을 가진 노드
    elif node.left==None or node.right==None :
        root = delete_bst_case2 (parent, node, root)

	#  case 3: 두 개의 자식을 가진 노드
    else :
        root = delete_bst_case3 (parent, node, root)

    return root


def calc_height(n) :
    if n is None : return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight) : return hLeft + 1
    else: return hRight + 1

# 코드 9.13: 노드의 균형인수 계산 함수
def calc_height_diff(n) :
    if n==None :
       return 0
    return calc_height(n.left) - calc_height(n.right)
'''
# 코드 9.14: AVL 트리의 LL회전     (수정)
def rotateLL(A) :
    B = A.left
    if calc_height(n.left) > calc_height(n.right):
        A.left = B.right
        B.right = A    
    else:
        A.left = B.left
        B.left = A
    return B
        
# 코드 9.15: AVL 트리의 RR회전     (수정)
def rotateRR(A) :
    B = A.right
    if calc_height(n.left) < calc_height(n.right):
        A.right = B.left
        B.left = A
    else:
        A.right = B.right
        B.right = A
    return B
'''
# 코드 9.14: AVL 트리의 LL회전     
def rotateLL(A) :
	B = A.left
	A.left = B.right
	B.right = A
	return B

# 코드 9.15: AVL 트리의 RR회전     
def rotateRR(A) :
	B = A.right
	A.right = B.left
	B.left = A
	return B

# 코드 9.16: AVL 트리의 RL회전
def rotateRL(A) :
	B = A.right
	A.right = rotateLL(B)
	return rotateRR(A)

# 코드 9.17: AVL 트리의 LR회전
def rotateLR(A) :
	B = A.left
	A.left = rotateRR(B)
	return rotateLL(A)

# 코드 9.18: AVL 트리의 재균형 함수
def reBalance (parent) :
	hDiff = calc_height_diff(parent)

	if hDiff > 1 :
		if calc_height_diff( parent.left ) > 0 :
			parent = rotateLL( parent )
		else :
			parent = rotateLR( parent )
	elif hDiff < -1 :
		if calc_height_diff( parent.right ) < 0 :
			parent = rotateRR( parent )
		else :
			parent = rotateRL( parent )
	return parent

# 코드 9.19: AVL 트리의 삽입 연산
def insert_avl(parent, node) :
    if node.key < parent.key :
        if parent.left != None :
            parent.left = insert_avl(parent.left, node)
        else :
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key :
        if parent.right != None :
            parent.right = insert_avl(parent.right, node)
        else :
            parent.right = node
        return reBalance(parent);
    else :
        print("중복된 키 에러")

#삭제 연산ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def delete_avl(root, key):
    # 삭제할 노드를 찾음
    if root is None:
        return None

    # 삭제할 키를 가진 노드를 탐색
    if key < root.key:
        root.left = delete_avl(root.left, key)
    elif key > root.key:
        root.right = delete_avl(root.right, key)
    else:
        # 경우 1: 단말 노드일 때
        if root.left is None and root.right is None:
            root = None
        # 경우 2: 하나의 자식 노드만 있을 때
        elif root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
        # 경우 3: 두 개의 자식이 있는 경우
        else:
            # 오른쪽 서브트리에서 최소값을 찾음
            min_node = search_min_bst(root.right)
            root.key = min_node.key
            root.right = delete_avl(root.right, min_node.key)

    # 트리의 균형을 맞춤
    if root is not None:
        root = reBalance(root)

    return root



def levelorder(root) :
    queue = CircularQueue(100)
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.key, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)




# 코드 9.20: AVL 트리 테스트 프로그램
if __name__ == "__main__":
    node = [7,8,9,2,1,5,3,6,4]

    root = None
    for i in node:
        n = BSTNode(i)
        if root is None:
            root = n
        else:
            root = insert_avl(root, n)

        print("AVL Insert(%d): " % i, end='')
        levelorder(root)
        print()

    print(" 노드의 개수 =", count_node(root))
    print(" 단말의 개수 =", count_leaf(root))
    print(" 트리의 높이 =", calc_height(root))

    # AVL 트리에서 노드 삭제 테스트
    print("\n=== AVL Tree Deletion Test ===")
    for i in node:
        root = delete_avl(root, i)
        print("AVL Delete(%d): " % i, end='')
        levelorder(root)
        print()

    print("삭제 후 트리의 노드 개수 =", count_node(root))
    print("삭제 후 트리의 단말 개수 =", count_leaf(root))
    print("삭제 후 트리의 높이 =", calc_height(root))

    
'''
    for i in node :
        n = BSTNode(i)
        if root == None :
            root = n
        else :
           root = delete_avl(root, n)
        print("AVL(%d): "%i, end='')
        levelorder(root)
        print()
'''
