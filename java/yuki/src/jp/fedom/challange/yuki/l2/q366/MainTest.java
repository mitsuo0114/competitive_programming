package jp.fedom.challange.yuki.l2.q366;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Arrays;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] in = { "6 2", "8 6 5 3 1 10" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(4));
	}

	@Test
	public void test1_() {
		String[] in = { "6 2", "1 3 5 6 10 8" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(-1));
	}

	@Test
	public void test1__() {
		String[] in = { "6 2", "1 3 5 10 8 6" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(1));
	}

	@Test
	public void test2() {
		String[] in = { "4 3", "5 7 2 11" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(-1));
	}

	@Test
	public void test2_() {
		String[] in = { "4 4", "5 7 2 11" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(-1));
	}

	@Test
	public void test3() {
		String[] in = { "5 10", "1 2 3 5 8" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(0));
	}

}