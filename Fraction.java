//Phil Prosapio Andrew ID: pprosapi
package lab3;

public class Fraction {
	protected int numerator;
	protected int denominator;
	
	public Fraction() {
		numerator = 1;
		denominator = 1;
	}
	
	public Fraction(int numerator, int denominator) {
		this.numerator = numerator;
		this.denominator = denominator;
	}
	
	public String toString() {
		return numerator + "/" + denominator;
	}
	
	public double toDecimal() {
		double div = numerator / (double) denominator;
		return div;
	}
	
	public Fraction add(Fraction f) {
		int aNum = this.numerator*f.denominator + f.numerator*this.denominator;
		int aDen = this.denominator*f.denominator;
		int gcd = findGCD(aNum, aDen);
		if(gcd != 0) {
			aNum = aNum / gcd;
			aDen = aDen / gcd;
		}
		Fraction retFrac = new Fraction();
		retFrac.denominator = aDen;
		retFrac.numerator = aNum;
		return retFrac;
	}
	
	public int findGCD(int numerator, int denominator) {
		if(numerator == 1) {
			return 1;
		}else if(denominator == 0) {
			return numerator;
		}else {
			int num = findGCD(denominator, numerator % denominator);
			return num;
		}
	}
}
