package jp.fedom.challange.probook.p99;

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
		
		set('A','B',2);
		set('A','C',5);
		set('B','C',4);
		set('B','D',6);
		set('B','E',10);
		set('C','D',2);
		set('D','F',1);
		set('E','F',3);
		set('E','G',5);
		set('F','G',9);
		
		assertThat(Main.solve(N, w, 'A', 'G'), is(16));
		assertThat(Main.path('A', 'G'), is("ACDFEG"));
	}

	private void set(int i, int j, int k) {
		i -= 'A';
		j -= 'A';
		w[i][j] = k;
		w[j][i] = k;
	}

}
