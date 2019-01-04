package jp.fedom.challange.google.codejam2016.q.q2;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import jp.fedom.challange.google.common.Utils;

public class MainExecute {

	public static void main(String[] args) {
		start("res/2016_q_q2/B-small-attempt2.in", "res/2016_q_q2/output_small.txt");
		start("res/2016_q_q2/B-large.in", "res/2016_q_q2/output_large.txt");
	}

	public static void start(String infile, String outputfile) {
		try {
			ArrayList<String[]> questionList;
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

	public static ArrayList<String[]> getQuestions(String filepath)
			throws IOException {
		ArrayList<String[]> questionList = new ArrayList<String[]>();

		FileReader f = new FileReader(filepath);
		BufferedReader b = new BufferedReader(f);
		String s;
		b.readLine();// cut header line
		while ((s = b.readLine()) != null) {
			questionList.add(Utils.convertToStringArray(s));
		}
		b.close();

		return questionList;
	}

	public static String solve(int quetionNumber, String[] question) {
		ArrayList<String> q = new ArrayList<>();
		out(question);
		for (int i = 0; i < question.length; i++) {
			q.add(question[i]);
		}
		int turnOvercount = 0;

		for (int i = 0; i < 1000; i++) {
			int lastBlankIndex = findBlank(q);
			if (lastBlankIndex == -1) {
				System.out.print(quetionNumber + " " + turnOvercount);
				return "Case #" + quetionNumber + ": "
						+ String.format("%d", turnOvercount);
			} else {
				q = turnover(q, lastBlankIndex);
				turnOvercount++;
			}
		}
		return "could not solve";

	}

	private static ArrayList<String> turnover(ArrayList<String> q,
			int lastBlankIndex) {
		ArrayList<String> newList = new ArrayList<String>();
//		System.out.println("turnover to " + lastBlankIndex);
//		out(q);
		for(int i = 0; i < q.size(); i++){
			if(i > lastBlankIndex){
				newList.add(q.get(i));
			}else{
				newList.add(reverse(q.get(i)));
			}
			
		}
//		out(newList);
		return newList;
	}

	private static String reverse(String c) {
		if(c.equals("-")){
			return "+";
		}else if(c.equals("+")){
			return "-";
		}
		throw new IllegalArgumentException("don't input " + c);
	}

	private static void out(String[]     q) {
		for(String c : q ){
			System.out.print(c);
		}
		System.out.println();
	}
	private static int findBlank(ArrayList<String> q) {
		return q.lastIndexOf("-");
	}

}
