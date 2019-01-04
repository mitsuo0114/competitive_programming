package jp.fedom.challange.probook.p53;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;


public class MainTest {
	
	@Test
	public void test_simple1() {
		Item[] items = new Item[]{
				new Item(2,3),
				new Item(1,2),
				new Item(3,4),
				new Item(2,2)
		};
		
		assertThat(Main.solve(items, 4, 5), is(7));
	}
	
}
