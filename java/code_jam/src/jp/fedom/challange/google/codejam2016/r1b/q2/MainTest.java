package jp.fedom.challange.google.codejam2016.r1b.q2;

import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.HashSet;

import jp.fedom.challange.google.codejam2016.r1b.q2.Main.Question;
import jp.fedom.challange.google.common.Utils;

import org.apache.commons.math3.geometry.spherical.oned.ArcsSet.Split;
import org.junit.Before;
import org.junit.Ignore;
import org.junit.Test;
import static org.hamcrest.CoreMatchers.*;

@Ignore
public class MainTest {

	Question q;

	@Before
	public void setup(){
		q = new Question();
	}

	
	@Test
	public void test_solve() {
		Question q = new Question();
		q.first  = "1?0";
		q.second = "?9?";
		assertThat(Main.solve(q, 1), is(Main.solve2(q, 1)));
	}
	

	@Test
	public void test_solve_testadd2() {
		Question q = new Question();
		q.first  = "100";
		q.second = "?50";
		assertThat(Main.solve(q, 1), is(Main.solve2(q, 1)));
	}
	
	@Test
	public void test_solve_testadd1() {
		Question q = new Question();
		q.first  = "?50";
		q.second = "1?0";
		assertThat(Main.solve(q, 1), is(Main.solve2(q, 1)));
	}
	
	@Test
	public void test_solve_sampleset1() {
		String[] f = new String[]{"1?", "?1","2?", "?2",};
		for(String ff : f){
			for(String ss : f){
				q.first =  ff;
				q.second = ss;
				assertThat(Main.solve(q, 1), is(Main.solve2(q, 1)));
			}
		}
	}
	
	@Test
	public void test_solve_sampleset1_a() {
		String[] f = new String[]{"1??", "1?9", "1??",};
		for(String ff : f){
			for(String ss : f){
				q.first =  ff;
				q.second = ss;
				assertThat(Main.solve(q, 1), is(Main.solve2(q, 1)));
			}
		}
	}
	
	@Test
	public void test_solve_sampleset2() {
		String[] all = new String[11];
		String[] f = new String[11 * 11 * 11];
		for(int i1 = 0; i1 < 11; i1++){
			String s1 = i1 == 10 ? "?" : String.valueOf(i1);
			for(int i2 = 0; i2 < 11; i2++){
				String s2 = i2 == 10 ? "?" : String.valueOf(i2);
				for(int i3 = 0; i3 < 11; i3++){
					String s3 = i3 == 10 ? "?" : String.valueOf(i3);
					f[i3 * 11 * 11 + i2 * 11 + i1] = s1 + s2 + s3;
				}
			}
		}
		
		for(String ff : f){
			for(String ss : f){
				q.first =  ff;
				q.second = ss;
				System.out.println(ff + " / " + ss);
				assertThat(Main.solve(q, 1), is(Main.solve2(q, 1)));
			}
		}
	}


	@Test
	public void test_solve_sample2() {
		String[] f = new String[]{"10?00", "10?30", "10?99", "20?00", "20300", "20?99"};
		for(String ff : f){
			for(String ss : f){
				q.first =  ff;
				q.second = ss;
				assertThat(Main.solve2(q, 1), is(Main.solve(q, 1)));
			}
		}
	}
	@Test
	public void test_solve_sample2_() {
		String[] f = new String[]{"10?0?", "10?3?", "10?9?", "20?0?", "2030?", "20?9?",
				"?0?0?", "?0?3?", "?0?9?", "?0?0?", "?030?", "?0?9?",};
		for(String ff : f){
			for(String ss : f){
				q.first =  ff;
				q.second = ss;
				assertThat(Main.solve2(q, 1), is(Main.solve(q, 1)));
			}
		}
	}

	@Test
	public void test_solve_sample3() {
		q.first =  "10?99";
		q.second = "10?00";
		assertThat(Main.solve2(q, 1), is(Main.solve(q, 1)));
		swap(q);
		assertThat(Main.solve2(q, 1), is(Main.solve(q, 1)));
	}

	@Test
	public void test_solve_sample4() {
		q.first =  "20?00";
		q.second = "10?00";
		assertThat(Main.solve(q, 1), is(Main.solve2(q, 1)));
		swap(q);
		assertThat(Main.solve(q, 1), is(Main.solve2(q, 1)));
	}


	@Test
	public void test_solve_sample5() {
		q.first =  "1?9";
		q.second = "0?9";
		assertThat(Main.solve(q, 1), is(Main.solve2(q, 1)));
		swap(q);
		assertThat(Main.solve(q, 1), is(Main.solve2(q, 1)));
	}


	@Test
	public void test_solve_sample6() {
		q.first =  "1?6";
		q.second = "0?9";
		assertThat(Main.solve(q, 1), is(Main.solve2(q, 1)));
		swap(q);
		assertThat(Main.solve(q, 1), is(Main.solve2(q, 1)));
	}

	
	
	
	@Test
	public void test_solve2_sample1() {
		Question q = new Question();
		q.first = "1?";
		q.second = "2?";
		assertEquals("Case #1: 19 20", Main.solve2(q, 1));
	}

