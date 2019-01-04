package jp.fedom.challange.probook.p53;

class Item {
	public Item(int w, int v) {
		this.w = w;
		this.v = v;
	}

	public int w;
	public int v;
}

public class Main {

	static int[][] dp;

	public static int solve(Item[] items, int n, int W) {
		int ans = 0;
		dp = new int[n][];

		for (int i = 0; i < n; i++) {
			dp[i] = new int[W + 1];
			for (int j = 0; j < W + 1; j++) {
				dp[i][j] = -1;
			}
		}

		ans = dfs(items, 0, W);
		return ans;
	}

	public static int dfs(Item[] items, int k, int W) {

		if (k >= items.length) {
			return 0;
		}

		if (dp[k][W] != -1) {
			return dp[k][W];
		}

		if (items[k].w > W) {
			// これは入れられない
			dp[k][W] = dfs(items, k + 1, W);
			return dp[k][W];

		} else {
			dp[k][W] = Math.max(
					dfs(items, k + 1, W),
					dfs(items, k + 1, W - items[k].w) + items[k].v);
			return dp[k][W];
		}

	}

}
