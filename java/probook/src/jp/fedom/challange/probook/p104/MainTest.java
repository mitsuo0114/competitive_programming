package jp.fedom.challange.probook.p104;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.List;

import org.junit.Test;

public class MainTest {

	@Test
	public void test_simple1() {
		int N = 4;
		int ML = 2;
		int MD = 1;
		
		List<int[]> good = new ArrayList<>();
		good.add(new int[]{ 1, 3, 10 });
		good.add(new int[]{ 2, 4, 20 });
				
		List<int[]> bad = new ArrayList<>();
		bad.add(new int[]{ 2, 3, 3 });

		assertThat(Main.solve(N, ML, MD, good, bad), is(27));
	}

	
	@Test
	public void test_simple2() {
		int N = 4;
		int ML = 1;
		int MD = 1;
		
		List<int[]> good = new ArrayList<>();
		good.add(new int[]{ 1, 3, 10 });
				
		List<int[]> bad = new ArrayList<>();
		bad.add(new int[]{ 2, 3, 20 });

		assertThat(Main.solve(N, ML, MD, good, bad), is(-1));
	}

	
	@Test
	public void test_simple3() {
		int N = 4;
		int ML = 1;
		int MD = 1;
		
		List<int[]> good = new ArrayList<>();
		good.add(new int[]{ 1, 3, 10 });
				
		List<int[]> bad = new ArrayList<>();
		bad.add(new int[]{ 1, 2, 10 });

		assertThat(Main.solve(N, ML, MD, good, bad), is(-2));
	}

}
