package jp.fedom.challange.probook.p62;

public class Main {

	static boolean[][] dp;

	public static boolean solve2(int n, int[] a, int[] m, int K) {
		return false;
	}

	public static boolean solve1(int n, int[] a, int[] m, int K) {
		dp = new boolean[n + 1][];
		for (int i = 0; i < dp.length; i++) {
			dp[i] = new boolean[K + 1];
		}
		dp[0][0] = true;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j <= K; j++) {
				for (int mi = 0; mi <= m[i]; mi++) {
					if (a[i] * mi <= j) {
						dp[i + 1][j] |= dp[i][j - (a[i] * mi)];
					}
				}

			}
		}
		return dp[n][K];
	}
}
