package jp.fedom.challange.google.codejam2016.r1a.q2;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

public class Main {

	public static void main(String[] args) {
		start("res/2016_r1a_q2/test.in", "res/2016_r1a_q2/output_test.txt");
		start("res/2016_r1a_q2/B-small-practice.in", "res/2016_r1a_q2/output_small.txt");
		start("res/2016_r1a_q2/B-large-practice.in", "res/2016_r1a_q2/output_large.txt");
	}

	public static void start(String infile, String outputfile) {
		try {
			ArrayList<List<String>> questionList;
			questionList = getQuestions(infile);
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < questionList.size(); i++) {
				sb.append(solve(i + 1, questionList.get(i))).append("\n");
			}
			System.out.println(sb);
			File file = new File(outputfile);
			file.delete();
			FileWriter filewriter = new FileWriter(file, true);
			filewriter.write(sb.toString());
			filewriter.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static String solve(int qnum, List<String> list) {
		Map<String, Integer> m = new HashMap<>();
		for(String l : list){
			if(l == null){ continue; }
			String[] ll = l.split(" ");
			for(String s : ll){
				if(m.containsKey(s)){
					m.put(s, m.get(s) + 1);
				}else{
					m.put(s, 1);
				}
			}
		}
		
		List<Integer> find = find(m);
		StringBuilder sb = new StringBuilder();
		for (Integer l : find) {
			sb.append(l + " ");
		}
		return "Case #" + qnum + ": " + sb.toString().trim();
	}

	private static List<Integer> find(Map<String, Integer> m) {
		List<Integer> l = new ArrayList<>();
		for(Entry<String, Integer>  e : m.entrySet()){
			if(e.getValue() % 2 == 1){
				l.add(Integer.valueOf(e.getKey()));
			}
		}
		Collections.sort(l);
		return l;
	}


	public static ArrayList<List<String>> getQuestions(String filepath) throws IOException {
		ArrayList<List<String>> questionList = new ArrayList<List<String>>();

		FileReader f = new FileReader(filepath);
		BufferedReader b = new BufferedReader(f);
		String s;
		b.readLine();// cut header line
		int n = 0;
		while ((s = b.readLine()) != null) {
			if ((s.split(" ").length) == 1) {
				n = Integer.valueOf(s) * 2 - 1;
			}
			List<String> q = new ArrayList<String>();

			for (int k = 0; k < n; k++) {
				q.add(b.readLine());
			}
			questionList.add(q);
		}
		b.close();
		return questionList;
	}
}
