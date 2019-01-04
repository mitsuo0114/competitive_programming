package jp.fedom.challange.probook.p62;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test_simple1() {
		int n = 3;
		int[] a = { 3, 5, 8 };
		int[] m = { 3, 2, 2 };
		int K = 17;

		assertThat(Main.solve1(n, a, m, K), is(true));
	}

}
