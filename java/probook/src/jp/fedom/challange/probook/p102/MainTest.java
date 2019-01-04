package jp.fedom.challange.probook.p102;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import org.junit.Test;

public class MainTest {

	@Test
	public void test1() {
		V[] vs = new V[8];
		vs[0] = new V(1, 2, 100);
		vs[1] = new V(2, 4, 200);
		vs[2] = new V(2, 3, 250);
		vs[3] = new V(4, 3, 100);
		
		vs[4] = new V(2, 1, 100);
		vs[5] = new V(4, 2, 200);
		vs[6] = new V(3, 2, 250);
		vs[7] = new V(3, 4, 100);

		assertThat(Main.solve(vs, 8, 4), is(450));
	}

}
