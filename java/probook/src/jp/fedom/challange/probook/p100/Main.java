package jp.fedom.challange.probook.p100;

public class Main {

	public static int solve(int N, int[][] w) {
		int mincost[] = new int[N];
		int INF = Integer.MAX_VALUE / 2 - 1;
		boolean used[] = new boolean[N];
		for (int i = 0; i < used.length; i++) {
			used[i] = false;
			mincost[i] = INF;
		}

		mincost[6] = 0;
		int res = 0;

		while (true) {
			int v = -1;
			for (int u = 0; u < N; u++) {
				if (used[u] == false && (v == -1 || mincost[u] < mincost[v])) {
					v = u;
				}
			}

			if (v == -1) {
				break;
			}

			used[v] = true;
			res += mincost[v];

			for (int u = 0; u < N; u++) {
				if (w[v][u] != 0) {
					mincost[u] = Math.min(mincost[u], w[v][u]);
				}
			}
		}

		return res;
	}

}
