package jp.fedom.challange.yuki.l1.q239;

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
		int N = Integer.valueOf(in.get(0));
		in.remove(0);
		List<String> cand = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			cand.add(String.valueOf(i));
		}

		for (int i = 0; i < N; i++) {
			String[] s = in.get(i).split(" ");
			for (int j = 0; j < N; j++) {
				if (!s[j].equals("nyanpass") && !s[j].equals("-")) {
					cand.remove(String.valueOf(j));
				}

			}
		}

		if (cand.size() == 1) {
			return Integer.valueOf(cand.get(0)) + 1;
		} else {
			return -1;
		}

	}

}
