package jp.fedom.challange.google.codejam2016.r1a.q1;

import static org.junit.Assert.*;

import java.util.ArrayList;

import jp.fedom.challange.google.common.Utils;

import org.junit.Test;
import static org.hamcrest.CoreMatchers.*;

public class MainExecuteTest {

	@Test
	public void test_solve_sample1() {
		String s = "CAB";
		assertEquals("Case #1: CAB", MainExecute.solve(s, 1));
	}
	
	@Test
	public void test_solve_sample2() {
		String s = "JAM";
		assertEquals("Case #1: MJA", MainExecute.solve(s, 1));
	}
	
	@Test
	public void test_solve_sample3() {
		String s = "CODE";
		assertEquals("Case #1: OCDE", MainExecute.solve(s, 1));
	}

	@Test
	public void test_solve_sample4() {
		String s = "ABAAB";
		assertEquals("Case #1: BBAAA", MainExecute.solve(s, 1));
	}
	
	@Test
	public void test_solve_sample5() {
		String s = "CABCBBABC";
		assertEquals("Case #1: CCCABBBAB", MainExecute.solve(s, 1));
	}
	
	@Test
	public void test_solve_sample6() {
		String s = "ABCABCABC";
		assertEquals("Case #1: CCCBAABAB", MainExecute.solve(s, 1));
	}
	
	@Test
	public void test_solve_sample7() {
		String s = "ZXCASDQWE";
		assertEquals("Case #1: ZXCASDQWE", MainExecute.solve(s, 1));
	}
}
