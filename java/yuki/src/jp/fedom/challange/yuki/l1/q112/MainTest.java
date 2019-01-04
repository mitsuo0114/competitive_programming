package jp.fedom.challange.yuki.l1.q112;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.Arrays;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] in = { "2", "2 4"};

		assertThat(Main.solve(Arrays.asList(in)), is("1 1"));
	}

	@Test
	public void test2() {
		String[] in = { "3", "4 4 4"};

		assertThat(Main.solve(Arrays.asList(in)), is("3 0"));
	}
	
	@Test
	public void test2_() {
		String[] in = { "3", "8 6 6"};

		assertThat(Main.solve(Arrays.asList(in)), is("1 2"));
	}
	
	@Test
	public void test2__() {
		String[] in = { "3", "4 6 6"};

		assertThat(Main.solve(Arrays.asList(in)), is("2 1"));
	}


	@Test
	public void test3() {
		String[] in = { "3", "8 8 8"};

		assertThat(Main.solve(Arrays.asList(in)), is("0 3"));
	}
}
