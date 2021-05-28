package BMSStreamSender;

public class BMSSender {

	public static void main(String[] args) {
		
		System.out.println("Please enter number of BMS readings to be generate (Min->10):");
		try {
		String inputGenarateRange = System.console().readLine();
		if(ValidateUserInput.isNumeric(inputGenarateRange)&&ValidateUserInput.isGreaterthanMin(inputGenarateRange))
		{
			System.out.println("You entered string " + Integer.parseInt(inputGenarateRange));
			IBMSService bms_s=new BMSServiceImpl();
			bms_s.genearateBatteryReadings( Integer.parseInt(inputGenarateRange));
			bms_s.printBatteryReadingsToConsole();
		}
		
		}
		catch(NullPointerException e)
		{
			System.out.println(e.getMessage());
		}
		}
		
		
		
	}

