package jp.fedom.challange.yuki.l2.q87;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Arrays;

import org.junit.Ignore;
import org.junit.Test;

public class MainTest {

	@Test
	public void test_slow1() {
		String[] in = { "2015" };

		assertThat(Main.solve_slow(new ArrayList<>(Arrays.asList(in))), is(0L));
	}

	@Test
	public void test_slow2() {
		String[] in = { "2038" };

		assertThat(Main.solve_slow(new ArrayList<>(Arrays.asList(in))), is(3L));
	}

	@Test
	public void test_slow4() {
		String[] in = { "3000" };

		assertThat(Main.solve_slow(new ArrayList<>(Arrays.asList(in))), is(141L));
	}

	@Test
	public void test_all() {
		for (int i = 2015; i <= 20000; i++) {
			String[] in = { String.valueOf(i) };

			assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))),
					is(Main.solve_slow(new ArrayList<>(Arrays.asList(in)))));
		}
	}

	@Test
	public void test1() {
		String[] in = { "10000000000" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(1424999712L));
	}

}