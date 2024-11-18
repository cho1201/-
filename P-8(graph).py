# Vertex 입력 받기
vtx = []
print("0 입력 시 vertex 입력 받기 종료")
while True:
    i = input("vertex: ")
    if i == '0':
        break
    vtx.append(i)

# 그래프 입력 받기
def input_graph():
    graph = {}  # 인접 리스트 방식의 그래프
    print("Edge 입력 (예: A-B). 종료하려면 0 입력.")
    while True:
        edge = input("Edge: ")
        if edge == "0":  # 종료 조건
            break
        try:
            u, v = edge.split("-")  # 입력 형식: "A-B"
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)  # 무향 그래프
        except ValueError:
            print("잘못된 입력입니다. 'A-B' 형식으로 입력하세요.")
    return graph

# 깊이 우선 탐색 (DFS)
def DFS(graph, v, visited):
    if v not in visited:  # v가 방문되지 않았으면
        visited.add(v)  # v를 방문했다고 표시
        print(v, end='-')  # v를 출력
        for neighbor in sorted(graph.get(v, [])):  # 정점의 인접 리스트 탐색 (정렬)
            if neighbor not in visited:
                DFS(graph, neighbor, visited)

# 너비 우선 탐색 (BFS)
def BFS(graph, start):
    visited = set()  # 방문한 정점을 기록
    queue = [start]  # 출발 정점을 A로 고정
    while queue:
        v = queue.pop(0)  # 큐에서 정점 제거
        if v not in visited:
            visited.add(v)  # 방문 기록
            print(v, end='-')  # 정점 출력
            for neighbor in sorted(graph.get(v, [])):  # 정점의 인접 리스트 탐색 (정렬)
                if neighbor not in visited:
                    queue.append(neighbor)  # 큐에 추가

# 연결 성분 검사
def find_connected_components(graph):
    visited = set()
    components = []

    def bfs(v):
        queue = [v]
        component = []
        while queue:
            curr = queue.pop(0)
            if curr not in visited:
                visited.add(curr)
                component.append(curr)
                for neighbor in sorted(graph.get(curr, [])):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return component

    for vertex in graph:
        if vertex not in visited:
            components.append(bfs(vertex))
    return components

# 신장 트리 (DFS 기반)
def spanning_tree_DFS(graph, start):
    visited = set()
    edges = []

    def dfs(v):
        visited.add(v)
        for neighbor in sorted(graph.get(v, [])):
            if neighbor not in visited:
                edges.append((v, neighbor))
                dfs(neighbor)

    dfs(start)
    return edges

# 메뉴 시스템
def menu(graph):
    while True:
        print("\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
        print("a = adjacent vertex 리스트")
        print("b = BFS 탐색")
        print("c = Connected Components")
        print("d = DFS 탐색")
        print("e = Spanning Tree")
        print("q = 종료")
        print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
        choice = input("메뉴를 선택하시오: ").lower()

        if choice == "a":
            print("\n입력된 그래프의 인접 리스트:")
            for key, value in graph.items():
                print(f"{key}: {value}")

        elif choice == "b":
            print("\nBFS 탐색 결과 (출발 정점 A):", end=" ")
            BFS(graph, 'A')
            print()

        elif choice == "c":
            print("\nConnected Components (BFS):")
            connected_components = find_connected_components(graph)
            for idx, component in enumerate(connected_components):
                print(f"Component {idx + 1}:", " - ".join(component))

        elif choice == "d":
            print("\nDFS 탐색 결과 (출발 정점 A):", end=" ")
            DFS(graph, 'A', set())
            print()

        elif choice == "e":
            print("\nSpanning Tree (출발 정점 A):")
            spanning_tree_edges = spanning_tree_DFS(graph, 'A')
            for edge in spanning_tree_edges:
                print(f"Edge: {edge[0]} - {edge[1]}")

        elif choice == "q":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

# 그래프 입력 및 메뉴 실행
graph = input_graph()
menu(graph)
