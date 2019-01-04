package jp.fedom.challange.yuki.l1.q111;

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

	public static long solve(List<String> in) {
		long L = Long.valueOf(in.get(0).split(" ")[0]);
		long ans = 0;
		for (long l = 3; l <= L; l += 2) {
			if (l == 3) {
				ans += 1;
			} else if (l == 5) {
				ans += 3;
			} else {
				ans += l - 2;
			}
		}
		return ans;
	}

}
