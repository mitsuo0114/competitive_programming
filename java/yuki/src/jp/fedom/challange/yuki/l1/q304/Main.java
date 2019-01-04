package jp.fedom.challange.yuki.l1.q304;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		new Main().solve();
	}

	public void solve() {
		List<String> candidate = new ArrayList<String>();
		for (int j = 0; j < 1000; j++) {
			candidate.add(String.format("%3d", j).replace(" ", "0"));
		}
		for (String c : candidate) {
			send(c);
			String input = get();
			if (input.equals("unlocked")) {
				break;
			}
		}

	}

	protected void send(String s) {
		System.out.println(s);
		System.out.flush();

	}

	protected String get() {
		return sc.nextLine();
	}

}
