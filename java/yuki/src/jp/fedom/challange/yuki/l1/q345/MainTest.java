package jp.fedom.challange.yuki.l1.q345;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.Arrays;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] in = { "ilovechiwawa"};

		assertThat(Main.solve(Arrays.asList(in)), is(6));
	}

	@Test
	public void test2() {
		String[] in = { "wachiwachi"};

		assertThat(Main.solve(Arrays.asList(in)), is(-1));
	}
	
	@Test
	public void test3() {
		String[] in = { "chiwaaaaaaamikawayadeeeeesu"};

		assertThat(Main.solve(Arrays.asList(in)), is(16));
	}

	@Test
	public void test4() {
		String[] in = { "cww"};

		assertThat(Main.solve(Arrays.asList(in)), is(3));
	}

	@Test
	public void test5() {
		String[] in = { "chiwaaaaaaamikawayadeeeeccccesucww"};

		assertThat(Main.solve(Arrays.asList(in)), is(3));
	}
}
