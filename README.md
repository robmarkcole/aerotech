# aerotech
Summary: `aerotech.py` provides a class called Ensemble to enable control of the Aerotech [Ensemble controllers](https://www.aerotech.com/product-catalog/drives-and-drive-racks/ensemble-lab.aspx) by issuing commands using TCP via ethernet cable. Default settings of the stage are assumed. The file is written in python 3 and no requirements other than the standard python 3 libraries are required.

## Emulator
`EnsembleEmulator.jar` is an emulator for the hardware that is used for testing and development. Assuming you have Java installed, double cliching the `.jar` file will launch the emulator, which will receive commands on port 8000. The jupyter notebook `usage.ipynb` shows how to control the emulator. For use with real hardware you would just update the IP address of the hardware.

## Tests
The file `test_aerotech.py` provides simple tests of the Ensemble class and assumes the emulator is running. Run the test with `$ python3 test_aerotech.py`
