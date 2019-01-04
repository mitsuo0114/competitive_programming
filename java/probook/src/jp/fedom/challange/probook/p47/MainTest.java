package jp.fedom.challange.probook.p47;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		int[] x = new int[] { 1, 7, 15, 20, 30, 50 };
		int r = 10;

		assertThat(Main.solve(x, r), is(3));
	}
}
