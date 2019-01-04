package jp.fedom.challange.yuki.l1.q146;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
	static BigInteger t = BigInteger.ZERO;
	static BigInteger TWO = BigInteger.valueOf(2);
	static BigInteger m = new BigInteger("1000000007");

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		long N = sc.nextLong();
		for (long i = 0; i < N; i++) {
			solve(sc.nextBigInteger(), sc.nextBigInteger());
		}
		t = t.mod(m);
		System.out.println(t.toString());

		sc.close();
	}

	public static void solve(BigInteger s, BigInteger k) {
		if (s.testBit(0) == false) {
			t = t.add(s.divide(TWO).multiply(k));
		} else {
			t = t.add((s.add(BigInteger.ONE).divide(TWO).multiply(k)));
		}
	}
}
