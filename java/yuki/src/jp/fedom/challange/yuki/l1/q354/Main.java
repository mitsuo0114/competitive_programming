package jp.fedom.challange.yuki.l1.q354;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String input;
		if (args.length == 0) {
			input = sc.nextLine();
		} else {
			input = args[0];
		}

		System.out.println(input);

		sc.close();
	}
}
