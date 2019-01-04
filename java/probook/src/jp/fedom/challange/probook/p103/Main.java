package jp.fedom.challange.probook.p103;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;

class UF {
	int[] par;
	int[] rank;

	void init(int n) {
		par = new int[n];
		rank = new int[n];
		for (int i = 0; i < n; i++) {
			par[i] = i;
			rank[i] = 0;
		}
	}

	int find(int x) {
		if (par[x] == x) {
			return x;
		} else {
			return (par[x] = find(par[x]));
		}
	}

	void unite(int x, int y) {
		x = find(x);
		y = find(y);
		if (x == y) {
			return;
		}
		if (rank[x] < rank[y]) {
			par[x] = y;
		} else {
			par[y] = x;
			if (rank[x] == rank[y]) {
				rank[x]++;
			}
		}
	}

	boolean same(int x, int y) {
		return find(x) == find(y);
	}

}

class R {
	public R(int x, int y, int d) {
		this.x = x;
		this.y = y;
		this.d = d;
	}

	int x;
	int y;
	int d;
}

public class Main {

	public static int solve(R[] vs, int N, int M, int R) {

		int INF = Integer.MAX_VALUE / 2 - 1;
		int[] d = new int[N * M];
		for (int i = 0; i < N * M; i++) {
			d[i] = INF;
		}
		UF uf = new UF();
		uf.init(N * M);
		Queue<R> rs = new PriorityQueue<>(new Comparator<R>() {
			@Override
			public int compare(R o1, R o2) {
				return o2.d - o1.d;
			}
		});

		for (int i = 0; i < R; i++) {
			rs.add(vs[i]);
		}

		int res = 0;
		while (!rs.isEmpty()) {
			R r = rs.poll();
			if (!uf.same(r.x, r.y + N)) {
				uf.unite(r.x, r.y + N);
				res += r.d;
			}
		}

		return (N + M) * 10000 - res;
	}
}
