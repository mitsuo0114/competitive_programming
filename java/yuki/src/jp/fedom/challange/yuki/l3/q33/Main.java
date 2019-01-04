package jp.fedom.challange.yuki.l3.q33;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
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

	public static int solve2(List<String> in) {
//		int N = Integer.valueOf(in.get(0).split(" ")[0]);
//		int D = Integer.valueOf(in.get(0).split(" ")[1]);
//		int T = Integer.valueOf(in.get(0).split(" ")[2]);
//		int[] X = new int[N];
//		String[] s = in.get(1).split(" ");
//		for (int i = 0; i < N; i++) {
//			X[i] = Integer.valueOf(s[i]);
//		}
//
//		long[][] min = new long[N][];
//		long[][] max = new long[N][];
//		for (int i = 0; i < N; i++) {
//			min[i] = new long[N];
//			max[i] = new long[N];
//		}
//		for (int i = 0; i < N; i++) {
//			for (int j = 0; j < N; j++) {
//				long d = Math.abs(X[i] - X[j]);
//				if (d % D == 0) {
//					min[i][j] = Math.max(X[i] - D * T, X[j] + D * T);
//					max[i][j] = Math.min(X[i] + D * T, X[j] - D * T);
//				}
//			}
//		}

		return 1; // f.bitCount();
	}

	public static int solve(List<String> in) {
		int N = Integer.valueOf(in.get(0).split(" ")[0]);
		int D = Integer.valueOf(in.get(0).split(" ")[1]);
		int T = Integer.valueOf(in.get(0).split(" ")[2]);
		String[] X = in.get(1).split(" ");

		BigInteger f = BigInteger.ZERO;
		for (String s : X) {
			int i = Integer.valueOf(s);
			f = f.setBit((int) (i + 10e4));
		}

		for (int i = 0; i < T; i++) {
			BigInteger l = f.shiftLeft(D);
			BigInteger r = f.shiftRight(D);

			f = f.or(l).or(r);
		}

		return f.bitCount();
	}
}
