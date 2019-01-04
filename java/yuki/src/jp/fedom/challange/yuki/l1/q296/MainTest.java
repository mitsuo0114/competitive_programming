package jp.fedom.challange.yuki.l1.q296;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.Arrays;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] in = { "2 7 30 5" };

		assertThat(Main.solve(Arrays.asList(in)), is("7" + Main.d + "35"));
	}

	@Test
	public void test2() {
		String[] in = { "1 8 0 5" };

		assertThat(Main.solve(Arrays.asList(in)), is("8" + Main.d + "0"));
	}

	@Test
	public void test3() {
		String[] in = { "7 8 0 5" };

		assertThat(Main.solve(Arrays.asList(in)), is("8" + Main.d + "30"));
	}
}
