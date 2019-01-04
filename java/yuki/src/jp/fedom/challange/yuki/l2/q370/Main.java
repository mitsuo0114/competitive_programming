package jp.fedom.challange.yuki.l2.q370;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[] d = new int[M];
		for (int i = 0; i < M; i++) {
			d[i] = sc.nextInt();
		}
		sc.close();
		System.out.println(solve(N, M, d));
	}

	public static int solve(int N, int M, int[] c) {
		List<Integer> posN = new ArrayList<>();
		List<Integer> negN = new ArrayList<>();
		for (int i : c) {
			if (i < 0) {
				negN.add(i * -1);
			} else {
				posN.add(i);
			}
		}

		Collections.sort(posN);
		Collections.sort(negN);

		int min = Integer.MAX_VALUE;
		for (int pN = 0; pN <= N; pN++) {
			int nN = N - pN;
			if (pN <= posN.size() && nN <= negN.size()) {
				int pd = pN - 1 < 0 ? 0 : posN.get(pN - 1);
				int nd = nN - 1 < 0 ? 0 : negN.get(nN - 1);
				int d = Math.min(pd * 2 + nd, pd + nd * 2);
				min = Math.min(d, min);
			}
		}

		return min;
	}
}
