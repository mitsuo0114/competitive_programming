package jp.fedom.challange.probook.p85;

class Info {
	public Info(int i, int j, int k) {
		type = i;
		x = j;
		y = k;
	}

	int type;
	int x;
	int y;

}

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

public class Main {

	public static int solve(Info[] I, int N) {

		int ans = 0;
		UnionFind uf = new UnionFind();
		uf.init(N * 3);

		for (int i = 0; i < I.length; i++) {
			int t = I[i].type;
			int x = I[i].x - 1;
			int y = I[i].y - 1;

			if ((t != 1 && t != 2) || x > N || y > N || x < 0 || y < 0) {
				ans++;
				continue;
			}
			
			if (t == 1) {
				if (uf.same(x, y + N) || uf.same(x, y + N * 2)) {
					ans++;
					continue;
				}

				uf.unite(x, y);
				uf.unite(x + N, y + N);
				uf.unite(x + N * 2, y + N * 2);
			} else {
				if (uf.same(x, y) || uf.same(x + N, y + N)|| uf.same(x + N * 2, y + N * 2)) {
					ans++;
					continue;
				}

				uf.unite(x, y + N);
				uf.unite(x + N, y + N * 2);
				uf.unite(x + N * 2, y);
			}

		}

		return ans;
	}

}
