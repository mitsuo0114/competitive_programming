package jp.fedom.challange.yuki.l2.q342;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Arrays;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] in = { "海賊王にｗ俺はなるｗｗ" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("俺はなる"));
	}

	@Test
	public void test1_() {
		String[] in = { "うはｗｗｗｗｗおｋｗｗｗｗｗ" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("うは" + System.lineSeparator() + "おｋ"));
	}

	@Test
	public void test1__() {
		String[] in = { "ｗｗそれなｗｗ" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("それな"));
	}

}