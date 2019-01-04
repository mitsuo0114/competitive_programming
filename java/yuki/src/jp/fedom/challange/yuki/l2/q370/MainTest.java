package jp.fedom.challange.yuki.l2.q370;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test() {
		assertThat(Main.solve(3, 5, new int[] { 1, 2, 3, 4, 5 }), is(3));
		assertThat(Main.solve(2, 4, new int[] { -5, -1, 2, 5 }), is(4));
		assertThat(Main.solve(2, 5, new int[] { -3, -1, 0, 2, 4 }), is(1));
	}

	@Test
	public void test1() {
		assertThat(Main.solve(3, 5, new int[] { -1, -2, -3, -4, -5 }), is(3));

		assertThat(Main.solve(2, 2, new int[] { -10000, 10000 }), is(30000));
		assertThat(Main.solve(2, 2, new int[] { -9999, 10000 }), is(29998));
		assertThat(Main.solve(2, 2, new int[] { -10000, 9999 }), is(29998));
	}

}
