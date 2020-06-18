class Solution {
  public void wallsAndGates(int [][] rooms) {
    for (int i=0; i<rooms.length; i++) {
      for (int j=0; j<rooms[i].length; j++) {
        dfs(i, j, 0, rooms);
      }
    }
  }

  public void dfs(int i, int j, int count, int [][] rooms) {
    // sanity check for outta bounds and worst distannce
    if (i < 0 || i >= rooms.length || j < 0 || j >= rooms[i].length || rooms[i][j] < count) {
      return;
    }
    dfs(i+1, j, count+1, rooms);
    dfs(i-1, j, count+1, rooms);
    dfs(i, j+1, count+1, rooms);
    dfs(i, j-1, count+1, rooms);
  }
}
