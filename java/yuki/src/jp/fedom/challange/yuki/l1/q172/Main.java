package jp.fedom.challange.yuki.l1.q172;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
	public static final double R2 = Math.pow(2, 0.5);

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
		double x = Double.valueOf(in.get(0).split(" ")[0]);
		double y = Double.valueOf(in.get(0).split(" ")[1]);
		double r = Double.valueOf(in.get(0).split(" ")[2]);

		double D = r * R2 + Math.abs(x) + Math.abs(y);

		return new Double(D).intValue() + 1;
	}
}
