package jp.fedom.challange.yuki.l2.q4;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Arrays;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] in = { "3", "1 2 3" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("possible"));
	}

	@Test
	public void test2() {
		String[] in = { "5", "1 2 3 4 5" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("impossible"));
	}

	@Test
	public void test3() {
		String[] in = { "15", "62 8 90 2 24 62 38 64 76 60 30 76 80 74 72", };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("impossible"));
	}
	
	@Test
	public void t1() {
		String[] in = { "3", "1 1 1" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("impossible"));
	}

	@Test
	public void t2() {
		String[] in = { "4", "1 1 1 1" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("possible"));
	}
	
	@Test
	public void t3() {
		String[] in = { "4", "1 1 1 1" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("possible"));
	}
}