package jp.fedom.challange.yuki.l2.q106;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Arrays;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] in = { "2 1" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(1));
	}

	@Test
	public void test2() {
		String[] in = { "4 2" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(0));
	}

	@Test
	public void test3() {
		String[] in = { "1000 4" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(23));
	}
	
	@Test
	public void test_max() {
		String[] in = { "2000000 4" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(545961));
	}

}