package jp.fedom.challange.yuki.l1.q349;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

enum Eto {
	ne, ushi, tora, u, tatsu, mi, uma, hitsuji, saru, tori, inu, i;
}

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] input = new String[51];
		if (args.length == 0) {
			int i = 0;
			while (sc.hasNext()) {
				input[i] = sc.nextLine();
				i++;
			}
		} else {
			input = args;
		}

		System.out.println(solve(input));

		sc.close();
	}

	public static String solve(String[] in) {
		boolean ans = true;
		Map<Eto, Integer> d = new HashMap<>();
		for (Eto e : Eto.values()) {
			d.put(e, 0);
		}

		int total = 0;
		for (int i = 1; i < in.length; i++) {
			if (in[i] == null || in[i].isEmpty()) {
				continue;
			}
			Eto e = Eto.valueOf(in[i]);
			d.put(e, d.get(e) + 1);
			total++;
		}

		for (Eto e : Eto.values()) {
			if (total - d.get(e) < d.get(e) - 1) {
				ans = false;
			}
		}

		return ans ? "YES" : "NO";
	}
}
