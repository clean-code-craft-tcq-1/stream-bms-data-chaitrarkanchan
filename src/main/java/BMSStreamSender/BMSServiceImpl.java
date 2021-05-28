package BMSStreamSender;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class BMSServiceImpl implements IBMSService {
	 Random random = new Random();
	 List<BMSFactors> paramValReading = new ArrayList<BMSFactors>();
	 public static double MaxTemperature = 40;
     public static double MinTemperature = 0;
     public static double MaxSoc = 80;
     public static double MinSoc = 20;
	
	@Override
	public List<BMSFactors> genearateBatteryReadings(int streamcount) {
		// TODO Auto-generated method stub
		
		
		while(streamcount!=0) {
			double Temperature=Math.round(getRandom(MaxTemperature,MinTemperature));
			double Soc=Math.round(getRandom(MaxSoc,MinSoc));
			paramValReading.add(new BMSFactors(Temperature,Soc));
			streamcount--;
		}

		return paramValReading;
	}
	

	@Override
	public void printBatteryReadingsToConsole() {
		 System.out.println("Temperature , SOC \n");
		for(BMSFactors paramval : paramValReading)
        {
            System.out.println(paramval.Temperature + "," + paramval.StateOfCharge);
        }

	}

	private double getRandom(double min, double max) {
		 double range = max - min;
		  double scaled = random.nextDouble() * range;
		  double shifted = scaled + min;
		  return shifted;
	}
	

	
}
