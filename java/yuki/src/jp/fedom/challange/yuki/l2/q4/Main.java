package jp.fedom.challange.yuki.l2.q4;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
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

	static int[] Ws;
	static boolean[][] dp;

	public static String solve(List<String> in) {
		int N = Integer.valueOf(in.get(0));
		String[] W = in.get(1).split(" ");

		boolean res = false;

		Ws = new int[N];
		int total = 0;
		for (int i = 0; i < N; i++) {
			Ws[i] = Integer.valueOf(W[i]);
			total += Ws[i];
		}
		Arrays.sort(Ws);

		if (total % 2 == 1) {
			res = false;
		} else {
			res = dfs(N, Ws, total / 2);
		}

		return res ? "possible" : "impossible";
	}

	private static boolean dfs(int N, int[] a, int K) {
		dp = new boolean[N + 1][];
		for (int i = 0; i < dp.length; i++) {
			dp[i] = new boolean[K + 1];
		}
		dp[0][0] = true;

		for (int i = 0; i < N; i++) {
			for (int j = 0; j <= K; j++) {
				dp[i + 1][j] |= dp[i][j];
				if (0 <= j - a[i]) {
					dp[i + 1][j] |= dp[i][j - a[i]];
				}
			}
		}
		return dp[N][K];
	}
}
