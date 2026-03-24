def floodFill(image, sr, sc, color):
    rows, cols = len(image), len(image[0])
    old = image[sr][sc]
    
    if old == color:
        return image
    
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != old:
            return
        image[r][c] = color
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    
    dfs(sr, sc)
    return image