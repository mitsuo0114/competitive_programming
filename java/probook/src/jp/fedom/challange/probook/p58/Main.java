package jp.fedom.challange.probook.p58;


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

	public static int solve2(Item[] items, int n, int W) {
		dp = new int[n + 1][];
		for (int i = 0; i < dp.length; i++) {
			dp[i] = new int[W + 1];
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j <= W; j++) {
				if (j < items[i].w) {
					dp[i + 1][j] = dp[i][j];
				} else {
					dp[i + 1][j] = Math.max(dp[i][j], dp[i + 1][j - items[i].w] + items[i].v);
				}
			}
		}
		return dp[n][W];
	}

	public static int solve1(Item[] items, int n, int W) {
		dp = new int[n + 1][];
		for (int i = 0; i < dp.length; i++) {
			dp[i] = new int[W + 1];
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j <= W; j++) {
				for (int k = 0; k * items[i].w <= j; k++) {
					System.out.println(i + "/" + j + "/" + k + "/" + k * items[i].w);
					dp[i + 1][j] = Math.max(dp[i + 1][j], dp[i][j - k * items[i].w] + k * items[i].v);
				}
			}
		}
		return dp[n][W];
	}
	//
	// // i番目までの品物から重さの総和がj以下となるときの最大値
	// public static int dfs(Item[] items, int i, int j){
	//
	// // i番目までに重さj以下の荷物がない
	// if(findMin(Arrays.copyOfRange(items, 0, i), j) == -1){
	// return dfs(items, i + 1, j);
	// }
	//
	//
	//
	// }
	//
	// private static int findMin(Item[] items, int j) {
	// for(int i = 0; i < items.length; i++){
	// if(items[i].w <= j){
	// return 1;
	// }
	// }
	// return -1;
	// }
}
