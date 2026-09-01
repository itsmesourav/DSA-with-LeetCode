import java.util.*;

class Solution {
    public int minMoves(String[] classroom, int energy) {
        int m = classroom.length, n = classroom[0].length();
        int sr = 0, sc = 0, k = 0;

        int[][] id = new int[m][n];
        for (int[] row : id) Arrays.fill(row, -1);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char ch = classroom[i].charAt(j);

                if (ch == 'S') {
                    sr = i;
                    sc = j;
                } else if (ch == 'L') {
                    id[i][j] = k++;
                }
            }
        }

        int target = (1 << k) - 1;
        if (k == 0) return 0;

        // best[r][c][mask] = maximum energy with which we reached this state
        int[][][] best = new int[m][n][1 << k];
        for (int[][] a : best)
            for (int[] b : a)
                Arrays.fill(b, -1);

        // State: r, c, energy, mask
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{sr, sc, energy, 0});
        best[sr][sc][0] = energy;

        int moves = 0;
        int[] dr = {1, -1, 0, 0};
        int[] dc = {0, 0, 1, -1};

        while (!q.isEmpty()) {
            int size = q.size();

            while (size-- > 0) {
                int[] cur = q.poll();
                int r = cur[0], c = cur[1];
                int e = cur[2], mask = cur[3];

                if (mask == target) return moves;

                if (e == 0) continue;

                for (int d = 0; d < 4; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];

                    if (nr < 0 || nr >= m || nc < 0 || nc >= n)
                        continue;

                    char ch = classroom[nr].charAt(nc);
                    if (ch == 'X') continue;

                    int ne = e - 1;
                    int nmask = mask;

                    if (ch == 'L') {
                        nmask |= 1 << id[nr][nc];
                    }

                    if (ch == 'R') {
                        ne = energy;
                    }

                    // If we've already reached this position/mask
                    // with more energy, this state is useless.
                    if (best[nr][nc][nmask] >= ne)
                        continue;

                    best[nr][nc][nmask] = ne;
                    q.offer(new int[]{nr, nc, ne, nmask});
                }
            }

            moves++;
        }

        return -1;
    }
}