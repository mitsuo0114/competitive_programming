package jp.fedom.challange.yuki.l1.q172;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.Arrays;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] in = { "2 2 1" };

		assertThat(Main.solve(Arrays.asList(in)), is(6));
	}

	@Test
	public void test2() {
		String[] in = { "-50 -40 30", };

		assertThat(Main.solve(Arrays.asList(in)), is(133));
	}

	@Test
	public void test3() {
		String[] in = { "0 0 100", };

		assertThat(Main.solve(Arrays.asList(in)), is(142));
	}
	
	@Test
	public void test5() {
		String[] in = { "10 0 1", };

		assertThat(Main.solve(Arrays.asList(in)), is(12));
	}
}
