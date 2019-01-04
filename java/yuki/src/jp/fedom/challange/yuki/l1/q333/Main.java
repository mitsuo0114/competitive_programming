package jp.fedom.challange.yuki.l1.q333;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] input = new String[1];
		int i = 0;
		while (sc.hasNext()) {
			input[i] = sc.nextLine();
			i++;
		}

		System.out.println(solve(input));

		sc.close();
	}

	public static long solve(String[] in) {
		long a = Long.valueOf(in[0].split(" ")[0]);
		long b = Long.valueOf(in[0].split(" ")[1]);
		if (b > a) {
			// b > a > c || b > c > a;
			return b - 2L;
		} else {
			// a > c > b
			return 2000000000L - b - 1L;
		}
	}
}
