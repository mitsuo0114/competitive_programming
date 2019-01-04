package jp.fedom.challange.google.codejam2016.q.q1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
import jp.fedom.challange.google.common.Utils;

public class MainExecute {

	public static void main(String[] args) {
//		start("res/sheep/test.in", "res/sheep/output_test.txt");
//		start("res/sheep/A-small-attempt0.in", "res/sheep/output_small.txt");
		start("res/2016_q_q1/A-large.in", "res/2016_q_q1/output_large.txt");
	}

	public static void start(String infile, String outputfile) {
		try {
			ArrayList<Long> questionList;
			questionList = getQuestions(infile);
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < questionList.size(); i++) {
				sb.append(solve(i + 1, questionList.get(i))).append("\n");
			}
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

	public static ArrayList<Long> getQuestions(String filepath)
			throws IOException {
		ArrayList<Long> questionList = new ArrayList<Long>();

		FileReader f = new FileReader(filepath);
		BufferedReader b = new BufferedReader(f);
		String s;
		b.readLine();// cut header line
		while ((s = b.readLine()) != null) {
			questionList.add(Long.valueOf(s));
		}
		b.close();
		return questionList;
	}

	public static String solve(int quetionNumber, long question) {
		Set<String> countingSet = new HashSet<String>();

		if(question == 0){
			return "Case #" + quetionNumber + ": INSOMNIA";
		}
		
		long dd = question;
		for (int i = 0; i < 1000; i++) {
			Set<String> p = pickup(dd);
			countingSet.addAll(p);
			if(countingSet.size() == 10){
				return "Case #" + quetionNumber + ": "+ String.valueOf(dd);
			}
			dd += question;
		}
		return "could not solve";

	}

	private static Set<String> pickup(long dd) {
		String dString = String.valueOf(dd);
		Set<String> set = new HashSet<String>();
		for(int i = 0; i < dString.length(); i++){
			set.add(String.valueOf(dString.charAt(i)));
		}
		return set;
	}

	private static void out(double q) {
		System.out.print(q);
	}

}
