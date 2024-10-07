# 코드 3.3: 배열로 구현된 리스트 클래스  (참고 파일: ch03/ArrayList.py)

class ArrayList:
    # 리스트의 데이터: 생성자에서 정의 및 초기화
    def __init__( self, capacity=100 ):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    # 리스트의 연산: 클래스의 메소드
    def isEmpty( self ):
       return self.size == 0

    def isFull( self ):
       return self.size == self.capacity

    def getEntry(self, pos) :
        if 0 <= pos < self.size :
            return self.array[pos]
        else : return None

    def insert( self, pos, e ) :
        if not self.isFull() and 0 <= pos <= self.size :
            for i in range(self.size, pos,-1) :
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1
        else : pass

    def delete( self, pos ) :
        if not self.isEmpty() and 0 <= pos < self.size :
            e = self.array[pos]
            for i in range(pos, self.size-1) :
                self.array[i] = self.array[i+1]
            self.size -= 1
            return e
        else : pass

    def __str__( self ) :
        return str(self.array[0:self.size])

#=========================================================
#   - 이 파일이 직접 실행될 때에는 다음 문장들을 실행함.
#   - 다른 파일에서 모듈로 불려지는 경우는 실행되지 않음.
#=========================================================
# 테스트 프로그램
if __name__ == "__main__":
    L = ArrayList(50)
    
    print("최초   ", L)
    L.insert(0, 10)
    L.insert(0, 20)
    L.insert(1, 30)
    L.insert(L.size, 40)
    L.insert(2, 50)
    print("삽입x5 ", L)
    L.delete(2)
    print("삭제(2)", L)
    L.delete(L.size-1)
    print("삭제(E)", L)
    L.delete(0)
    print("삭제(0)", L)













# 배열구조의 리스트를 이용한 라인 편집기 프로그램
list = ArrayList(1000)
while True :
    command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, m-빈도, q-종료 => ")

    if command == 'i' :
        pos = int( input("  입력행 번호: ") )
        str = input("  입력행 내용: ")
        list.insert(pos, str)

    elif command == 'd' :
        pos = int( input("  삭제행 번호: ") )
        list.delete(pos)

    elif command == 'r' :
        pos = int( input("  변경행 번호: ") )
        str = input("  변경행 내용: ");
        list.replace(pos, str)

    elif command == 'p' :
        print('Line Editor')
        for line in range (list.size) :
            print('[%2d] '%line, end='')
            print(list.getEntry(line))
        print()

    elif command == 'q' : exit()

    elif command == 'l' :
        # filename = input("  읽어들일 파일 이름: ")
        filename = 'test.txt'
        infile = open(filename , "r")
        lines = infile.readlines();
        for line in lines:
            list.insert(list.size, line.rstrip('\n'))
        infile.close()

    elif command == 's' :
        # filename = input("  저장할 파일 이름: ")
        filename = 'test.txt'
        outfile = open(filename , "w")
        len = list.size
        for i in range(len) :
            outfile.write(list.getEntry(i)+'\n')
        outfile.close()

    elif command == 'm':
       #입력된 문자열들의 단어들을 추출하고, 그 단어의 출현 빈도수를 출력하고, 'dict.txt'파일에 저장하는 함수
        str = input("  입력할 문자열: ")
        words = str.split()
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        filename = 'dict.txt'
        with open(filename, "w") as outfile:
            for word, count in word_count.items():
                outfile.write(f"{word}: {count}\n")
                
        filename = 'dict.txt'
        infile = open(filename , "r")
        lines = infile.readlines();
        for line in lines:
            list.insert(list.size, line.rstrip('\n'))
        infile.close()
        for line in range (list.size) :
            print(list.getEntry(line))


