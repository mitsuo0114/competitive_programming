package jp.fedom.challange.yuki.l2.q366;

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

	public static int solve(List<String> in) {
		int N = Integer.valueOf(in.get(0).split(" ")[0]);
		int K = Integer.valueOf(in.get(0).split(" ")[1]);
		int[][] a = new int[N][];
		int count = 0;

		for (int i = 0; i < N; i++) {
			a[i] = new int[N];
		}

		for (int i = 0; i < N; i++) {
			int x = i % K;
			int y = i / K;
			a[x][y] = Integer.valueOf(in.get(1).split(" ")[i]);
		}
		
		for (int i = 0; i < N; i++) {
			count += sort(a[i]);
		}

		for (int i = 0; i < N - 1; i++) {
			int x = i % K;
			int y = i / K;
			int nx = (i + 1) % K;
			int ny = (i + 1) / K;
			if (a[nx][ny] < a[x][y] && a[x][y] > 0 && a[nx][ny] > 0) {
				return -1;
			}
		}

		return count;
	}

	private static int sort(int[] ar) {
		int c = 0;
		for (int i = 0; i < ar.length; i++) {
			for (int j = i + 1; j < ar.length; j++) {
				if (ar[i] > 0 && ar[j] > 0 && ar[j] < ar[i]) {
					int tmp = ar[j];
					ar[j] = ar[i];
					ar[i] = tmp;
					c++;
				}

			}
		}
		return c;
	}
}
