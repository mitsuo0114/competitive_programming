package jp.fedom.challange.google.common;

import java.util.ArrayList;

public class Utils {

	public static int[] convertToIntArray(String string, int num) {
		int[] returnList = new int[num];
		String[] stringList = string.split(" ");
		for (int i = 0; i < num; i++) {
			returnList[i] = Integer.valueOf(stringList[i]);
		}
		return returnList;
	}
	
	public static String doubleArraytoString(double[] question) {
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < question.length; i++) {
			sb.append(question[i] + " ");
		}
		return sb.toString();
	}
	
	
	
	
	public static String intArraytoString(int[] question) {
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < question.length; i++) {
			sb.append(question[i] + " ");
		}
		return sb.toString();
	}
	
	public static double[] convertToDoubleArray(String string, int num) {
		double[] returnList = new double[num];
		String[] stringList = string.split(" ");
		for (int i = 0; i < num; i++) {
			returnList[i] = Double.valueOf(stringList[i]);
		}
		return returnList;
	}

	public static String[] convertToStringArray(String readLine) {
		String[] read = new String[readLine.length()];
		
		for(int i = 0; i < readLine.length(); i++){
			read[i] = String.valueOf(readLine.charAt(i));
		}
		return read;
	}
}
