package jp.fedom.challange.probook.p42;

public class Main {

	public static int solve(int[] s, int t) {
		int count = 0;
		int[] coins = new int[] { 1, 5, 10, 50, 100, 500 };

		for (int i = 5; i >= 0; i--) {

			if (t == 0) {
				break;
			}
			if (s[i] > 0 && t >= s[i]) {
				int c = Math.min(t / coins[i], s[i]);
				t -= coins[i] * c;
				s[i] -= c;
				count += c;
			}
		}

		return count;
	}

}
