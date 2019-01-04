package jp.fedom.challange.probook.p73;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test_simple1() {
		int[] A = new int[] { 10, 14, 20, 21 };
		int[] B = new int[] { 10, 5, 2, 4 };

		assertThat(Main.solve(A, B, 4, 25, 10), is(2));
	}

}
