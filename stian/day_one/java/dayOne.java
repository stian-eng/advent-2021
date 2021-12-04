package stian.day_one.java;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class dayOne {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner s = new Scanner(new File("day_one.txt"));
        ArrayList<String> list = new ArrayList<String>();
        while (s.hasNext()){
            list.add(s.next());
        }
        s.close();
        System.out.println("Part One: " + partOne(list));
        System.out.println("Part TWo: " + partTwo(list));
    }

    public static int partOne(ArrayList<String> data) {
        int prev = Integer.parseInt(data.get(0));
        int counter = 0;
        for (int i = 0; i < data.size(); i++) {
            int curr = Integer.parseInt(data.get(i));
            if (curr > prev) {
                counter++;
            }
        }
        return counter;
    }

    public static int partTwo(ArrayList<String> data) {
        int curr = 0;
        int prev = 0;
        int counter = 0;
        for (int i = 0; i < data.size(); i++) {
            curr += Integer.parseInt(data.get(i));
            if (i > 2) {
                if (curr > prev) {
                    counter++;
                }
                prev = curr;
                curr -= Integer.parseInt(data.get(i-2));
            }
        }
        return counter;
    }
}
