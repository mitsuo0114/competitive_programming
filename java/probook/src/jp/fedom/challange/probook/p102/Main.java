package jp.fedom.challange.probook.p102;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;

class V {
	public V(int i, int j, int k) {
		to = i;
		from = j;
		cost = k;
	}

	int to;
	int from;
	int cost;
}

class P {
	public P(int i, int j) {
		d = i;
		n = j;
	}

	int d;
	int n;
}

public class Main {

	public static int solve(V[] vs, int N, int g) {
		int[] d = new int[N];
		int[] s = new int[N];
		int INF = 10000;
		Queue<P> ps = new PriorityQueue<>(new Comparator<P>() {
			@Override
			public int compare(P o1, P o2) {
				if (o1.d == o2.d) {
					return 0;
				} else {
					return o1.d < o2.d ? -1 : 1;
				}
			}
		});

		for (int i = 0; i < N; i++) {
			d[i] = INF;
			s[i] = INF;
		}

		d[0] = 0;
		ps.add(new P(0, 0));

		while (true) {
			if (ps.isEmpty()) {
				break;
			}
			// System.out.println(ps.size());
			P p = ps.poll();
			if (s[p.n] < p.d) {
				continue;
			}

			for (V v : vs) {
				int from = v.from - 1;
				int to = v.to - 1;
				if (from != p.n) {
					continue;
				}
				// この時点で最短距離候補
				int d2 = p.d + v.cost;

				// if文を通る = d[to]が入る = これまで最短だったが置き換えられたもの＝2位
				// if文を通らない = d[to]が既に大きい = これが2番目である可能性
				if (d[to] > d2) {
					d2 = d[to];
					d[to] = p.d + v.cost;
					ps.add(new P(d[to], to));
				}
				// d2は2番目候補
				// 2番目の置き換え条件は、これまでの2番目より小さく、1番目よりは大きい

				if (d2 < s[to] && d[to] < d2) {
					s[to] = d2;
					ps.add(new P(s[to], to));
				}

			}
		}

		return s[g - 1];
	}
}
