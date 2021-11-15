def solution(tickets):
    answer = []
    graph = {}
    for ticket in tickets:
        graph[ticket[0]] = graph.get(ticket[0], []) + [ticket[1]]
    for k in graph:
        graph[k].sort(reverse=True) # 스택이므로 내림차순으로 정렬해 알파벳순서대로 꺼냄

    lst = ["ICN"]
    while lst:
        cur = lst[-1] # 출발지
        if cur in graph and graph[cur]: # 도착지가 존재
            lst.append(graph[cur].pop())
        else:   # 도착지가 존재하지 않는 경우
            answer.append(lst.pop())

    return answer[::-1]

print(solution([["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]))
# print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]))