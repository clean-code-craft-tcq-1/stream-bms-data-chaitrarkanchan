package BMSStreamSender;
import static org.junit.Assert.*;

import org.junit.runner.RunWith;
import org.mockito.Mockito;
import org.mockito.runners.MockitoJUnitRunner;
import org.junit.Test;

@RunWith(MockitoJUnitRunner.class)
public class BatteryManagementSystemTest {

	@Test
	 public void generateParamValues_whenValueIsEmpty_thenReturnFalse() {
			
		 assertFalse(ValidateUserInput.isNumeric(""));
	 }
	
	@Test
	 public void generateParamValues_whenValueInValid_thenReturnFalse() {
			
		 assertFalse(ValidateUserInput.isNumeric("12B"));
	 }
	
	@Test
	public void generateParamValues_whenValueIsLesserThan10_thenReturnFalse() {
		assertFalse(ValidateUserInput.isGreaterthanMin("5"));
	}
	
	@Test
	public void generateParamValues_whenValueIsGreaterOrEquals10_thenReturnTrue() {
		assertTrue(ValidateUserInput.isGreaterthanMin("10"));
	}
	
	@Test
	public void generateParamValues_whenGeneratedParamValCount_thenReturnTrue() {
		IBMSService bms_service=new BMSServiceImpl();
		int expected_reading_count=12;
		assertEquals(bms_service.genearateBatteryReadings(12).size(),expected_reading_count);
	}
	
	@Test
	public void checkIfBMSValuesPrinting() {
	IBMSService bmsStreamerImplMock = Mockito.mock(BMSServiceImpl.class);
	((BMSServiceImpl) bmsStreamerImplMock).printBatteryReadingsToConsole();
	((BMSServiceImpl) Mockito.verify(bmsStreamerImplMock, Mockito.times(1))).printBatteryReadingsToConsole();
	}
}
