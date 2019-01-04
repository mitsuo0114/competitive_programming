package jp.fedom.challange.yuki.l3.q33;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Arrays;

import org.junit.Ignore;
import org.junit.Test;

public class MainTest {

	@Test
	public void test1_solve2() {
		String[] in = { "2 3 1", "0 7" };
		System.out.println(Long.toBinaryString((long)10e12).length());
//		assertThat(Main.solve2(new ArrayList<>(Arrays.asList(in))), is(6));
	}
	
	@Test
	public void test1() {
		String[] in = { "2 3 1", "0 7" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(6));
	}

	@Test
	public void test2() {
		String[] in = { "2 3 2", "0 6" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(7));
	}

	
	@Test
	public void test3() {
		String[] in = { "2 3 1", "0 2" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(6));
	}

	@Test
	public void test4() {
		String[] in = { "2 3 1000", "0 7" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is(4002));
	}

}
