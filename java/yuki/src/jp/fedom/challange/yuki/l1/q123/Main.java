package jp.fedom.challange.yuki.l1.q123;

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
		int N = Integer.valueOf(in[0].split(" ")[0]);
		// int M = Integer.valueOf(in[0].split(" ")[1]);

		List<Integer> stack = new ArrayList<>();

		for (int i = 1; i < N + 1; i++) {
			stack.add(i);
		}

		for (String s : in[1].split(" ")) {
			int p = Integer.valueOf(s) - 1;
			int i = stack.get(p);
			stack.remove(p);
			stack.add(0, i);
		}
		return stack.get(0);
	}
}
