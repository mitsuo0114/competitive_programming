package jp.fedom.challange.yuki.l1.q112;

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
		int N = Integer.valueOf(in.get(0).split(" ")[0]);
		int t = 0;
		for (String s : in.get(1).split(" ")) {
			t += Integer.valueOf(s);
		}
		int kame = (t - ((N - 1) * N * 2)) / (2 * (N - 1));
		int tsuru = N - kame;
		return tsuru + " " + kame;
	}

}
