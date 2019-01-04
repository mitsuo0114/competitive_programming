package jp.fedom.challange.yuki.l2.q78;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Arrays;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] in = { "5 4","01200" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), 
				is(Main.solve_slow(new ArrayList<>(Arrays.asList(in)))));
	}
	
	@Test
	public void test2() {
		String[] in = { "2 10000","10" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), 
				is(Main.solve_slow(new ArrayList<>(Arrays.asList(in)))));
	}

	@Test
	public void test2__() {
		String[] in = { "2 100","20" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), 
				is(Main.solve_slow(new ArrayList<>(Arrays.asList(in)))));
	}

	@Test
	public void test3() {
		String[] in = { "10 100","2222222222" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(1L));
	}

	@Test
	public void test3_() {
		String[] in = { "10 2000000000","2222222222" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(1L));
	}

	@Test
	public void test4() {
		String[] in = { "2 5","01" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(3L));
	}
	@Test
	public void test4_() {
		String[] in = { "3 100","002" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(35L));
	}

	@Test
	public void test4__() {
		String[] in = { "3 100","020" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), 
				is(Main.solve_slow(new ArrayList<>(Arrays.asList(in)))));
	}


	@Test
	public void test4__101() {
		String[] in = { "3 101","020" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), 
				is(Main.solve_slow(new ArrayList<>(Arrays.asList(in)))));
	}

	@Test
	public void test4__102() {
		String[] in = { "3 102","020" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), 
				is(Main.solve_slow(new ArrayList<>(Arrays.asList(in)))));
	}

	@Test
	public void test5() {
		String[] in = { "6 10","120202" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(1L));
	}

	@Test
	public void test6() {
		String[] in = { "6 10","000222" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(4L));
	}

	@Test
	public void test7() {
		String[] in = { "3 100","012" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(2L));
	}

	@Test
	public void test8() {
		String[] in = { "4 1000","0022" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), 
				is(Main.solve_slow(new ArrayList<>(Arrays.asList(in)))));
	}


	@Test
	public void test9() {
		String[] in = { "4 1000","0102" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), 
				is(Main.solve_slow(new ArrayList<>(Arrays.asList(in)))));

	}



	@Test
	public void test10() {
		String[] in = { "4 10000","0201" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), 
				is(Main.solve_slow(new ArrayList<>(Arrays.asList(in)))));

	}

	@Test
	public void test11() {
		String[] in = { "6 10003","010101" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), 
				is(Main.solve_slow(new ArrayList<>(Arrays.asList(in)))));
	}
	@Test
	public void test12() {
		String[] in = { "6 10000","002002" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), 
				is(Main.solve_slow(new ArrayList<>(Arrays.asList(in)))));
	}

	
	
}