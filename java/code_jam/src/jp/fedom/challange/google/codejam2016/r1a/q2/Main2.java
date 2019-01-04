package jp.fedom.challange.google.codejam2016.r1a.q2;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
import java.util.TreeMap;

import org.apache.commons.math3.linear.Array2DRowRealMatrix;
import org.apache.commons.math3.linear.LUDecomposition;
import org.apache.commons.math3.linear.MatrixUtils;
import org.apache.commons.math3.linear.RealMatrix;
import org.apache.commons.math3.linear.RealVector;

public class Main2 {

	public static void main(String[] args) {
		start("res/2016_r1_a_q2/test.in", "res/2016_r1_a_q2/output_test.txt");
		start("res/2016_r1_a_q2/test2.in", "res/2016_r1_a_q2/output_test.txt");
		start("res/2016_r1_a_q2/test3.in", "res/2016_r1_a_q2/output_test.txt");
		 start("res/2016_r1_a_q2/B-small-practice.in", "res/2016_r1_a_q2/output_small.txt");
		// start("res/2016_r1_a_q2/A-large.in",
		// "res/2016_r1_a_q1/output_large.txt");
	}

	public static void start(String infile, String outputfile) {
		try {
			// ArrayList<int[][]> questionList;
			// questionList = getQuestions(infile);
			// StringBuilder sb = new StringBuilder();
			// for (int i = 0; i < questionList.size(); i++) {
			// sb.append(solve(i + 1, questionList.get(i))).append("\n");
			// }
			List<RealMatrix> questionList;
			questionList = getQuestions(infile);
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < questionList.size(); i++) {
//				show(questionList.get(i).getData());
				sb.append(solve(i + 1, questionList.get(i))).append("\n");
			}
			System.out.println("ans====");
			System.out.println(sb.toString());
			File file = new File(outputfile);
			file.delete();
			FileWriter filewriter = new FileWriter(file, true);
			filewriter.write(sb.toString());
			filewriter.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public static String solve(int qNum, RealMatrix matrix) {
		sort(matrix);
		show(matrix.getData());
		System.out.println("Group 1--");
		RealMatrix g1 = split(matrix, 0, matrix.getRowDimension()/2 + 1); 
		show(g1.getData());
		RealMatrix g2 = split(matrix, 1, matrix.getRowDimension()/2); 
		RealMatrix tg1 = g1.transpose();
		
		for (int hoge = 0; hoge < 3; hoge++) {
//			System.out.println("Trans Group 1--");
//			show(tg1.getData());

//			System.out.println("Group 2--");
//			show(g2.getData());

			
			Map<Integer, RealVector> unmatchedVectors = findUnmatchedRow(tg1, g2);
			System.out.println("Unmatched");
			show(v2m(unmatchedVectors.values()).getData());

			if (unmatchedVectors.size() == 1) {
				Iterator<Integer> k = unmatchedVectors.keySet().iterator();
				return "Case #" + qNum + ":　" + toS(unmatchedVectors.get(k.next()));
			} else {
				OUT: for (Entry<Integer, RealVector> v : unmatchedVectors.entrySet()) {
					int f = -1;
					for (int i = 0; i < g2.getRowDimension(); i++) {
						if (g2.getRowVector(i).getEntry(0) == v.getValue().getEntry(0)) {
							f = i;
							break;
						}
					}
					if(f > 0){
						System.out.println("Replace Group 1--");
						show(v2m(v.getValue()).getData());
						replace(tg1, v.getKey(), g2, f);
//						System.out.println("Replace Group 1--");
//						show(tg1.getData());
//						System.out.println("Replace Group 2--");
//						show(g2.getData());

						tg1 = tg1.transpose();
						break OUT;
					}
				}
					
					
//					if (matchResult.contains(i) || row == i) {
//						continue;
//					}
//					// System.out.println("replace " + i);
//					replace(transgroup1, group2, i, row);
//					transgroup1 = trans(transgroup1);
//					i += group1.length;
			}
		}
		return "";
	}


	private static String toS(RealVector realVector) {
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i < realVector.getDimension(); i++){
			sb.append((int)realVector.getEntry(i) + " ");
		}
		return sb.toString().trim();
	}

