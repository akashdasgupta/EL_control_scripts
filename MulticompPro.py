import pyvisa as visa
try:
    rm.list_resources()
except NameError:
    rm = visa.ResourceManager(r'C:\Windows\System32\visa64.dll')
    resources = rm.list_resources()
for resource in resources:
    if resource.startswith("USB"):
        power_supply_string = resource

class MulticompPro():
    def __init__(self):
        try:
            print("Attempting to connect to Multicomp power supply...")
            self.ps = rm.open_resource(power_supply_string)
            self.ps.read_termination = '\n'
            self.ps.write_termination = '\n'
            # Safety: 
            self.ps.write("OUTPUT OFF")
            self.ps.write("CURR:LIM 2.01")
            print("Done!")
        except:
            print('Could not initilise Multicomp power supply (for LED)! ID given:', power_supply_string)

    def on(self):
        self.ps.write("OUTPUT ON")
    def off(self):
        self.ps.write("OUTPUT OFF")
    
    def set_voltage(self, value):
        self.ps.write(f"VOLT {value}")
    
    def close(self):
        self.ps.close()
        
    










