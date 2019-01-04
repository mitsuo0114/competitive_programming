package jp.fedom.challange.yuki.l2.q360;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] input = new String[1];
		int i = 0;
		while (sc.hasNext()) {
			input[i] = sc.nextLine();
			i++;
		}
		String[] d = input[0].split(" ");
		int[] dl = new int[d.length];
		for (i = 0; i < d.length; i++) {
			dl[i] = Integer.valueOf(d[i]);
		}

		System.out.println(solve(dl));

		sc.close();
	}

	public static String solve(int[] d) {
		List<Integer> t = new ArrayList<>();
		for (int dd : d) {
			t.add(dd);
		}
		List<List<Integer>> candidate = getPermulation(t);
		// System.out.println(candidate.size());

		for (List<Integer> c : candidate) {
			if (isMatch(toArr(c))) {
				return "YES";
			}
		}

		return "NO";
	}

	private static int[] toArr(List<Integer> c) {
		int[] r = new int[c.size()];
		for (int i = 0; i < c.size(); i++) {
			r[i] = c.get(i);
		}
		return r;
	}

	public static List<List<Integer>> getPermulation(List<Integer> d) {
		int LL = d.size();
		List<List<Integer>> ret = new ArrayList<List<Integer>>();
		if (LL == 1) {
			ret.add(d);
		} else {
			for (int i = 0; i < LL; i++) {
				List<Integer> r = new ArrayList<>(d);
				int keep = r.remove(i);
				List<List<Integer>> rr = getPermulation(r);

				for (int k = 0; k < rr.size(); k++) {
					rr.get(k).add(keep);
				}
				ret.addAll(rr);
			}

		}
		return ret;
	}

	private static boolean isMatch(int[] c) {
		for (int i = 0; i < c.length - 2; i++) {
			int a0 = i;
			int a1 = i + 1;
			int a2 = i + 2;
			if (c[a0] == c[a1] || c[a1] == c[a2] || c[a2] == c[a0]) {
				return false;
			}
			if (c[a0] > c[a2]) {
				return false;
			}
			if ((c[a0] < c[a1] && c[a1] < c[a2]) || (c[a2] < c[a1] && c[a1] < c[a0])) {
				return false;
			}

		}
		return true;
	}
}
