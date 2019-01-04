package jp.fedom.challange.yuki.l1.q353;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String input = "";
		if (args.length == 0) {
			input = sc.nextLine();
		} else {
			input = args[0];
		}

		System.out.println(solve(input));

		sc.close();
	}

	public static String solve(String in) {

		BigInteger bi = BigInteger.ZERO;
		bi = bi.add(BigInteger.valueOf(Long.valueOf(in.split(" ")[0])));
		bi = bi.add(BigInteger.valueOf(Long.valueOf(in.split(" ")[1])));

		return bi.toString();
	}
}
