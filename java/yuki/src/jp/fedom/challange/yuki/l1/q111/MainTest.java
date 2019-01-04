package jp.fedom.challange.yuki.l1.q111;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.Arrays;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] in = { "5" };

		assertThat(Main.solve(Arrays.asList(in)), is(4L));
	}

	@Test
	public void test2() {
		String[] in = { "9", };

		assertThat(Main.solve(Arrays.asList(in)), is(16L));
	}

	@Test
	public void test3() {
		String[] in = { "200001", };

		assertThat(Main.solve(Arrays.asList(in)), is(10000000000L));
	}
	

	@Test
	public void test4() {
		String[] in = { "100000001", };

		assertThat(Main.solve(Arrays.asList(in)), is(2500000000000000L));
	}
}
