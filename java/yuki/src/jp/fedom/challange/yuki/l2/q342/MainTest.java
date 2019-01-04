package jp.fedom.challange.yuki.l2.q342;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Arrays;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] in = { "ŠC‘¯‰¤‚É‚—‰´‚Í‚È‚é‚—‚—" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("‰´‚Í‚È‚é"));
	}

	@Test
	public void test1_() {
		String[] in = { "‚¤‚Í‚—‚—‚—‚—‚—‚¨‚‹‚—‚—‚—‚—‚—" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("‚¤‚Í" + System.lineSeparator() + "‚¨‚‹"));
	}

	@Test
	public void test1__() {
		String[] in = { "‚—‚—‚»‚ê‚È‚—‚—" };

		assertThat(Main.solve(new ArrayList<>(Arrays.asList(in))), is("‚»‚ê‚È"));
	}

}