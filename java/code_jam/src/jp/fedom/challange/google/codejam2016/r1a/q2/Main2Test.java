package jp.fedom.challange.google.codejam2016.r1a.q2;

import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.List;

import org.apache.commons.math3.linear.MatrixUtils;
import org.junit.Test;

public class Main2Test {

	@Test
	public void test_solve_sample1() {
		double[][] m = { 
				{ 1, 2, 3 }, 
				{ 2, 3, 5 }, 
				{ 3, 5, 6 }, 
				{ 2, 3, 4 }, 
				{ 1, 2, 3 }, };
		assertEquals("Case #1:　3 4 6", Main2.solve(1,MatrixUtils.createRealMatrix(m)));
	}

	@Test
	public void test_solve_sample2() {
		double[][] m = { 
				{ 1, 2, 3 }, 
				{ 2, 3, 5 }, 
				{ 3, 5, 6 }, 
				{ 3, 4, 6 }, 
				{ 2, 3, 4 }, 
				 };
		assertEquals("Case #1:　1 2 3", Main2.solve(1,MatrixUtils.createRealMatrix(m)));
	}

	
	@Test
	public void test_solve_sample3() {
		double[][] m = { {11,14,16,22},
		{3,6,9,11},
		{6,7,11,14},
		{9,11,15,19},
		{10,11,19,22},
		{6,7,10,11},
		{3,6,8,10},};
		
		assertEquals("Case #1:　8 10 15 16", Main2.solve(1,MatrixUtils.createRealMatrix(m)));
	}

	@Test
	public void test_solve_sample4() {
		double[][] m = { 
		{22,22 }, 
		{2,22 }, 
		{2,22 },  };
		
		assertEquals("Case #1:　22 22", Main2.solve(1,MatrixUtils.createRealMatrix(m)));
	}
	
	@Test
	public void test_solve_sample5() {
		double[][] m = { 
				{4,9,13,16,17,18,28},
				{1,2,3,4,5,6,23},
				{23,25,26,29,30,32,34},
				{6,11,15,18,20,21,33},
				{3,8,12,13,14,15,27},
				{1,2,3,4,5,6,22},
				{6,11,15,18,20,21,32},
				{2,7,8,9,10,11,24},
				{5,10,14,17,19,20,31},
				{5,10,14,17,19,20,30},
				{2,7,8,9,10,11,25},
				{22,24,27,28,31,33,34},
				{4,9,13,16,17,18,29},
			};
		
		assertEquals("Case #1:　22 22", Main2.solve(1,MatrixUtils.createRealMatrix(m)));
	}
	
}
