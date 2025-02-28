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



def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.key, end=' ')   # node의 key만 중위순회로 출력
        inorder(n.right)

#임시 
def preorder(n):
    if n is not None:
        print(n.key,end=" ")
        preorder(n.left)        
        preorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.key,end=" ")

global get_order

def get_order():
    while True:
        print("원하는 트리 순회 방식을 선택하시오")
        get_order = int(input("1 = inorder / 2 = preorder / 3 = postorder"))
        if (get_order == 1):
            print("inorder를 선택하셨습니다.")
            return 1
        elif (get_order == 2):
            print("preorder를 선택하셨습니다.")
            return 2
        elif (get_order == 3):
            print("postorder를 선택하셨습니다.")
            return 3
        else:
            print("잘못된 order입니다")
            

#여기까지




# 코드 9.11: 이진탐색트리를 이용한 맵 클래스
class BSTMap():
    def __init__ (self):
        self.root = None

    def isEmpty (self):
       return self.root == None

    def findMax(self):
       return search_max_bst(self.root)

    def findMin(self):
       return search_min_bst(self.root)

    def search(self, key):
       return search_bst(self.root, key)
       #return search_bst_iter(self.root, key)

    def searchValue(self, key):
       return search_value_bst(self.root, key)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty() :
           self.root = n
        else :
           insert_bst(self.root, n)

    def delete(self, key):
        self.root = delete_bst (self.root, key)

    def display(self, msg = 'BTSMap :',order= get_order()):
        print(msg, end='')
        if (order == 1):
            inorder(self.root)
        elif (order == 2):
            preorder(self.root)
        elif (order == 3):
            postorder(self.root)
        print()


#=========================================================
#   - 이 파일이 직접 실행될 때에는 다음 문장들을 실행함.
#   - 다른 파일에서 모듈로 불려지는 경우는 실행되지 않음.
#=========================================================
# 코드 9.12: 이진탐색트리를 이용한 맵 테스트 프로그램
if __name__ == "__main__":
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
    value= ["삼오", "일팔", "영칠", "이육", "일이", "영삼", "육팔", "이이", "삼영", "구구"]

    map = BSTMap()
    map.display("[삽입 전] : ")
    for i in range(len(data)) :
        map.insert(data[i],value[i])
        map.display("[삽입 %2d] : "%data[i])

    print('[최대 키] : ', map.findMax().key)
    print('[최소 키] : ', map.findMin().key)
    print('[탐색 26] : ', '성공' if map.search(26) != None else '실패')
    print('[탐색 25] : ', '성공' if map.search(25) != None else '실패')
    print('[탐색 일팔]:', '성공' if map.searchValue("일팔") != None else '실패')
    print('[탐색 일칠]:', '성공' if map.searchValue("일칠") != None else '실패')
    

