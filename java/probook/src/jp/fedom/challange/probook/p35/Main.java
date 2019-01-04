package jp.fedom.challange.probook.p35;

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

		int n = s.length;
		int m = s[0].length();
		char[][] ff = new char[n][];
		for (int i = 0; i < n; i++) {
			ff[i] = new char[m];
			for (int j = 0; j < m; j++) {
				ff[i][j] = s[i].charAt(j);
			}
		}
		int count = 0;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (ff[i][j] == 'W') {
					destoryPond(i, j, ff);
					++count;
				}

			}
		}

		return count;
	}

	private static void destoryPond(int i, int j, char[][] ff) {
		ArrayDeque<P> ad = new ArrayDeque<>();
		int n = ff.length;
		int m = ff[0].length;

		ad.addFirst(new P(i, j));
		ff[i][j] = '.';

		while (!ad.isEmpty()) {
			P p = ad.poll();
			ff[p.i][p.j] = '.';
			for (int di = -1; di <= 1; di++) {
				for (int dj = -1; dj <= 1; dj++) {
					if (di == 0 && dj == 0) {
						continue;
					}
					int ni = p.i + di;
					int nj = p.j + dj;
					if (ni >= 0 && ni < n && nj >= 0 && nj < m) {
						if (ff[ni][nj] == 'W') {
							ad.addFirst(new P(ni, nj));
							ff[ni][nj] = '.';
						}
					}
				}
			}
		}
	}

}
