package BMSStreamSender;

public class BMSSender {

	public static void main(String[] args) {
		while(true) {
		System.out.println("Please enter number of BMS readings to be generate (Min->10):");
		try {
		String inputGenarateRange = System.console().readLine();
		if(inputGenarateRange.contentEquals("x"))
		{
			break;
		}
		
		if(ValidateUserInput.isNumeric(inputGenarateRange)&&ValidateUserInput.isGreaterthanMin(inputGenarateRange))
		{
			System.out.println("You entered string " + Integer.parseInt(inputGenarateRange));
			IBMSService bms_s=new BMSServiceImpl();
			bms_s.genearateBatteryReadings( Integer.parseInt(inputGenarateRange));
			bms_s.printBatteryReadingsToConsole();
		}
		System.out.println("\n\n Enter 'x' to exit...! ");
		
		}
		catch(NullPointerException  e)
		{
			System.out.println(e.getMessage());
		}
		}
		
	}
}
