package jp.fedom.challange.probook.p23;

import java.util.List;


public class Main {

	public static String solve(List<Long> numbers, long l, long n) {
		long min = Long.MIN_VALUE;
		long max = Long.MIN_VALUE;
		
		for(long nn : numbers){
			long leftTime = nn;
			long rightTime = l - nn;
			min = Math.max(Math.min(leftTime, rightTime), min);
			max = Math.max(Math.max(leftTime, rightTime), max);
		}
		
		return min + " " + max;
	}
}
	