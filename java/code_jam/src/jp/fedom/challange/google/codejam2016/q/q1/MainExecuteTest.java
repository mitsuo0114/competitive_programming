package jp.fedom.challange.google.codejam2016.q.q1;

import static org.junit.Assert.*;

import java.util.ArrayList;
import jp.fedom.challange.google.common.Utils;

import org.junit.Test;
import static org.hamcrest.CoreMatchers.*;

public class MainExecuteTest {

	@Test
	public void test_solve_sample1() {
		long question = 0L;
		assertEquals("Case #1: INSOMNIA", MainExecute.solve(1,question));
	}

	@Test
	public void test_solve_sample2() {
		long question = 1L;
		assertEquals("Case #2: 10", MainExecute.solve(2,question));
	}

	@Test
	public void test_solve_sample3() {
		long question = 2L;
		assertEquals("Case #3: 90", MainExecute.solve(3,question));
	}

	@Test
	public void test_solve_sample4() {
		long question = 11L;
		assertEquals("Case #4: 110", MainExecute.solve(4,question));
	}

	@Test
	public void test_solve_sample5() {
		long question = 1692L;
		assertEquals("Case #5: 5076", MainExecute.solve(5,question));
	}
//	}
//
//	@Test
//	public void test_solve_sample6() {
//		double[] question = {1,2,2,2,2,2};
//		assertEquals("Case #6: 1.937500", MainExecute.solve(6,question));
//	}
//
//	@Test
//	public void createQuestion() throws Exception{
//		double[] question = Utils.convertToDoubleArray("1 2 3 4 5", 5);
//		assertThat(question[0], is(1.0));
//		assertThat(question[1], is(2.0));
//		assertThat(question[2], is(3.0));
//		assertThat(question[3], is(4.0));
//		assertThat(question[4], is(5.0));
//	}
//
//	@Test
//	public void readfile() throws Exception{
//		ArrayList<double[]> questionList = MainExecute.getQuestions("res/hedgemony/sample.in");
//		assertThat(questionList.get(0), is(new double[]{1.0,2.0,3.0,6.0,7.0}));
//		assertThat(questionList.get(1), is(new double[]{1.0,2.0,3.0,4.0,7.0}));
//		assertThat(questionList.get(2), is(new double[]{7.0,7.0,7.0}));
//		assertThat(questionList.get(3), is(new double[]{7.0,8.0,7.0,9.0,9.0}));
//		assertThat(questionList.get(4), is(new double[]{5.0,8.0,9.0,9.0,9.0}));
//		assertThat(questionList.get(5), is(new double[]{1.0,2.0,2.0,2.0,2.0,2.0}));
//	}
}
