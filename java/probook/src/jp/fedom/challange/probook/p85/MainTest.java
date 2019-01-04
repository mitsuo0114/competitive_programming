package jp.fedom.challange.probook.p85;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test_simple1() {
		Info[] info = new Info[]	{ 
				new Info(1, 101, 1),
				new Info(2, 1, 2),
				new Info(2, 2, 3),
				new Info(2, 3, 3),
				new Info(1, 1, 3),
				new Info(2, 3, 1),
				new Info(1, 5, 5),
						};
		int K = 100;

		assertThat(Main.solve(info, K), is(3));
	}
}
