package jp.fedom.challange.yuki.l2.q297;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test() {
		assertThat(Main.solve(5, new String[] { "1", "1", "1", "+", "+" }), is("3 3"));
		assertThat(Main.solve(3, new String[] { "1", "3", "-" }), is("2 -2"));
		assertThat(Main.solve(5, new String[] { "1", "2", "3", "-", "4" }), is("431 -431"));
	}
	@Test
	public void test_zero() {
		assertThat(Main.solve(4, new String[] { "1", "0", "9", "+" }), is("91 10"));
		assertThat(Main.solve(4, new String[] { "1", "0", "0", "9", "+" }), is("910 10"));
		assertThat(Main.solve(5, new String[] { "1", "1", "0", "9", "+" }), is("911 20"));
	}

	
	@Test
	public void test2() {
		assertThat(Main.solve(6, new String[] { "1", "2", "3", "-", "+","4" }), is("44 -40"));
		assertThat(Main.solve(15, new String[] { "9","9","9","9","9",
				                                 "9","9","9","9","9",
				                                 "9","9","9","9", "+" }), is("10000000000008 10000000000008"));
		assertThat(Main.solve(15, new String[] { 
				"9","9","9","9","9",
                "9","9","9","9","9",
                "9","9","9","0", "+" }), is("9999999999999 1000000000008"));
		assertThat(Main.solve(15, new String[] { "9","9","9","9","9",
                "9","9","9","9","9",
                "9","9","9","9", "-" }), is("9999999999990 -9999999999990"));

	}

}
