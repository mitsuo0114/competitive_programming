package jp.fedom.challange.yuki.l1.q123;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] in = { "3 1", "2", };

		assertThat(Main.solve(in), is(2));
	}
	@Test
	public void test2() {
		String[] in = { "3 2", "3 2", };

		assertThat(Main.solve(in), is(1));
	}
	
	@Test
	public void test3() {
		String[] in = { "4 4", "1 1 1 1", };
		
		assertThat(Main.solve(in), is(1));
	}
	@Test
	public void test4() {
		String[] in = { "10 8", "6 10 4 2 7 1 4 3", };

		assertThat(Main.solve(in), is(10));
	}
}
