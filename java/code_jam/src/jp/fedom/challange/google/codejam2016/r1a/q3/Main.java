package jp.fedom.challange.google.codejam2016.r1a.q3;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import jp.fedom.challange.google.common.Utils;

public class Main {

	public static void main(String[] args) {
		start("res/2016_r1_a_q3/test.in", "res/2016_r1_a_q3/output_test.txt");
//		start("res/sheep/A-small-attempt0.in", "res/sheep/output_small.txt");
//		start("res/sheep/A-large.in", "res/sheep/output_large.txt");
	}

	public static void start(String infile, String outputfile) {
		try {
			 ArrayList<List<Integer>>  questionList;
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

	public static ArrayList<List<Integer>> getQuestions(String filepath)
			throws IOException {
		ArrayList<List<Integer>> questionList = new ArrayList<List<Integer>>();

		FileReader f = new FileReader(filepath);
		BufferedReader b = new BufferedReader(f);
		String s;
		b.readLine();// cut header line
		List<Integer> q = null;
		while ((s = b.readLine()) != null) {
			if (s.length() == 1) {
				q = new ArrayList<Integer>(); 
				continue; // headers
			}
			String[] ss = s.split(" ");
			
			for(int k = 0; k < ss.length; k++){ 
				q.add(Integer.valueOf(ss[k]));
			}
			questionList.add(q);
		}
		b.close();
		return questionList;
	}

	public static String solve(int quetionNumber, List<Integer> list) {
		Set<String> countingSet = new HashSet<String>();
		int max = 3;
		
		int[] direction = new int[list.size()];
		for(int k = 0; k < list.size(); k++){
			direction[k] = list.get(k);
		}
		for(int n = list.size(); n > 3; n++){
			if(check(direction, list, n)){
				max = Math.max(max, n);
			}
		}
		
		return "Case #" + quetionNumber + ": " + max;

	}

	// n人で組めるか判定
	private static boolean check(int[] direction, List<Integer> list, int n) {
		for(int start = 0; start < list.size(); start++){
			
		}
		return true;
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
