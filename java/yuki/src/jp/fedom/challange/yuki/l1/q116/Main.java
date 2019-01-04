package jp.fedom.challange.yuki.l1.q116;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] input = new String[2];
		int i = 0;
		while (sc.hasNext()) {
			input[i] = sc.nextLine();
			i++;
		}

		System.out.println(solve(input));

		sc.close();
	}

	public static int solve(String[] in) {
		int N = Integer.valueOf(in[0]);

		List<Integer> as = new ArrayList<>();

		String[] ss = in[1].split(" ");
		for (int i = 0; i < N; i++) {
			as.add(Integer.valueOf(ss[i]));
		}

		int count = 0;
		for (int i = 0; i < N - 2; i++) {
			int a = as.get(i);
			int b = as.get(i + 1);
			int c = as.get(i + 2);
			if ((a != b && b != c && c != a) && ((b < a && b < c) || (c < b && a < b))) {
				count++;
			}
		}
		return count;
	}
}
