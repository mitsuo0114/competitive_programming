package jp.fedom.challange.yuki.l2.q8;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Arrays;

import org.junit.Ignore;
import org.junit.Test;

public class MainTest {

	@Test
	public void test() {
		String[] in = { "1", "21 3" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("Lose"));
	}

	@Test
	public void test2() {
		String[] in = { "1", "12 5" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("Win"));
	}

	@Test
	public void test3() {
		String[] in = { "3", "5 10", "40 6", "100 8" };

		String d = "\r\n";
		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("Win" + d + "Win" + d + "Lose"));
	}

	@Test
	public void test4() {
		String[] in = { "1", "10 3" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("Win"));
	}

	@Test
	public void test5() {
		String[] in = { "1", "10 9" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("Win"));
	}

	@Test
	public void test6() {
		String[] in = { "1", "10 8" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("Lose"));
	}

	@Test
	public void test_max() {
		String[] in = { "1", "120000 119999" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("Win"));
	}

	@Test
	public void test_max2() {
		String[] in = { "1", "120000 119998" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("Lose"));
	}

	@Test
	public void test_max3() {
		String[] in = { "1", "120000 119997" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("Win"));
	}
}
