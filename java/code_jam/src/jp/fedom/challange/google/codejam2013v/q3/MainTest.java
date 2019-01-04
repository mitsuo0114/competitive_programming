package jp.fedom.challange.google.codejam2013v.q3;

import static org.junit.Assert.*;

import java.util.ArrayList;

import jp.fedom.challange.google.common.Utils;

import org.junit.Ignore;
import org.junit.Test;
import static org.hamcrest.CoreMatchers.*;

public class MainTest {

	@Test
	public void test_solve_sample1() {
		int[] questionSmall = {1,4,3,3};
		assertEquals("Case #1: 2", Main.solve(1,questionSmall));
	}

	@Test
	public void test_solve_sample2() {
		int[] question= {3,4,6,7,10};
		assertEquals("Case #2: 0", Main.solve(2,question));
	}

	@Test
	public void test_solve_sample3() {
		int[] question = {4,3,2,1};
		assertEquals("Case #3: 3", Main.solve(3,question));
	}

	@Test
	public void test_solve_sample4() {
		int[] question = {4,5,6,1,7};
		assertEquals("Case #4: 1", Main.solve(4,question));
	}

	@Test
	public void createQuestion() throws Exception{
		int[] question = Utils.convertToIntArray("1 2 3 4 5", 5);
		assertThat(question[0], is(1));
		assertThat(question[1], is(2));
		assertThat(question[2], is(3));
		assertThat(question[3], is(4));
		assertThat(question[4], is(5));
	}

	@Test
	public void readfile() throws Exception{
		ArrayList<int[]> questionList = Main.getQuestions("res/oceanview/sample.in");
		assertThat(questionList.get(0), is(new int[]{1,4,3,3}));
		assertThat(questionList.get(1), is(new int[]{3,4,6,7,10}));
		assertThat(questionList.get(2), is(new int[]{4,3,2,1}));
		assertThat(questionList.get(3), is(new int[]{4,5,6,1,7}));
	}
	
	@Test
	public void getBackLower_sample3() throws Exception{
		int[] question =  {4,5,6,1,7};
		assertThat(Main.getBackLower(0, question),is(1));
		assertThat(Main.getBackLower(1, question),is(1));
		assertThat(Main.getBackLower(2, question),is(1));
		assertThat(Main.getBackLower(3, question),is(0));
		assertThat(Main.getBackLower(4, question),is(0));
	}
	@Test
	public void getBackLower_equals() throws Exception{
		int[] question =  {4,4,4,4,4};
		assertThat(Main.getBackLower(0, question),is(4));
		assertThat(Main.getBackLower(1, question),is(3));
		assertThat(Main.getBackLower(2, question),is(2));
		assertThat(Main.getBackLower(3, question),is(1));
		assertThat(Main.getBackLower(4, question),is(0));
	}

	@Test
	public void frontHeighter_sample3() throws Exception{
		int[] question =  {4,5,6,1,7};
		assertThat(Main.getFrontHigher(0, question),is(0));
		assertThat(Main.getFrontHigher(1, question),is(0));
		assertThat(Main.getFrontHigher(2, question),is(0));
		assertThat(Main.getFrontHigher(3, question),is(3));
		assertThat(Main.getFrontHigher(4, question),is(0));
	}
	@Test
	public void frontHeighter_equals() throws Exception{
		int[] question =  {4,4,4,4,4};
		assertThat(Main.getFrontHigher(0, question),is(0));
		assertThat(Main.getFrontHigher(1, question),is(1));
		assertThat(Main.getFrontHigher(2, question),is(2));
		assertThat(Main.getFrontHigher(3, question),is(3));
		assertThat(Main.getFrontHigher(4, question),is(4));
	}

	@Test
	public void getBackLowerInvalidate_sample3() throws Exception{
		int[] question =  {4,5,6,-1,7};
		assertThat(Main.getBackLower(0, question),is(0));
		assertThat(Main.getBackLower(1, question),is(0));
		assertThat(Main.getBackLower(2, question),is(0));
		assertThat(Main.getBackLower(3, question),is(0));
		assertThat(Main.getBackLower(4, question),is(0));
	}
	@Test
	public void getBackLowerInvalidate_equals() throws Exception{
		int[] question =  {-1,4,-1,-1,-1};
		assertThat(Main.getBackLower(0, question),is(0));
		assertThat(Main.getBackLower(1, question),is(0));
		assertThat(Main.getBackLower(2, question),is(0));
		assertThat(Main.getBackLower(3, question),is(0));
		assertThat(Main.getBackLower(4, question),is(0));
	}

	@Test
	public void frontHeighterInvalidate_sample3() throws Exception{
		int[] question =  {-1,5,6,1,7};
		assertThat(Main.getFrontHigher(0, question),is(0));
		assertThat(Main.getFrontHigher(1, question),is(0));
		assertThat(Main.getFrontHigher(2, question),is(0));
		assertThat(Main.getFrontHigher(3, question),is(2));
		assertThat(Main.getFrontHigher(4, question),is(0));
	}
	@Test
	public void frontHeighterInvalidate_equals() throws Exception{
		int[] question =  {-1,-1,-1,-1,4};
		assertThat(Main.getFrontHigher(0, question),is(0));
		assertThat(Main.getFrontHigher(1, question),is(0));
		assertThat(Main.getFrontHigher(2, question),is(0));
		assertThat(Main.getFrontHigher(3, question),is(0));
		assertThat(Main.getFrontHigher(4, question),is(0));
	}
	@Test
	public void getMaxIndex_1() throws Exception{
		int[] front =  {0,0,3,0,0};
		int[] back  =  {0,0,3,0,0};
		assertThat(Main.getMaxIndex(front, back), is(2));
		assertThat(Main.getMax(front, back), is(6));
	}
	@Test
	public void getMaxIndex_2() throws Exception{
		int[] front =  {0,0,3,0,0};
		int[] back  =  {5,0,0,0,0};
		assertThat(Main.getMaxIndex(front, back), is(0));
		assertThat(Main.getMax(front, back), is(5));
	}
	@Test
	public void getMaxIndex_3() throws Exception{
		int[] front =  {0,0,3,0,6};
		int[] back  =  {5,0,0,0,0};
		assertThat(Main.getMaxIndex(front, back), is(4));
		assertThat(Main.getMax(front, back), is(6));
	}
	@Test
	public void getMaxIndex_4() throws Exception{
		int[] front =  {0,0,0,0,0};
		int[] back  =  {0,0,0,0,0};
		assertThat(Main.getMaxIndex(front, back), is(0));
		assertThat(Main.getMax(front, back), is(0));
	}
	@Test
	public void choice_1() throws Exception{
		int[] question =  {1,-1,3,3};
		assertThat(Main.choice(question), is(2));
	}

	@Test
	public void choice_2() throws Exception{
		int[] question =  {1,-1,-1,3};
		assertThat(Main.choice(question), is(-1));
	}

}
