package jp.fedom.challange.yuki.l1.q116;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] in = { "5", "1 3 4 1 2", };

		assertThat(Main.solve(in), is(2));
	}
	@Test
	public void test2() {
		String[] in = { "5", "1 4 2 4 1", };

		assertThat(Main.solve(in), is(2));
	}
	
	@Test
	public void test3() {
		String[] in = { "5", "1 4 1 5 2", };
		
		assertThat(Main.solve(in), is(2));
	}
}
