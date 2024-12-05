import queue

comparisons = 0  # 비교 횟수
moves = 0  # 데이터 이동 횟수

# printStep 함수
def printStep(arr, val):
    print("  Step %2d = " % val, end='')
    print(arr)

# Selection Sort
def selection_sort(A):
    n = len(A)
    global comparisons
    global moves
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            comparisons += 1  # 비교
            if A[j] < A[least]:
                least = j
        if least != i:
            A[i], A[least] = A[least], A[i]
            moves += 2  # 2번의 데이터 이동 (A[i], A[least] 교환)
        printStep(A, i + 1)

# Insertion Sort
def insertion_sort(A):
    n = len(A)
    global comparisons
    global moves
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            comparisons += 1  # 비교
            A[j + 1] = A[j]
            moves += 1  # 데이터 이동
            j -= 1
        if j >= 0:  # 마지막 비교
            comparisons += 1
        A[j + 1] = key
        moves += 1  # key 값 이동
        printStep(A, i)

# Bubble Sort
def bubble_sort(A):
    n = len(A)
    global comparisons
    global moves
    for i in range(n - 1, 0, -1):
        bChanged = False
        for j in range(i):
            comparisons += 1  # 비교
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                moves += 2  # 2번의 데이터 이동 (A[j], A[j+1] 교환)
                bChanged = True
        if not bChanged:
            break
        printStep(A, n - i)

# Heap Sort
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    local_comparisons = 0  # 비교 횟수
    local_moves = 0  # 데이터 이동 횟수

    if l < n and arr[i] < arr[l]:
        largest = l
        local_comparisons += 1
    if r < n and arr[largest] < arr[r]:
        largest = r
        local_comparisons += 1
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        local_moves += 2  # 2번의 데이터 이동 (arr[i], arr[largest] 교환)
        heapify(arr, n, largest)
    return local_comparisons, local_moves

