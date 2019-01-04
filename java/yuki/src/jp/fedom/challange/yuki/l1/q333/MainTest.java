package jp.fedom.challange.yuki.l1.q333;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] in = { "2 3", };

		assertThat(Main.solve(in), is(1L));
	}

	@Test
	public void test2() {
		String[] in = { "2 1", };

		assertThat(Main.solve(in), is(1999999998L));
	}

	@Test
	public void test3() {
		String[] in = { "1999999999 1999999998", };

		assertThat(Main.solve(in), is(1L));
	}

	@Test
	public void test4() {
		String[] in = { "1999999999 2000000000", };

		assertThat(Main.solve(in), is(1999999998L));
	}

	@Test
	public void test5() {
		String[] in = { "5 10", };
		assertThat(Main.solve(in), is(8L));
	}

	@Test
	public void test5__() {
		String[] in = { "10 5", };
		assertThat(Main.solve(in), is(1999999994L));
	}

	@Test
	public void test6() {
		String[] in = { "1999999999 2000000000", };

		assertThat(Main.solve(in), is(1999999998L));
	}

}
