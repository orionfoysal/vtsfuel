/**
 * kf_fuel
 */

// import Gaussian.*;

public class Kf_fuel {

    public static void main(String[] args){
        Gaussian obj = new Gaussian();
        obj.setGaussian(12,14);
        int[] a = obj.getGaussian();
        System.out.print(a[0]);
    }
}
