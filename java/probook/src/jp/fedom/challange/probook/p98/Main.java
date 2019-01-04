package jp.fedom.challange.probook.p98;

public class Main {

	public static int solve(int N, int[][] w, char s, char e) {
		int[][] d = new int[N][];
		int INF = Integer.MAX_VALUE / 2 - 1;
		for (int i = 0; i < N; i++) {
			d[i] = new int[N];
			for (int j = 0; j < N; j++) {
				if (i == j) {
					d[i][j] = 0;
				} else if (w[i][j] == 0) {
					d[i][j] = INF;
				} else {
					d[i][j] = w[i][j];
				}
			}
		}

		for (int k = 0; k < N; k++) {
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					d[i][j] = Math.min(d[i][j], d[i][k] + d[k][j]);
				}
			}
		}

		return d[s - 'A'][e - 'A'];
	}

}
