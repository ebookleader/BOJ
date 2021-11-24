# import sys
# from collections import deque
#
# def bfs(s):
#     global matrix
#     queue = deque()
#     queue.append([1, 0])    # 화면 이모티콘, 클립보드 이모티콘
#     matrix[1][0] = 1    # [화면 이모티콘][클립보드 이모티콘]
#     while queue:
#         mm, cc = queue.popleft()
#         # 화면의 이모티콘 모두 복사 후 클립보드에 저장
#         if matrix[mm][cc] == -1:
#             queue.append([mm, mm])
#             matrix[mm][mm] = matrix[mm][cc]
#         # 클립보드의 모든 이모티콘 화면에 붙여넣기
#         if cc > 0:
#             queue.append([mm+cc, cc, sec+1])
#         # 화면 이모티콘 한개 삭제
#         if mm > 0:
#             queue.append([mm-1, cc, sec+1])
# s = int(sys.stdin.readline().split())
# matrix = [[-1] * (s+1) for _ in range(s+1)]