package jp.fedom.challange.google.codejam2016.r1b.q3;

import static org.junit.Assert.*;

import java.util.ArrayList;

import jp.fedom.challange.google.codejam2016.r1b.q3.Main.Question;
import jp.fedom.challange.google.common.Utils;

import org.junit.Test;
import static org.hamcrest.CoreMatchers.*;

public class MainTest {

	Question q = new Question();

	@Test
	public void test_solve_sample1() {
		q.size = 3;
		q.f = new String[]{"AA", "AB", "AB"};
		q.s = new String[]{"BA", "BB", "BA"};
		assertEquals("Case #1: 1", Main.solve(q, 1));
	}

	@Test
	public void test_solve_sample2() {
		q.size = 4;
		q.f = new String[]{"AA", "AB", "AB", "AA"};
		q.s = new String[]{"BA", "BB", "BA", "BB"};
		assertEquals("Case #1: 2", Main.solve(q, 1));
		q.size = 4;
		q.f = new String[]{"1A", "1B", "1A", "1B"};
		q.s = new String[]{"2A", "2B", "2B", "2A"};
		assertEquals("Case #1: 2", Main.solve(q, 1));
	}
	
	@Test
	public void test_solve_sample3() {
		q.size = 4;
		q.f = new String[]{"1A", "1B", "1A", "1B"};
		q.s = new String[]{"2A", "2B", "2B", "2A"};
		assertEquals("Case #1: 2", Main.solve(q, 1));
	}

	@Test
	public void test_fetchubset() {
		assertThat(Main.fetchubset(1).size(), is(2));
		assertThat(Main.fetchubset(2).size(), is(2 * 2));
		assertThat(Main.fetchubset(3).size(), is(2 * 2 * 2));
	}
	
	@Test
	public void test_filter() {
		String[] t = new String[]{"1A", "1B", "1A", "1B"};
		assertThat(Main.filter(t, "0000").size(), is(0));
		assertThat(Main.filter(t, "0001").size(), is(1));
	}
}
