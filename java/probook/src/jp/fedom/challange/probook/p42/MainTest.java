package jp.fedom.challange.probook.p42;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		int[] coins = new int[] { 3, 2, 1, 3, 0, 2 };

		assertThat(Main.solve(coins, 620), is(6));
	}

}
