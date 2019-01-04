package jp.fedom.challange.yuki.l2.q8;

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

	public static String solve(List<String> in) {
		int P = Integer.valueOf(in.get(0));
		StringBuilder sb = new StringBuilder();
		in.remove(0);

		for (String s : in) {
			int n = Integer.valueOf(s.split(" ")[0]);
			int k = Integer.valueOf(s.split(" ")[1]);
			if (n <= k) {
				sb.append("Win");
			} else {
				int m = (n - 1) % (k + 1);
				if (m == 0) {
					sb.append("Lose");
				} else {
					sb.append("Win");
				}
			}
			sb.append("\r\n");
		}

		return sb.toString().trim();

	}
}
