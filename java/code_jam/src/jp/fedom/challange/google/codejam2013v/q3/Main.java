package jp.fedom.challange.google.codejam2013v.q3;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

import jp.fedom.challange.google.common.Utils;

public class Main {

	public static void main(String[] args) {

		start("res/2013v_q3/C-small-practice.in","res/2013v_q3/output_small.txt");
		start("res/2013v_q3/C-large-practice.in","res/2013v_q3/output_large.txt");
	}
	
	static int INVALIDATE = -1;

	public static void start(String infile, String outputfile) {
		try {
			ArrayList<int[]> questionList;
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
			e.printStackTrace();
		}
	}

	public static ArrayList<int[]> getQuestions(String filepath)
			throws IOException {
		ArrayList<int[]> questionList = new ArrayList<int[]>();

		FileReader f = new FileReader(filepath);
		BufferedReader b = new BufferedReader(f);
		String s;
		
		b.readLine();// cut header line
		while ((s = b.readLine()) != null) {
			questionList.add(Utils.convertToIntArray(b.readLine(),
					Integer.valueOf(s)));
		}
		b.close();

		return questionList;
	}

	public static String solve(int quetionNumber, int[] question) {
		System.out.println("Start  : " +  Utils.intArraytoString(question));
		int count = 0;

		while (true) {
			int i = choice(question);

			if (i == INVALIDATE) {
				break;
			} else {
				question[i] = INVALIDATE;
				count++;
			}
		}
		
		System.out.println("finish  : " +  Utils.intArraytoString(question));
		return "Case #" + quetionNumber + ": "	+ String.format("%d", count);
	}
	
	
	public static int choice(int[] question) {
		int[] frontScore = new int[question.length];
		int[] backScore = new int[question.length];
		for (int i = 0; i < question.length ; i++) {
			if(question[i] != INVALIDATE){
			frontScore[i] = getFrontHigher(i, question);
			backScore[i]  = getBackLower(i,question);
			}
		}
		System.out.println(Utils.intArraytoString(question));
		System.out.println(Utils.intArraytoString(frontScore));
		System.out.println(Utils.intArraytoString(backScore));
		System.out.println();
		int max = getMax(frontScore, backScore);
		int maxindex = getMaxIndex(frontScore, backScore);
		return max == 0 ? INVALIDATE : maxindex;
	}
	
	public static int getMaxIndex(int[] front, int[] back){
		int max = 0;
		int returnindex = 0;
		for (int i = 0; i < front.length ; i++) {
			if(max <= front[i] + back[i]){
				max = front[i] + back[i];
				returnindex = i;
			}
		}
		return returnindex;
	}
	
	public static int getMax(int[] front, int[] back){
		int index = getMaxIndex(front, back); 
		return front[index] + back[index];
	}
	

	public	static int getBackLower(int i, int[] question) {
		int self = question[i];
		int count = 0;
		for(int j = i + 1; j < question.length; j++){
			if(question[j] != INVALIDATE && question[j] <= self){
				count++;
			}
		}
		return count;
	}

	public static int getFrontHigher(int i, int[] question) {
		int self = question[i];
		int count = 0;
		for(int j = i - 1; j >= 0; j--){
			if(question[j] != INVALIDATE && self <= question[j] ){
				count++;
			}
		}
		return count;
	}

}