def heapSort(arr):
    n = len(arr)
    global comparisons
    global moves
    for i in range(n // 2, -1, -1):
        c, m = heapify(arr, n, i)
        comparisons += c
        moves += m
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        moves += 2  # 2번의 데이터 이동 (arr[i], arr[0] 교환)
        c, m = heapify(arr, i, 0)
        comparisons += c
        moves += m

# Merge Sort
sorted = [0] * 100

def merge(A, left, mid, right):
    global sorted
    k = left
    i = left
    j = mid + 1
    local_comparisons = 0
    local_moves = 0
    while i <= mid and j <= right:
        local_comparisons += 1
        if A[i] <= A[j]:
            sorted[k] = A[i]
            local_moves += 1
            i, k = i + 1, k + 1
        else:
            sorted[k] = A[j]
            local_moves += 1
            j, k = j + 1, k + 1
    if i > mid:
        sorted[k:k + right - j + 1] = A[j:right + 1]
        local_moves += right - j + 1
    else:
        sorted[k:k + mid - i + 1] = A[i:mid + 1]
        local_moves += mid - i + 1
    A[left:right + 1] = sorted[left:right + 1]
    return local_comparisons, local_moves

def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        c1, m1 = merge_sort(A, left, mid)
        c2, m2 = merge_sort(A, mid + 1, right)
        merge_comparisons, merge_moves = merge(A, left, mid, right)
        return c1 + c2 + merge_comparisons, m1 + m2 + merge_moves
    return 0, 0

# Quick Sort
def partition(A, left, right):
    low = left + 1
    high = right
    pivot = A[left]
    local_comparisons = 0
    local_moves = 0
    while low < high:
        while low <= right and A[low] < pivot:
            low += 1
            local_comparisons += 1
        while high >= left and A[high] > pivot:
            high -= 1
            local_comparisons += 1
        if low < high:
            A[low], A[high] = A[high], A[low]
            local_moves += 2
    A[left], A[high] = A[high], A[left]
    local_moves += 2
    return high, local_comparisons, local_moves

def quick_sort(A, left, right):
    if left < right:
        q, c, m = partition(A, left, right)
        left_comparisons, left_moves = quick_sort(A, left, q - 1)
        right_comparisons, right_moves = quick_sort(A, q + 1, right)
        return c + left_comparisons + right_comparisons, m + left_moves + right_moves
    return 0, 0

# Radix Sort
BUCKETS = 10
DIGITS = 4

def radix_sort(A):
    global comparisons
    global moves
    queues = []
    for i in range(BUCKETS):
        queues.append(queue.Queue())
    n = len(A)
    factor = 1
    for d in range(DIGITS):
        for i in range(n):
            queues[(A[i] // factor) % BUCKETS].put(A[i])
            moves += 1  # 데이터 이동
        i = 0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[i] = queues[b].get()
                i += 1
                moves += 1  # 데이터 이동
        factor *= 10
        printStep(A, d + 1)

# Shell Sort
def sortGapInsertion(A, first, last, gap):
    global comparisons
    global moves
    for i in range(first + gap, last + 1, gap):
        key = A[i]
        j = i - gap
        while j >= first and key < A[j]:
            comparisons += 1  # 비교
            A[j + gap] = A[j]
            moves += 1  # 데이터 이동
            j = j - gap
        if j >= first:  # 마지막 비교
            comparisons += 1
        A[j + gap] = key
        moves += 1  # 데이터 이동
    return comparisons, moves

def shell_sort(A):
    n = len(A)
    global comparisons
    global moves
    gap = n // 2
    while gap > 0:
        if (gap % 2) == 0:
            gap += 1
        for i in range(gap):
            c, m = sortGapInsertion(A, i, n - 1, gap)
            comparisons += c
            moves += m
        gap = gap // 2

# Algorithm Menu
def SEL(A):
    global comparisons
    global moves
    print("Original  :", org)
    comparisons, moves = 0, 0
    selection_sort(data)
    print("Selection Sort: Comparisons = ", comparisons, ", Moves = ", moves)

def INS(A):
    global comparisons
    global moves
    print("Original  :", org)
    comparisons, moves = 0, 0
    insertion_sort(data)
    print("Insertion Sort: Comparisons = ", comparisons, ", Moves = ", moves)

def BUB(A):
    global comparisons
    global moves
    print("Original  :", org)
    comparisons, moves = 0, 0
    bubble_sort(data)
    print("Bubble Sort: Comparisons = ", comparisons, ", Moves = ", moves)

def HEA(A):
    global comparisons
    global moves
    print("Original  :", org)
    comparisons, moves = 0, 0
    heapSort(data)
    print("Heap Sort: Comparisons = ", comparisons, ", Moves = ", moves)

def MER(A):
    global comparisons
    global moves
    print("Original  :", org)
    comparisons, moves = merge_sort(data, 0, len(data) - 1)
    print("Merge Sort: Comparisons = ", comparisons, ", Moves = ", moves)

def QUI(A):
    global comparisons
    global moves
    print("Original  :", org)
    comparisons, moves = quick_sort(data, 0, len(data) - 1)
    print("Quick Sort: Comparisons = ", comparisons, ", Moves = ", moves)

def RAD(A):
    global comparisons
    global moves
    print("Original  :", org)
    comparisons, moves = 0, 0
    radix_sort(data)
    print("Radix Sort: Comparisons = ", comparisons, ", Moves = ", moves)

def SHE(A):
    global comparisons
    global moves
    print("Original  :", org)
    comparisons, moves = 0, 0
    shell_sort(data)
    print("Shell Sort: Comparisons = ", comparisons, ", Moves = ", moves)

def menu():
    global data
    global org
    while True:
        org_input = input("Enter the data to be sorted (comma separated): ").strip()
        try:
            org = list(map(int, org_input.split(',')))
            break
        except ValueError:
            print("Please enter valid integers separated by commas.")
    
    while True:
        print("\n----------------Target Sorting Algorithm List--------------")
        print("Selection(SEL), Insertion(INS), Bubble(BUB), Shell(SHE),")
        print("Heap(HEA), Merge(MER), Quick(QUI), Radix(RAD)")
        print("q = quit")
        print("-----------------------------------------------------------")
        a = input("Select sorting algorithm : ").upper()
        if a == 'Q':
            print("Exiting the program.")
            break
        
        data = org.copy()
        if a == "SEL": SEL(data)
        elif a == "INS": INS(data)
        elif a == "BUB": BUB(data)
        elif a == "SHE": SHE(data)
        elif a == "HEA": HEA(data)
        elif a == "MER": MER(data)
        elif a == "QUI": QUI(data)
        elif a == "RAD": RAD(data)
        else:
            print("Please select correct algorithm.")

menu()
