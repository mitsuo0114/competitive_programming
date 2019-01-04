package jp.fedom.challange.probook.p43;

public class Main {

	public static int solve(int[] s, int[] e) {
		int count = 0;
		int now = 0;

		while (true) {
			int mini = -1;
			int minE = Integer.MAX_VALUE;

			for (int i = 0; i < e.length; i++) {
				if (s[i] > now) {
					if (minE > e[i]) {
						minE = e[i];
						mini = i;
					}
				}
			}

			if (mini == -1) {
				break;
			} else {
				System.out.println("select " + (mini + 1));
				count++;
				now = minE;
			}
		}

		return count;
	}

}
