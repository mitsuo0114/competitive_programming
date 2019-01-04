package jp.fedom.challange.google.codejam2015.r1b.q1;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test() {
		assertThat(Main.swap(1L), is(1L));
		assertThat(Main.swap(21L), is(12L));
		assertThat(Main.swap(321L), is(123L));
	}
	@Test
	public void test2() {
		assertThat(Main.solve(1,1), is("Case #1: 1"));
		assertThat(Main.solve(19, 2), is("Case #2: 19"));
		assertThat(Main.solve(23, 3), is("Case #3: 15"));
		assertThat(Main.solve(20, 4), is("Case #4: 20"));
	}
	@Test
	public void test3() {
		assertThat(Main.solve(92,1), is("Case #1: 21"));
		assertThat(Main.solve(12345678,1), is("Case #1: " + (Main.reachCount(8) + 4321L + 1L + 5678L - 1L)));
//		assertThat(Main.solve(19, 2), is("Case #2: 19"));
//		assertThat(Main.solve(23, 3), is("Case #3: 15"));
	}

	@Test
	public void leftright() {
		assertThat(Main.left("12"), is("1"));
		assertThat(Main.right("12"), is("2"));
		assertThat(Main.left("1234"), is("12"));
		assertThat(Main.right("1234"), is("34"));
		assertThat(Main.left("12345"), is("12"));
		assertThat(Main.right("12345"), is("345"));
	}
	
	@Test
	public void reachCount() {
		assertThat(Main.reachCount(2), is(10L));
		assertThat(Main.reachCount(3), is(Main.reachCount(2) + 9L + 1L + 9L));
		assertThat(Main.reachCount(4), is(Main.reachCount(3) + 99L + 1L + 9L));
		assertThat(Main.reachCount(5), is(Main.reachCount(4) + 99L + 1L + 99L));
		assertThat(Main.reachCount(6), is(Main.reachCount(5) + 999L + 1L + 99L));
		assertThat(Main.reachCount(7), is(Main.reachCount(6) + 999L + 1L + 999L));
		assertThat(Main.reachCount(8), is(Main.reachCount(7) + 9999L + 1L + 999L));
		assertThat(Main.reachCount(9), is(Main.reachCount(8) + 9999L + 1L + 9999L));
	}
	
	

}
