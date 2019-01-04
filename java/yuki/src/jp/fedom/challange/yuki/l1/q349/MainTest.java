package jp.fedom.challange.yuki.l1.q349;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] in ={
				"12",
				"ne",
				"ushi",
				"tora",
				"u",
				"tatsu",
				"mi",
				"uma",
				"hitsuji",
				"saru",
				"tori",
				"inu",
				"i",
		};
				
		assertThat(Main.solve(in), is("YES"));
	}

	@Test
	public void test2() {
		String[] in = {
				"3",
				"saru",
				"saru",
				"saru",
		};
		assertThat(Main.solve(in), is("NO"));
	}
	
	@Test
	public void test2_() {
		String[] in = {
				"5",
				"saru",
				"saru",
				"saru",
				"u",
				"u",
		};
		assertThat(Main.solve(in), is("YES"));
	}
	
	
	@Test
	public void test2__() {
		String[] in = {
				"8",
				"saru",
				"saru",
				"saru",
				"u",
				"u",
				"u",
				"u",
				"u",
		};
		assertThat(Main.solve(in), is("YES"));
	}

	@Test
	public void test2___() {
		String[] in = {
				"9",
				"saru",
				"saru",
				"saru",
				"u",
				"u",
				"u",
				"u",
				"u",
				"u",
		};
		assertThat(Main.solve(in), is("NO"));
	}
	@Test
	public void test3() {
		String[] in = {
				"15",
				"u",
				"ushi",
				"tora",
				"tora",
				"hitsuji",
				"saru",
				"saru",
				"hitsuji",
				"tatsu",
				"hitsuji",
				"ne",
				"inu",
				"hitsuji",
				"u",
				"mi",
		};
		assertThat(Main.solve(in), is("YES"));
	}

}
