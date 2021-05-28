package BMSStreamSender;

public class ValidateUserInput {

	public boolean UserInputisEmpty(String val) {
		return isNumeric(val);
	}

	public static boolean isNumeric(String inputGenarateRange) {
		try {
		    Integer.parseInt(inputGenarateRange);
		   
		} catch (NumberFormatException e) {
			System.out.println("Input value is Invalid!!");
		   return false;
		   
		}
		 return true;
	}


	public static boolean isGreaterthanMin(String inputGenarateRange) {
		// TODO Auto-generated method stub
		if((Integer.parseInt(inputGenarateRange))>=10) {
			return true;
		}
		System.out.println("Entered value is lesser than defined minimum!");
		return false;
		
	}
	
	
}
