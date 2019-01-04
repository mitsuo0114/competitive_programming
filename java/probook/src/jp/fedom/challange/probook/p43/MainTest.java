package jp.fedom.challange.probook.p43;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		int[] s = new int[] { 1, 2, 4, 6, 8 };
		int[] e = new int[] { 3, 5, 7, 9, 10 };

		assertThat(Main.solve(s, e), is(3));
	}


	@Test
	public void test2() {
		int[] s = new int[] { 1, 2, 4 };
		int[] e = new int[] { 10, 3, 5 };

		assertThat(Main.solve(s, e), is(2));
	}

	@Test
	public void test3() {
		int[] s = new int[] { 1, 5, 3 };
		int[] e = new int[] { 4, 8, 6 };

		assertThat(Main.solve(s, e), is(2));
	}

}
