package jp.fedom.challange.probook.p75;

import java.util.PriorityQueue;
import java.util.Queue;

public class Main {

	public static int solve(int[] L, int N) {
		Queue<Integer> que = new PriorityQueue<Integer>();

		int ans = 0;

		for (int i = 0; i < L.length; i++) {
			que.add(L[i]);
		}
		while (que.size() > 1) {
			int n1 = que.poll();
			int n2 = que.poll();
			ans += n1 + n2;
			que.add(n1 + n2);
		}
		return ans;
	}

}
