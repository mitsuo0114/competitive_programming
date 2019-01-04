package jp.fedom.challange.yuki.l1.q70;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		String[] in ={
				"3",
				"22:24 5:9",
				"22:46 5:37",
				"1:11 7:11",
		};
				
		assertThat(Main.solve(in), is(1176L));
	}

	@Test
	public void test2() {
		String[] in = {
				"5",
				"22:30 4:30",
				"22:46 4:46",
				"1:17 7:26",
				"0:38 7:0",
				"23:49 7:41",
		};
		assertThat(Main.solve(in), is(1943L));
	}

}
