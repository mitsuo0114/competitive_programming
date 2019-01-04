package jp.fedom.challange.yuki.l1.q296;

import java.time.LocalDateTime;
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

	public static String solve(List<String> in) {
		Integer N = Integer.valueOf(in.get(0).split(" ")[0]);
		Integer H = Integer.valueOf(in.get(0).split(" ")[1]);
		Integer M = Integer.valueOf(in.get(0).split(" ")[2]);
		Integer T = Integer.valueOf(in.get(0).split(" ")[3]);

		LocalDateTime now = LocalDateTime.of(2016, 1, 1, H, M);
		now = now.plusMinutes((N - 1) * T);

		return now.getHour() + d + now.getMinute();
	}

}
