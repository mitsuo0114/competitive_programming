package jp.fedom.challange.google.codejam2013v.q1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

import jp.fedom.challange.google.common.Utils;

public class Main {

	public static boolean isMale(){
		boolean aa = true;
		return aa;
	}
	
	public static void main(String[] args) {
		boolean result = isMale();
		if(result){
			System.out.println("true");
		}else{
			System.out.println("false");
		}

		start("res/2013v_q1/A-small-practice.in","res/2013v_q1/output_small.txt");
		start("res/2013v_q1/A-large-practice.in","res/2013v_q1/output_large.txt");
	}
	
	public static void start(String infile, String outputfile){
		try {
			ArrayList<double[]> questionList;
			questionList = getQuestions(infile);
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < questionList.size(); i++) {
				sb.append(solve(i + 1, questionList.get(i))).append("\n");
			}
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

	public static ArrayList<double[]> getQuestions(String filepath)
			throws IOException {
		ArrayList<double[]> questionList = new ArrayList<double[]>();

		FileReader f = new FileReader(filepath);
		BufferedReader b = new BufferedReader(f);
		String s;
		b.readLine();// cut header line
		while ((s = b.readLine()) != null) {
			questionList.add(Utils.convertToDoubleArray(b.readLine(), Integer.valueOf(s)));
		}
		b.close();

		return questionList;
	}

	public static String solve(int quetionNumber, double[] question) {
		System.out.println(Utils.doubleArraytoString(question));
		for (int i = 1; i < question.length - 1; i++) {
			double average = getAverage((double) question[i - 1],
					(double) question[i + 1]);
			if (question[i] > average) {
				question[i] = average;
			}
		}
		System.out.println(Utils.doubleArraytoString(question));
		return "Case #" + quetionNumber + ": "
				+ String.format("%.6f", question[question.length - 2]);
	}



	private static double getAverage(double a, double b) {
		return (a + b) / 2.00000;
	}



}
