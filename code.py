def catMouseGame(graph):
    memo = {}

    def dfs(m, c, turn):
        key = (m, c, turn)
        if key in memo:
            return memo[key]
        
        if m == 0:
            memo[key] = 1
            return 1
        if m == c:
            memo[key] = 2
            return 2
        
        if turn == 1:
            next_positions = [pos for pos in graph[c] if pos != 0]
            if not next_positions:
                memo[key] = 0
                return 0
        
        memo[key]