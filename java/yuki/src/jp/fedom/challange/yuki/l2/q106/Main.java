package jp.fedom.challange.yuki.l2.q106;

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
		int[] f = new int[N + 1];

		int c = 0;

		for (int i = 2; i <= N; i++) {
			if (isPrime(i)) {
				for (int n = 1; n * i <= N; n++) {
					f[n * i]++;
					if (f[n * i] == K) {
						c++;
					}
				}
			}
		}

		return c;
	}

	private static boolean isPrime(int j) {
		int N = (int) Math.sqrt(j);
		boolean isPrime = true;
		for (int i = 2; i <= N; i++) {
			if (j % i == 0) {
				isPrime = false;
				break;
			}
		}
		return isPrime;
	}

}
