import fire
class FileModifier(object):
    """ Modifies the file for further simulation """
    def modifyFiles(self, theta):
        ## Main CFG file
        fileNamePrefix = "PureWeakening_theta" + str(theta)
        mainCFGr = open("UsualSampleVSFH_pureweakening.cfg", 'r')
        list_of_lines = mainCFGr.readlines()
        # Change initial theta
        list_of_lines[204] = "friction.db_initial_state.data = [" + str(theta) + "*s]\n"
        # Change output file name
        list_of_lines[272] = "writer.filename = output/frontsurfFiles/" + fileNamePrefix + "-frontsurf.h5\n"
        list_of_lines[285] = "writer.filename = output/faultFiles/" + fileNamePrefix + "-fault.h5\n"
        # list_of_lines[297] = "writer.filename = output3/" + fileNamePrefix + "-upper_crust.h5\n"
        # list_of_lines[308] = "writer.filename = output3/" + fileNamePrefix + "-lower_crust.h5\n"
        list_of_lines[297] = "writer.filename = output/dumpFiles/upper_crust.h5\n"
        list_of_lines[308] = "writer.filename = output/dumpFiles/lower_crust.h5\n"
        mainCFGw = open("UsualSampleVSFH_pureweakening.cfg", 'w')
        mainCFGw.writelines(list_of_lines)
        # print(fileNamePrefix)
        mainCFGr.close()
        mainCFGw.close()
        
if __name__ == '__main__':
    fire.Fire(FileModifier)
