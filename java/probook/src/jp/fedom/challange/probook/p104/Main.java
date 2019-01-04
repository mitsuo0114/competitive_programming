package jp.fedom.challange.probook.p104;

import java.util.List;

public class Main {

	private static final int INF = Integer.MAX_VALUE;

	public static int solve(int N, int ML, int MD, List<int[]> good, List<int[]> bad) {
		int[] d = new int[N];
		for (int i = 0; i < d.length; i++) {
			d[i] = INF;
		}
		d[0] = 0;

		for (int i = 0; i < d.length; i++) {
			System.out.print((d[i] == INF ? "-" : d[i]) + " ");
		}
		System.out.println();

		for (int k = 0; k < N; k++) {
			
			for (int i = 0; i < N; i++) {
				if (i + 1 < N && d[i + 1] != INF) {
					d[i] = Math.min(d[i], d[i + 1] + 0);
				}
			}
			
			for (int[] g : good) {
				int AL = g[0] - 1;
				int BL = g[1] - 1;
				int DL = g[2];
				if (d[AL] != INF) {
					d[BL] = Math.min(d[BL], d[AL] + DL);
				}
			}

			for (int[] b : bad) {
				int AD = b[0] - 1;
				int BD = b[1] - 1;
				int DD = b[2];
				if (d[BD] != INF) {
					d[AD] = Math.min(d[AD], d[BD] - DD);
				}
			}
			for (int i = 0; i < d.length; i++) {
				System.out.print((d[i] == INF ? "-" : d[i]) + " ");
			}
			System.out.println();

		}
		if (d[0] < 0) {
			return -1;
		} else if (d[N - 1] == INF) {
			return -2;
		} else {
			return d[N - 1];
		}
	}
}
