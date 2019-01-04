package jp.fedom.challange.probook.p25;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		List<Long> numbers = new ArrayList<Long>();
		String num = "1 3 5";

		numbers = toList(num);
		long target = 10;
		assertThat(Main.solve(numbers, target), is(true));
		assertThat(Main.solve2(numbers, target), is(true));
		assertThat(Main.solve3(numbers, target), is(true));
	}

	@Test
	public void test_rnd() {
		List<Long> numbers = new ArrayList<Long>();

		int n = 100;
		long s = System.currentTimeMillis();
		System.out.println(0);
		for (int i = 0; i < 100; i++) {
			numbers = rmdList(n);
			long target = (long) (Math.random() * 100_000_000L);
			assertThat(Main.solve(numbers, target), is(Main.solve2(numbers, target)));
		}
		long ss = System.currentTimeMillis();
		System.out.println(ss -s);

		for (int i = 0; i < 100; i++) {
			numbers = rmdList(n);
			long target = (long) (Math.random() * 100_000_000L);
			assertThat(Main.solve(numbers, target), is(Main.solve3(numbers, target)));
		}
		long sss = System.currentTimeMillis();
		System.out.println(sss - ss);
	}
	
	@Test
	public void test_rnd2() {
		List<Long> numbers = new ArrayList<Long>();

		int n = 500;
		int m = 1;
		numbers = rmdList(n);
		long target = (long) (Math.random() * 100_000_000L);

		long s = System.currentTimeMillis();
		System.out.println(0);
		for (int i = 0; i < m; i++) {
			Main.solve(numbers, target);
		}
		long ss = System.currentTimeMillis();
		System.out.println(ss -s);
		for (int i = 0; i < m; i++) {
			Main.solve2(numbers, target);
		}
		long sss = System.currentTimeMillis();
		System.out.println(sss - ss);
		for (int i = 0; i < m; i++) {
			Main.solve3(numbers, target);
		}
		long ssss = System.currentTimeMillis();
		System.out.println(ssss - sss);
	}

	private List<Long> rmdList(int n) {
		List<Long> numbers = new ArrayList<Long>();
		for (int i = 0; i < n; i++) {
			numbers.add((long) (Math.random() * 100_000_000L));
		}
		return numbers;
	}

	private List<Long> toList(String num) {
		List<Long> numbers = new ArrayList<Long>();
		String[] n = num.split(" ");
		for (int i = 0; i < n.length; i++) {
			numbers.add(Long.parseLong(n[i]));
		}
		return numbers;
	}

}
