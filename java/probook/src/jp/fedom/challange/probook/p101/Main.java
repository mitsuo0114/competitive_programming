package jp.fedom.challange.probook.p101;

import java.util.Comparator;
import java.util.PriorityQueue;

class UnionFind {
	int[] par;
	int[] rank;

	void init(int n) {
		par = new int[n + 1];
		rank = new int[n + 1];
		for (int i = 0; i <= n; i++) {
			par[i] = i;
			rank[i] = 0;
		}
	}

	int find(int x) {
		if (par[x] == x) {
			return x;
		} else {
			int p = find(par[x]);
			par[x] = p;
			return p;
		}
	}

	void unite(int x, int y) {
		x = find(x);
		y = find(y);

		if (x == y) {
			return;
		}
		par[x] = y;

	}

	boolean same(int x, int y) {
		return find(x) == find(y);
	}

}

class V {
	public V(int i, int j, int k) {
		from = i;
		to = j;
		cost = k;
	}

	int from;
	int to;
	int cost;
}

public class Main {

	public static int solve(int N, int[][] w) {

		PriorityQueue<V> pq = new PriorityQueue<>(new Comparator<V>() {
			public int compare(V o1, V o2) {
				if (o1.cost == o2.cost) {
					return 0;
				} else {
					return o1.cost < o2.cost ? -1 : 1;
				}
			}
		});
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (w[i][j] != 0) {
					pq.add(new V(i, j, w[i][j]));
				}
			}
		}

		UnionFind uf = new UnionFind();
		uf.init(N);
		int res = 0;
		while (!pq.isEmpty()) {
			V v = pq.poll();
			if (!uf.same(v.to, v.from)) {
				uf.unite(v.to, v.from);
				res += v.cost;
			}
		}

		return res;
	}

}
