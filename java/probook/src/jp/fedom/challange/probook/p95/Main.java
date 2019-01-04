package jp.fedom.challange.probook.p95;

public class Main {

	public static int solve(int N, int[][] w, char s, char e) {
		int[] d = new int[N];
		int INF = Integer.MAX_VALUE - 1000;
		for (int i = 0; i < N; i++) {
			d[i] = INF;
		}

		d[s - 'A'] = 0;

		while (true) {
			boolean update = false;
			for (int i = 0; i < N; i++) {
				System.out.println("update --");
				for (int j = 0; j < N; j++) {
					if (w[i][j] == 0) {
						continue;
					}
					if (d[i] != INF && d[j] > d[i] + w[i][j]) {
						d[j] = d[i] + w[i][j];
						System.out.println(Character.toString((char) (j + 'A')) + " = " + d[j]);
						update = true;
					}
				}
				System.out.println("--");
			}
			if (update == false) {
				break;
			}
		}
		return d[e - 'A'];
	}

}
