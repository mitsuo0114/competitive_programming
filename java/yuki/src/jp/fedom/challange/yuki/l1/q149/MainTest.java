package jp.fedom.challange.yuki.l1.q149;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.Arrays;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] in = { "2 1", "1 2", "2 3", };

		assertThat(Main.solve(Arrays.asList(in)), is(3));
	}

	@Test
	public void test2() {
		String[] in = { "2 0", "0 3", "2 1", };

		assertThat(Main.solve(Arrays.asList(in)), is(1));
	}

	@Test
	public void test3() {
		String[] in = { "3 0", "2 3", "0 5", };

		assertThat(Main.solve(Arrays.asList(in)), is(5));
	}

	@Test
	public void test4() {
		String[] in = { "43682 82641", "54647 3647", "92674 64591", };

		assertThat(Main.solve(Arrays.asList(in)), is(98240));
	}
}
