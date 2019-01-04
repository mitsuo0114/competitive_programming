package jp.fedom.challange.yuki.l1.q70;

import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] input = new String[31];
		int i = 0;
		while (sc.hasNext()) {
			input[i] = sc.nextLine();
			i++;
		}

		System.out.println(solve(input));

		sc.close();
	}

	public static long solve(String[] in) {
		int m = Integer.valueOf(in[0]);
		long ans = 0;
		for (int i = 1; i <= m; i++) {
			String[] s = in[i].split(" ");
			int sh = Integer.valueOf(s[0].split(":")[0]);
			int sm = Integer.valueOf(s[0].split(":")[1]);
			int eh = Integer.valueOf(s[1].split(":")[0]);
			int em = Integer.valueOf(s[1].split(":")[1]);
			LocalDateTime start = LocalDateTime.of(2016, 1, 1, sh, sm, 0, 0);
			LocalDateTime end = LocalDateTime.of(2016, 1, 2, eh, em, 0, 0);
			long d = ChronoUnit.MINUTES.between(start, end);
			ans += d % (60 * 24);
		}
		return ans;
	}
}
