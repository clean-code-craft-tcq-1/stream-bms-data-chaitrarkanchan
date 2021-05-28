package BMSStreamSender;

import java.util.List;

public interface IBMSService {
		public List<BMSFactors> genearateBatteryReadings(int streamcount);
		public void printBatteryReadingsToConsole();
}
