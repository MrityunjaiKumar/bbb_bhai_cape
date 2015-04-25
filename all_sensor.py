import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
     
ADC.setup()
GPIO.setup("P8_10",GPIO.IN)
GPIO.setup("P8_9",GPIO.IN)    
while True:
	'''lm35'''
	value_P9_39 = ADC.read("P9_39")
    	millivolt_P9_39 = value_P9_39 * 1800 #1.8V
	temp_c=(millivolt_P9_39 - 500) / -10
	
	'''hall effect sensor'''
	value_P9_36 = ADC.read("P9_36")
	millivolt_P9_36 = value_P9_36 * 1800
	
	''' LDR '''
	value_P9_33 =ADC.read("P9_33")
	millivolt_P9_33 =value_P9_33 * 1800
	
	'''Thermistor'''
	value_P9_40 = ADC.read("P9_40")
	millivolt_P9_40 =value_P9_40 * 1800

	
	'''ThubPot'''
	value_P9_38 =ADC.read("P9_38")
	millivolt_P9_38 = value_P9_38 * 1800

	'''Push Button'''
	Button1 = 'OFF'
	Button2 = 'OFF'
	if GPIO.input("P8_10")==False:
		Button1 = 'ON'
	if GPIO.input("P8_9")==False:
		Button2 = 'ON'
	
	print ('mv_P9_39=%.2f \t Temperature=%.2f \t\t hall=%.2f \t LDR=%.2f \t Thermistor=%.2f \t Thubpot=%.2f \t Button1=%s \t Button2=%s' % (millivolt_P9_39,temp_c,millivolt_P9_36, millivolt_P9_33, millivolt_P9_40, millivolt_P9_38,Button1,Button2)), "\r", 
