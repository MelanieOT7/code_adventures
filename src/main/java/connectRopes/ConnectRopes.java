package connectRopes;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class ConnectRopes {

    public static int findMinCost(Integer[] ropes) {
        Arrays.sort(ropes);
        ArrayList<Integer> new_ropes = new ArrayList<>(Arrays.asList(ropes));

        int sum = 0;

        while(new_ropes.size() > 1 ){
            int num =  new_ropes.get(0) + new_ropes.get(1);
            sum+=num;
            new_ropes.remove(1);
            new_ropes.remove(0);
            new_ropes.add(num);

            Collections.sort(new_ropes);
        }


        return sum;
    }

    public static void main(String[] args) {
        Integer[] ropes1 = {4, 3, 2, 6};
        System.out.println("Minimum cost is: " + findMinCost(ropes1)); // should print 29

    }
}
