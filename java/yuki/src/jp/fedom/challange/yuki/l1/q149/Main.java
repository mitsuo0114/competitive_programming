package jp.fedom.challange.yuki.l1.q149;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

	final static String d = System.getProperty("line.separator");

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
		Integer Aw = Integer.valueOf(in.get(0).split(" ")[0]);
		Integer Ab = Integer.valueOf(in.get(0).split(" ")[1]);
		Integer Bw = Integer.valueOf(in.get(1).split(" ")[0]);
		Integer C = Integer.valueOf(in.get(2).split(" ")[0]);
		Integer D = Integer.valueOf(in.get(2).split(" ")[1]);

		int mo = Math.min(Ab, C);
		Bw += C - mo;
		Aw -= C - mo;

		mo = Math.min(Bw, D);
		Aw += mo;

		return Aw;

	}

}
