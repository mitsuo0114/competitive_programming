package jp.fedom.challange.probook.p37;

import java.util.ArrayDeque;

class P {

	int i;
	int j;

	public P(int i, int j) {
		this.i = i;
		this.j = j;
	}

}

public class Main {

	public static int solve(String[] s) {

		int INF = Integer.MAX_VALUE;
		int n = s.length;
		int m = s[0].length();
		char[][] ff = new char[n][];
		int[][] d = new int[n][];
		P sp = null;
		P gp = null;

		for (int i = 0; i < n; i++) {
			ff[i] = new char[m];
			d[i] = new int[m];

			for (int j = 0; j < m; j++) {
				ff[i][j] = s[i].charAt(j);
				d[i][j] = INF;

				if (ff[i][j] == 'S') {
					sp = new P(i, j);
				}
				if (ff[i][j] == 'G') {
					gp = new P(i, j);
				}
			}
		}

		ArrayDeque<P> ad = new ArrayDeque<>();

		ad.addFirst(sp);
		d[sp.i][sp.j] = 0;

		int[] di = new int[] { -1, 0, 0, 1 };
		int[] dj = new int[] { 0, -1, 1, 0 };

		while (!ad.isEmpty()) {
			P p = ad.poll();
			for (int k = 0; k < 4; k++) {
				int ni = p.i + di[k];
				int nj = p.j + dj[k];
				if (ni >= 0 && ni < n && nj >= 0 && nj < m) {
					if ((ff[ni][nj] == '.' || ff[ni][nj] == 'G') && d[ni][nj] == INF) {
						ad.addFirst(new P(ni, nj));
						d[ni][nj] = d[p.i][p.j] + 1;
					}
				}
			}
		}
		return d[gp.i][gp.j];
	}

}
