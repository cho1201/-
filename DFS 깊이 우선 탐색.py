
# 코드 4.2: 배열로 구현된 스택 클래스 (참고 파일: ch04/ArrayStack.py)

class ArrayStack :
    def __init__( self, capacity ):	        # 생성자 정의
        self.capacity = capacity		    # 용량(고정)
        self.array = [None]*self.capacity	# 요소들을 저장할 배열
        self.top = -1			            # 스택 상단의 인덱스

    # 코드 1.2b: 스택 클래스의 연산들
    def isEmpty( self ) :
       return self.top == -1

    def isFull( self ) :
       return self.top == self.capacity-1

    def push( self, item ):
        if not self.isFull() :
            self.top += 1
            self.array[self.top] = item
        else: pass              # overflow 예외는 처리하지 않았음

    def pop( self ):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else: pass              # underflow 예외는 처리하지 않았음

    def peek( self ):
        if not self.isEmpty():
            return self.array[self.top]
        else: pass              # underflow 예외는 처리하지 않았음

    def __str__(self ) :
        return str(self.array[0:self.top+1][::-1])

    def size( self ) : return self.top+1


#=========================================================
# 코드 1.3: 문자열 역순 출력 프로그램
#   - 이 파일이 직접 실행될 때에는 다음 문장들을 실행함.
#   - 다른 파일에서 모듈로 불려지는 경우는 실행되지 않음.
#=========================================================
if __name__ == "__main__":
    s = ArrayStack(10)
    for i in range(1,6):		# i = 1, 2, 3, 4, 5
        s.push(i)			    # push 연산 5회 
    print(' push 5회: ', s)	        # 스택 내용 출력
    print(' push 5회: ', s.array)	# 스택 내용 출력





map =[[ '1', '0', '1', '1', '1', '1' ,'1' ,'0' ,'1' ,'1' ],
          [ 'e', '0', '0', '0', '0', '1' ,'0' ,'0' ,'1' ,'1' ],
          [ '0', '1', '1', '1', '0', '1' ,'0' ,'1' ,'1' ,'1' ],
          [ '0', '1', '1', '0', '0', '0' ,'0' ,'1' ,'1' ,'1' ],
          [ '0', '0', '1', '0', '1', '1' ,'1' ,'1' ,'1' ,'1' ],
          [ '1', '0', '1', '0', '0', '0' ,'1' ,'0' ,'1' ,'1' ],
          [ '1', '0', '1', '1', '1', '0' ,'0' ,'0' ,'1' ,'x' ],
          [ '1', '0', '0', '0', '1', '1' ,'1' ,'0' ,'1' ,'0' ],
          [ '1', '0', '1', '0', '1', '1' ,'1' ,'0' ,'1' ,'0' ],
          [ '0', '0', '1', '1', '1', '1' ,'1' ,'0' ,'0' ,'0' ]]
                
MAZE_SIZE = 10


# 코드 4.7: 갈 수 있는 위치인지를 판단하는 알고리즘 (참고 파일: ch04/MazeStack.py)
def isValidPos(x, y) :		# (x,y)가 갈 수 있는 방인지 검사하는 함수
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE :
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False


def DFS() :			# 깊이우선탐색 함수
    global count                # 전역 변수 count 선언
    count = 0
    print('DFS: ')
    stack = ArrayStack(100)	# 사용할 덱 객체를 준비
    stack.push((0,1))		# 후단에 시작위치 삽입. (0,1)은 튜플

    while not stack.isEmpty(): 	# 공백이 아닐 동안 
        here = stack.pop()      # 후단에서 항목을 꺼냄(pop)
        count += 1              # 실행될 때마다 count를 1씩 더함
        print(here, end='->')
        (x,y) = here

        if (map[y][x] == 'x') :	# 출구이면 성공. True 반환
            return True
        else :
            map[y][x] = '.'	# 현재위치를 지나왔다고 ’.’표시
            if isValidPos(x, y - 1): stack.push((x, y - 1)) # 상
            if isValidPos(x + 1, y): stack.push((x + 1, y)) # 우
            if isValidPos(x, y + 1): stack.push((x, y + 1)) # 하
            if isValidPos(x - 1, y): stack.push((x - 1, y)) # 좌
        print(' 현재 스택: ', stack)
    return False

result = DFS()
if result : print(' --> 미로탐색 성공')
else : print(' --> 미로탐색 실패')
print("이동거리:",count)
