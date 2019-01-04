package jp.fedom.challange.probook.p103;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import org.junit.Test;

public class MainTest {

	@Test
	public void test_uf() {
		UF t = new UF();
		t.init(10);
		t.unite(1, 2);
		t.unite(2, 3);
		t.unite(3, 4);
		assertThat(t.find(3), is(1));
		assertThat(t.same(2, 4), is(true));
	}

	@Test
	public void test1() {
		R[] rs = new R[8];
		rs[0] = new R(4, 3, 6831);
		rs[1] = new R(1, 3, 4583);
		rs[2] = new R(0, 0, 6592);
		rs[3] = new R(0, 1, 3063);
		rs[4] = new R(3, 3, 4975);
		rs[5] = new R(1, 3, 2049);
		rs[6] = new R(4, 2, 2104);
		rs[7] = new R(2, 2, 781);

		assertThat(Main.solve(rs, 5, 5, 8), is(71071));
	}

}
