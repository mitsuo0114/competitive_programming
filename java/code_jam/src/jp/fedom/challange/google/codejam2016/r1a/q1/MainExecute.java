package jp.fedom.challange.google.codejam2016.r1a.q1;

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
//		start("res/2016_r1_a_q1/test.in", "res/2016_r1_a_q1/output_test.txt");
		start("res/2016_r1a_q1/A-small-attempt0.in", "res/2016_r1a_q1/output_small.txt");
		start("res/2016_r1a_q1/A-large.in", "res/2016_r1a_q1/output_large.txt");
	}

	public static void start(String infile, String outputfile) {
		try {
			ArrayList<String> questionList;
			questionList = getQuestions(infile);
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < questionList.size(); i++) {
				sb.append(solve(questionList.get(i), i + 1)).append("\n");
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

	public static ArrayList<String> getQuestions(String filepath)
			throws IOException {
		ArrayList<String> questionList = new ArrayList<String>();

		FileReader f = new FileReader(filepath);
		BufferedReader b = new BufferedReader(f);
		String s;
		b.readLine();// cut header line
		while ((s = b.readLine()) != null) {
			questionList.add(s);
		}
		b.close();
		return questionList;
	}

	public static String solve(String st, int qNum) {
		
		StringBuilder sb = new StringBuilder();
		
		for (int i = 0; i < st.length(); i++) {
			if(sb.length() == 0){
				sb.append(String.valueOf(st.charAt(i)));
				continue;
			}
			char first = sb.charAt(0);
			
			if(first > st.charAt(i)){
				sb.append(st.charAt(i));
			}else{
				sb.insert(0, st.charAt(i));
			}
		}
		return 	 "Case #" + qNum + ": "+ sb.toString();
	}


}
