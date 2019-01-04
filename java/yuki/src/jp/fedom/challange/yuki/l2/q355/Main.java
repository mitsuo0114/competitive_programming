package jp.fedom.challange.yuki.l2.q355;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
	public static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		new Main().solve();
	}

	public void solve() {
		List<int[]> candidate = new ArrayList<int[]>();
		for (int j = 0; j < 10000; j++) {
			int c1 = j % 10;
			int c2 = j / 10 % 10;
			int c3 = j / 100 % 10;
			int c4 = j / 1000 % 10;
			if (c1 == c2 || c1 == c3 || c1 == c3 || c1 == c4 || c2 == c3 || c2 == c4 || c3 == c4) {
				continue;
			} else {
				int[] r = new int[4];
				r[0] = c1;
				r[1] = c2;
				r[2] = c3;
				r[3] = c4;
				candidate.add(r);
			}
		}
		while (candidate.size() > 1) {
			int[] c = candidate.get(0);
			send(c);
			String input = get();
			if (input.equals("4 0")) {
				return;
			} else {
				candidate.remove(0);
				List<Integer> rm = new ArrayList<>();
				for (int i = 0; i < candidate.size(); i++) {
					if (isContradiction(candidate.get(i), input, c)) {
						rm.add(i);
						candidate.remove(i);
						i--;
					}
				}
			}
		}
		send(candidate.get(0));

	}

	private void send(int[] c) {
		send(c[0] + " " + c[1] + " " + c[2] + " " + c[3]);
	}

	private boolean isContradiction(int[] can, String input, int[] ans) {

		int m1 = 0;
		int m2 = 0;

		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (ans[i] == can[j]) {
					m2++;
				}
			}
		}
		for (int i = 0; i < 4; i++) {
			if (ans[i] == can[i]) {
				m1++;
				m2--;
			}
		}
		return !input.equals(m1 + " " + m2);
	}

	protected void send(String s) {
		System.out.println(s);
		System.out.flush();

	}

	protected String get() {
		return sc.nextLine();
	}

}