	@Test
	public void test_solve2_sample1_1() {
		Question q = new Question();
		q.first = "2?";
		q.second = "1?";
		assertEquals("Case #1: 20 19", Main.solve2(q, 1));
	}

	@Test
	public void test_solve2_sample2() {
		Question q = new Question();
		q.first = "?";
		q.second = "?";
		assertEquals("Case #1: 0 0", Main.solve2(q, 1));
	}

	@Test
	public void test_solve2_sample3() {
		Question q = new Question();
		q.first = "?2?";
		q.second = "??3";
		assertEquals("Case #1: 023 023", Main.solve2(q, 1));
	}

	@Test
	public void test_solve2_sample4() {
		Question q = new Question();
		q.first = "?5";
		q.second = "?0";
		assertEquals("Case #1: 05 00", Main.solve2(q, 1));
	}

	@Test
	public void test_solve2_sample5() {
		Question q = new Question();
		q.first = "6?1";
		q.second = "759";
		assertEquals("Case #1: 691 759", Main.solve2(q, 1));
	}

	@Test
	public void test_solve2_sample6() {
		Question q = new Question();
		q.first = "759";
		q.second = "6?1";
		assertEquals("Case #1: 759 691", Main.solve2(q, 1));
	}

	@Test
	public void test_solve2_sample7() {
		Question q = new Question();
		q.first = "6??1";
		q.second = "7588";
		assertEquals("Case #1: 6991 7588", Main.solve2(q, 1));
	}

	@Test
	public void test_solve2_sample8() {
		Question q = new Question();
		q.first = "72?";
		q.second = "?98";
		assertEquals("Case #1: 720 698", Main.solve2(q, 1));
	}

	@Test
	public void test_solve2_sample9() {
		Question q = new Question();
		q.first = "1700";
		q.second = "1?99";
		assertEquals("Case #1: 1700 1699", Main.solve2(q, 1));
	}

	@Test
	public void test_solve2_sample10() {
		Question q = new Question();
		q.first = "2700";
		q.second = "2?99";
		assertEquals("Case #1: 2700 2699", Main.solve2(q, 1));
	}

	@Test
	public void test_solve2_sample11() {
		Question q = new Question();
		q.first = "1700";
		q.second = "1?00";
		assertEquals("Case #1: 1700 1700", Main.solve2(q, 1));
	}

	@Test
	public void test_solve2_sample12() {
		Question q = new Question();
		q.first = "2700";
		q.second = "2?50";
		assertEquals("Case #1: 2700 2650", Main.solve2(q, 1));
	}

	@Test
	public void test_solve2_my1() {
		Question q = new Question();
		q.first = "2?";
		q.second = "2?";
		assertEquals("Case #1: 20 20", Main.solve2(q, 1));
	}

	@Test
	public void test_solve2_my2() {
		Question q = new Question();
		q.first = "1?0";
		q.second = "20?";
		assertEquals("Case #1: 190 200", Main.solve2(q, 1));
	}

	@Test
	public void test_solve2_my2__() {
		Question q = new Question();
		q.first = "1?0";
		q.second = "10?";
		assertEquals("Case #1: 100 100", Main.solve2(q, 1));
	}

	@Test
	public void test_solve2_my2_2() {
		Question q = new Question();
		q.first = "20?";
		q.second = "1?0";
		assertEquals("Case #1: 200 190", Main.solve2(q, 1));
	}

	@Test
	public void test_solve2_my3() {
		Question q = new Question();
		q.first = "1??";
		q.second = "2??";
		assertEquals("Case #1: 199 200", Main.solve2(q, 1));
	}

	@Test
	public void test_solve2_my4() {
		Question q = new Question();
		q.first = "1??8?";
		q.second = "2??8?";
		assertEquals("Case #1: 19989 20080", Main.solve2(q, 1));
	}

	@Test
	public void test_solve2_my5() {
		Question q = new Question();
		q.first = "22";
		q.second = "23";
		assertEquals("Case #1: 22 23", Main.solve2(q, 1));
	}

	@Test
	public void test_split() {
		assertThat(Main.split("?").size(), is(10));
	}

	@Test
	public void test_split2() {
		assertThat(Main.split("1?").size(), is(10));
	}

	@Test
	public void test_split3() {
		assertThat(Main.split("?8").size(), is(10));
	}

	@Test
	public void test_split4() {
		assertThat(Main.split("??").size(), is(100));
	}
	
	@Test
	public void test_fill1() {
		assertThat(Main.fill("103??",3,"9"), is("10399"));
	}


	private void swap(Question q2) {
		String s = q.first;
		q.first = q.second;
		q.second = s;
	}

}
