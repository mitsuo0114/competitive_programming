package jp.fedom.challange.yuki.l1.q345;

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		List<String> input = new ArrayList<>();
		while (sc.hasNext()) {
			input.add(sc.nextLine());
		}

		System.out.println(solve(input));

		sc.close();
	}

	public static int solve(List<String> in) {
		String s = in.get(0);
		int INF = Integer.MAX_VALUE;
		int ans = INF;
		Queue<Integer> cp = new PriorityQueue<>();
		List<Integer> wp = new ArrayList<>();
		char[] ll = s.toCharArray();
		for (int i = 0; i < ll.length; i++) {
			if (ll[i] == 'c') {
				cp.add(i);
			} else if (ll[i] == 'w') {
				wp.add(i);
			}
		}

		while (!cp.isEmpty()) {
			int cplace = cp.poll();
			for (int i = 0; i < wp.size() - 1; i++) {
				int w1place = wp.get(i);
				if (w1place < cplace) {
					continue;
				} else {
					int w2place = wp.get(i + 1);
					ans = Math.min(ans, w2place - cplace + 1);
				}
			}
		}

		if (ans == INF) {
			return -1;
		} else {
			return ans;
		}
	}

}
