package jp.fedom.challange.probook.p96;

public class Main {

	public static int solve(int N, int[][] w, char s, char e) {
		int[] d = new int[N];
		boolean[] f = new boolean[N];
		int INF = Integer.MAX_VALUE - 1000;
		for (int i = 0; i < N; i++) {
			d[i] = INF;
			f[i] = false;
		}

		d[s - 'A'] = 0;

		while (true) {
			int v = -1;

			for (int i = 0; i < N; i++) {
				if (f[i] == false && (v == -1 || d[i] < d[v])) {
					v = i;
				}
			}
			if (v == -1) {
				break;
			}
			f[v] = true;

			System.out.println("update --");
			for (int i = 0; i < N; i++) {
				if (w[i][v] == 0 || f[i] == true) {
					continue;
				}
				d[i] = Math.min(d[i], d[v] + w[i][v]);
				System.out.println(Character.toString((char) (i + 'A')) + " = " + d[i]);
			}
			System.out.println("--");
		}
		return d[e - 'A'];
	}

}
