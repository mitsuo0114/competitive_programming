package jp.fedom.challange.probook.p49;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test_simple1() {
		int[] L = new int[] { 4, 2 };
		int N = 2;

		assertThat(Main.solve(L, N), is(6));
	}

	@Test
	public void test1() {
		int[] L = new int[] { 8, 5, 8 };
		int N = 3;

		assertThat(Main.solve(L, N), is(34));
	}

	@Test
	public void test2() {
		int[] L = new int[] { 8, 2, 3, 8 };
		int N = 4;

		assertThat(Main.solve(L, N), is(39));
	}
}
