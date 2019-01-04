package jp.fedom.challange.probook.p58;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;


public class MainTest {
	
	@Test
	public void test_simple1() {
		Item[] items = new Item[]{
				new Item(3,4),
				new Item(4,5),
				new Item(2,3),
		};
		
		assertThat(Main.solve1(items, 3, 7), is(10));
		assertThat(Main.solve2(items, 3, 7), is(10));
	}
	
}
