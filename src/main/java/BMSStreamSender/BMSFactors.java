package BMSStreamSender;

public class BMSFactors {
	public double Temperature;
    public double StateOfCharge;
    
    public BMSFactors(double temperature, double soc)
    {
        this.Temperature = temperature;
        this.StateOfCharge = soc;
    }
}
