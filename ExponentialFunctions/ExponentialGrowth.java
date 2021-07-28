import java.lang.Math;

class ExponentialGrowth {
  public static void main(String[] args) {
    System.out.println(simpleExponentialGrowth(10, 1.1, 2));
    System.out.println(compoundedExponentialGrowth(1200, 0.06, 12, 3));
    System.out.println(compoundedExponentialDecay(4000, 0.025, 12000, 5));
  }

  public static double simpleExponentialGrowth(int initialAmount, double rate, int iterations) {
    return initialAmount * Math.pow(rate, iterations);
  }

  public static double compoundedExponentialGrowth(int initialAmount, double rate, int divisions, int iterations) {
    return initialAmount * Math.pow(1+(rate/divisions), divisions*iterations);
  }

  public static double compoundedExponentialDecay(int initialAmount, double rate, int divisions, int iterations) {
    return initialAmount * Math.pow(1-(rate/divisions), divisions*iterations);
  }
}
