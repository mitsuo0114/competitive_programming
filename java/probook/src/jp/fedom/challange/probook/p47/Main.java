package jp.fedom.challange.probook.p47;

public class Main {

	public static int solve(int[] X, int r) {
		int i = 0, ans = 0;
		int N = X.length;

		while (i < N) {
			int s = X[i];
			i++;
			while (i < N && X[i] <= s + r) {
				i++;
			}
			int p = X[i - 1];
			while (i < N && X[i] <= p + r) {
				i++;
			}

			ans++;
		}

		return ans;
	}

}
