package jp.fedom.challange.yuki.l2.q3;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Arrays;

import org.junit.Test;

public class MainTest {

	@Test
	public void test0() {
		String[] in = { "1", };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(1));
	}

	@Test
	public void test0_3() {
		String[] in = { "3", };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(3));
	}

	
	@Test
	public void test1() {
		String[] in = { "5", };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(4));
	}

	@Test
	public void test2() {
		String[] in = { "11", };
		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(9));

	}

	@Test
	public void test3() {
		String[] in = { "4", };
		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(-1));

	}
	
	@Test
	public void test10000() {
		String[] in = { "10000", };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(1610));
	}
}