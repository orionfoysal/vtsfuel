/**
 * gaussian
 */ 
public class Gaussian {
    private int mean;
    private int var;

    public void setGaussian(int mean, int var) {
        this.mean = mean;
        this.var = var;
    }
    public int[] getGaussian() {
        int[] gauss = new int[2];
        gauss[0] = this.mean;
        gauss[1] = this.var;
        return gauss;
    }   
}
