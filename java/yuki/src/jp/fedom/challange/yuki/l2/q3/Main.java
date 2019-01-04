package jp.fedom.challange.yuki.l2.q3;

import java.math.BigInteger;
import java.util.ArrayList;
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

	public static int solve(List<String> in) {
		int N = Integer.valueOf(in.get(0));
		Map<Integer, Integer> av = new HashMap<Integer, Integer>();

		av.put(1, 1);
		for (int i = 1; i <= N; i++) {
			// System.out.println(av + " / " + i);
			int bit = BigInteger.valueOf(i).bitCount();
			if (!av.containsKey(i)) {
				continue;
			}

			int minD = av.get(i);

			if (i + bit <= N) {
				if (!av.containsKey(i + bit)) {
					av.put(i + bit, minD + 1);
				}
				av.put(i + bit, Math.min(minD + 1, av.get(i + bit)));
			}

			if (i - bit >= 1) {
				if (!av.containsKey(i - bit)) {
					av.put(i - bit, minD + 1);
					i = 1;
					continue;
				}
				if (minD + 1 < av.get(i - bit)) {
					av.put(i - bit, minD + 1);
					i = 1;
					continue;
				}
			}
		}

		return av.containsKey(N) ? av.get(N) : -1;
	}

}
