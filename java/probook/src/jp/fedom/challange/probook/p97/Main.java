package jp.fedom.challange.probook.p97;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;

class P {
	public P(int i, int j) {
		d = i;
		n = j;
	}

	int d;
	int n;
}

public class Main {

	public static int solve(int N, int[][] w, char s, char e) {
		int[] d = new int[N];
		int INF = Integer.MAX_VALUE - 1000;
		Queue<P> priQue = new PriorityQueue<>(new Comparator<P>() {
			@Override
			public int compare(P o1, P o2) {
				if (o1.d == o2.d) {
					if (o1.n == o2.n) {
						return 0;
					} else {
						return o1.n < o2.n ? -1 : 1;
					}
				} else {
					return o1.d < o2.d ? -1 : 1;
				}
			}
		});

		for (int i = 0; i < N; i++) {
			d[i] = INF;
		}

		d[s - 'A'] = 0;
		priQue.add(new P(0, s - 'A'));

		while (!priQue.isEmpty()) {
			P p = priQue.poll();
			if (d[p.n] < p.d) {
				continue;
			}

			System.out.println("update --");
			for (int i = 0; i < N; i++) {
				if (w[p.n][i] == 0) {
					continue;
				}
				if (d[p.n] + w[p.n][i] < d[i]) {
					d[i] = d[p.n] + w[i][p.n];
					priQue.add(new P(d[i], i));
				}
				System.out.println(Character.toString((char) (i + 'A')) + " = " + d[i]);
			}
			System.out.println("--");
		}
		return d[e - 'A'];
	}

}