	private static Map<Integer, RealVector> findUnmatchedRow(RealMatrix tg1, RealMatrix g2) {
		Map<Integer, RealVector> r = new TreeMap<>();
		for(int i = 0; i < tg1.getRowDimension(); i++){
			boolean find = false;
			for(int j = 0; j < g2.getRowDimension(); j++){
				if(comp(tg1.getRowVector(i), g2.getRowVector(j)) == 0){
					find = true;
				}
			}
			if(find == false ){
				r.put(i, tg1.getRowVector(i));
			}
		}
		return r;
	}

	private static RealMatrix split(RealMatrix matrix, int mod, int expectedSize) {
		List<RealVector> mat = new ArrayList<RealVector>();
		
		for(int i = 0; i < matrix.getRowDimension(); i++){
			if(i % 2 == mod){
				mat.add(matrix.getRowVector(i));
			}
		}
		return v2m(mat);
		
	}
	
	private static RealMatrix v2m(Collection<RealVector> mat) {
		List<RealVector> l = new ArrayList<RealVector>();
		for(RealVector v : mat){
			l.add(v);
		}
		return v2m(l);
	}
	
	private static RealMatrix v2m(RealVector v) {
		List<RealVector> l = new ArrayList<RealVector>();
		l.add(v);
		return v2m(l);
	}

	private static RealMatrix v2m(List<RealVector> mat) {
		double[][] m = new double[mat.size()][];
		for(RealVector v : mat){
			m[mat.indexOf(v)] = v.toArray();
		}
		return MatrixUtils.createRealMatrix(m);
	}

	private static void sort(RealMatrix matrix) {
		final int rowMax = matrix.getRowDimension();
		for(int i = 0; i < rowMax; i++){
			for(int j = i; j < rowMax; j++){
				if ( comp(matrix.getRowVector(i), matrix.getRowVector(j)) == 1){
					replace(matrix, i , j);
				}
			}
		}
		
		
	}

	private static void replace(RealMatrix matrix, int i, int j) {
		RealVector tmp = matrix.getRowVector(i);
		matrix.setRowVector(i, matrix.getRowVector(j));
		matrix.setRowVector(j, tmp);
		
	}
	private static void replace(RealMatrix g1, int key, RealMatrix g2, int g2key) {
		RealVector tmp = g1.getRowVector(key);
		g1.setRowVector(key, g2.getRowVector(g2key));
		g2.setRowVector(g2key, tmp);
	}


	private static int comp(RealVector rowVector, RealVector rowVector2) {
		for(int i = 0; i < rowVector.getDimension(); i++){
			if(rowVector.getEntry(i) > rowVector2.getEntry(i)){
				return 1;
			}else if (rowVector.getEntry(i) < rowVector2.getEntry(i)){
				return -1;
			}
		}
		return 0;
	}

	public static List<RealMatrix>  getQuestions(String filepath) throws IOException {
		ArrayList<RealMatrix > questionList = new ArrayList<RealMatrix>();

		FileReader f = new FileReader(filepath);
		BufferedReader b = new BufferedReader(f);
		String s;
		b.readLine();// cut header line
		int n = 0;
		double[][] matrixData = null;
		while ((s = b.readLine()) != null) {
			if ((s.split(" ").length) == 1) {
				n = Integer.valueOf(s.split(" ")[0]);
				matrixData = new double[n * 2 - 1][];
				for(int i = 0; i < n * 2 - 1; i++){
					matrixData[i] = new double[n];
				}
			}
			for (int k = 0; k < n * 2 - 1; k++) {
				s = b.readLine();
				String[] l = s.split(" ");
				for(int i = 0; i < l.length; i++){
					matrixData[k][i] = Double.parseDouble(l[i]);
				}
			}
			questionList.add(MatrixUtils.createRealMatrix(matrixData));
		}
		b.close();
		return questionList;
	}
	
	private static void show(double[][] q) {
		for (int i = 0; i < q.length; i++) {
			for (int j = 0; j < q[i].length; j++) {
				System.out.print(String.format("%d",(int)q[i][j]) + " ");
			}
			System.out.println();
		}
	}
	}
