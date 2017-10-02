from complex_functions import *
from wrapper_functions import *

name = "test_run"

def run():

    address, Sample, Sample_Box, sample_description = get_sample_info()
    #####################
    #select the test object and mount the sample on it

    test_object = select_test_object()
    cryostat    = select_cryostat()

    prepare_sample (Sample, Sample_Box, test_object)

    #####################
    #switch on and set up systems
    turn_on_computer()

    turn_on_PQMS_modules()
    set_up_pump(cryostat)

    #####################

    is_the_sample_loaded (Sample, Sample_Box, test_object, cryostat)
    cables_connected_check (test_object, cryostat)

    goto  ('work/git/XPLORE/Qrius/user_scripts/')
    write ('execute : Open Terminal')
    write ('execute : type python voltage_measurements.py')
    write ('execute : press enter')

    write ('execute : set temperature setpoints as required')
    write ('execute : set tolerance as 0.05')    
    write ('execute : press enter')
    
    write ("execute : Wait for run to end")
    
    write ('execute : Exit Terminal')

