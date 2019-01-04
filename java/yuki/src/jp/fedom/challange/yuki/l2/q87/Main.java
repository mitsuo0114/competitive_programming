package jp.fedom.challange.yuki.l2.q87;

import java.math.BigInteger;
import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.LocalDateTime;
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

	static DayOfWeek D = LocalDate.of((int) 2014, 7, 23).getDayOfWeek();

	public static long solve_slow(List<String> in) {
		long N = Integer.valueOf(in.get(0).split(" ")[0]);
		long count = 0;

		for (long i = 2015; i <= N; i++) {
			if (LocalDate.of((int) i, 7, 23).getDayOfWeek() == D) {
				count++;
			}
		}

		return count;
	}

	public static long solve(List<String> in) {
		BigInteger N = new BigInteger(in.get(0).split(" ")[0]);
		long count0_2015 = 288L;

		long count400 = 0;
		for (long i = 1; i <= 400; i++) {
			if (LocalDate.of((int) i, 7, 23).getDayOfWeek() == D) {
				count400++;
			}
		}

		long count = 0;
		long M = N.mod(BigInteger.valueOf(400L)).longValue();
		for (long i = 0; i <= M; i++) {
			if (LocalDate.of((int) i, 7, 23).getDayOfWeek() == D) {
				count++;
			}
		}

		return (count400 * N.divide(BigInteger.valueOf(400L)).longValue()) + count - count0_2015;
	}
}
