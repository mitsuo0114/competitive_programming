package jp.fedom.challange.probook.p93;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test0() {
		V[] vs = new V[]{
				new V(0,1),
		};
		assertThat(Main.solve(2, vs), is(true));
	}

	
	@Test
	public void test1() {
		V[] vs = new V[]{
				new V(0,1),
				new V(0,2),
				new V(1,2)
		};
		assertThat(Main.solve(3, vs), is(false));
	}

	@Test
	public void test2() {
		V[] vs = new V[]{
				new V(0,1),
				new V(0,3),
				new V(1,2),
				new V(2,3)
		};
		assertThat(Main.solve(4, vs), is(true));
	}

}
