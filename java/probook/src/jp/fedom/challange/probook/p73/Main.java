package jp.fedom.challange.probook.p73;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;

public class Main {

	public static int solve(int[] A, int[] B, int N, int L, int P) {
		Queue<Integer> stack = new PriorityQueue<>(A.length, new Comparator<Integer>() {
			@Override
			public int compare(Integer o1, Integer o2) {
				if (o1 == o2) {
					return 0;
				} else {
					return o2 < o1 ? -1 : 1;
				}
			}
		});

		int d = P;
		int ans = 0;
		while (d < L) {
			for (int i = 0; i < A.length; i++) {
				if (A[i] <= d) {
					stack.add(B[i]);
					A[i] = Integer.MAX_VALUE;
				}
			}
			if (stack.isEmpty()) {
				return -1;
			} else {
				d += stack.poll();
				ans++;
			}
		}

		return ans;
	}
}
