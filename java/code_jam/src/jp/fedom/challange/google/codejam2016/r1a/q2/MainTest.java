package jp.fedom.challange.google.codejam2016.r1a.q2;

import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.List;

import org.junit.Test;

public class MainTest {

	@Test
	public void test_solve_sample1() {
		List<String> q = new ArrayList<>();
		q.add("1 2 3");
		q.add("2 3 5");
		q.add("3 5 6");
		q.add("2 3 4");
		q.add("1 2 3");
		
		assertEquals("Case #1: 3 4 6", Main.solve(1,q));
	}

	@Test
	public void test_solve_sample2() {
		List<String> q = new ArrayList<>();
		q.add("1 2 3");
		q.add("2 3 5");
		q.add("3 4 6");
		q.add("3 5 6");
		q.add("2 3 4");
		
		assertEquals("Case #1: 1 2 3", Main.solve(1,q));
	}
	
	@Test
	public void test_solve_sample3() {
		List<String> q = new ArrayList<>();
		q.add("11 14 16 22");
		q.add("3 6 9 11");
		q.add("6 7 11 14");
		q.add("9 11 15 19");
		q.add("10 11 19 22");
		q.add("6 7 10 11");
		q.add("3 6 8 10");
		
		assertEquals("Case #1: 8 10 15 16", Main.solve(1,q));
	}
	@Test
	public void test_solve_sample4() {
		List<String> q = new ArrayList<>();
		q.add("22 222");
		q.add("2 22");
		q.add("2 22");
		
		assertEquals("Case #1: 22 222", Main.solve(1,q));
	}
	}
