package jp.fedom.challange.probook.p100;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	int[][] w;
	
	@Test
	public void test0() {
		int N = 7;
		w = new int[N][];
		for(int i = 0; i < N; i++){
			w[i] = new int[N];
		}
		
		set('A','C',1);
		set('B','C',2);
		set('B','E',10);
		set('C','D',3);
		set('C','F',7);
		set('D','F',1);
		set('D','G',5);
		set('E','F',5);
		set('F','G',8);
		
		assertThat(Main.solve(N, w), is(17));
	}

	private void set(int i, int j, int k) {
		i -= 'A';
		j -= 'A';
		w[i][j] = k;
		w[j][i] = k;
	}

}
