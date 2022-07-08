import imp
from hourlyEmployee import HourlyEmployee
from fulltimeemployee import FullTimeEmployee
from payroll import Payroll




payroll = Payroll()
payroll.add(FullTimeEmployee('Zelalem', 'Enyew', 1000 ))
payroll.add(FullTimeEmployee('Abel', 'Tefera', 4000 ))
payroll.add(HourlyEmployee('Getnet', 'ENdaye', 200, 50 ))
payroll.add(HourlyEmployee('Mahlaet ', 'Kinfe', 100, 150 ))


payroll.print()