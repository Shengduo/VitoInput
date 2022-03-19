import fire
class FileModifier(object):
    """ Modifies the file for further simulation """
    def modifyFiles(self, DRS, Load, Vw, VwW, Vw1, fw, fwW, theta, A):
        ## Main CFG file
        fileNamePrefix = "VWFirst_DRS1_" + str(DRS) + "ModA" + str(A) + "Load" + str(Load) + "_Vww" + str(Vw1) + "_" + str(VwW) + "_" + str(Vw) + "_fw" + str(fwW) + "_" + str(fw) + "_theta" + str(theta)
        mainCFGr = open("UsualSampleVSFH.cfg", 'r')
        list_of_lines = mainCFGr.readlines()
        # Change initial theta
        list_of_lines[204] = "friction.db_initial_state.data = [" + str(theta) + "*s]\n"
        # Change output file name
        list_of_lines[272] = "writer.filename = output3/frontsurfFiles/" + fileNamePrefix + "-frontsurf.h5\n"
        list_of_lines[285] = "writer.filename = output3/faultFiles/" + fileNamePrefix + "-fault.h5\n"
        # list_of_lines[297] = "writer.filename = output3/" + fileNamePrefix + "-upper_crust.h5\n"
        # list_of_lines[308] = "writer.filename = output3/" + fileNamePrefix + "-lower_crust.h5\n"
        list_of_lines[297] = "writer.filename = output3/upper_crust.h5\n"
        list_of_lines[308] = "writer.filename = output3/lower_crust.h5\n"
        mainCFGw = open("UsualSampleVSFH.cfg", 'w')
        mainCFGw.writelines(list_of_lines)
        # print(fileNamePrefix)
        mainCFGr.close()
        mainCFGw.close()

        ## Load .timedb file
        timeDBr = open("spatialdb/perturbation_cycle.timedb", 'r')
        list_of_lines = timeDBr.readlines()
        # print(list_of_lines)
        # Change load magnitude
        list_of_lines[15] = "0.1e-4 " + str(Load / 10.) + "\n"
        list_of_lines[16] = "0.14e-4 " + str(Load / 10.) + "\n"
        list_of_lines[17] = "0.16e-4 " + str(0.0) + "\n"
        timeDBw = open("spatialdb/perturbation_cycle.timedb", 'w')
        timeDBw.writelines(list_of_lines)
        timeDBr.close()
        timeDBw.close()

        ## Load .spatialdb file for friction
        fricDBr = open("spatialdb/rateStateProps1.spatialdb", 'r')
        list_of_lines = fricDBr.readlines()
        # list_of_lines[38] = "0.006354 0.003522 -0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  0.0256  0.011  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        # list_of_lines[38] = "0.006354 0.003522 -0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.011  0.0  " + str(fw) + "  " + str(Vw / 10.) + "\n"
        # list_of_lines[39] = "0.006354 0.003522  0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.011  0.0  " + str(fw) + "  " + str(Vw / 10.) + "\n"
        list_of_lines[32] = "-0.100000 -0.055430 -0.005000     0.58  1e-6   1e-6  0.011  0.016  0.0  0.3  " + str(Vw1) + "\n"
        list_of_lines[33] = "-0.100000 -0.055430  0.005000     0.58  1e-6   1e-6  0.011  0.016  0.0  0.3  " + str(Vw1) + "\n"
        list_of_lines[35] = "0.005480 0.003037 -0.005000     0.58  1e-6   1e-6  0.011  0.016  0.0  0.3  " + str(Vw1) + "\n"
        list_of_lines[36] = "0.005480 0.003037  0.005000     0.58  1e-6   1e-6  0.011  0.016  0.0  0.3  " + str(Vw1) + "\n"

        list_of_lines[38] = "0.006354 0.003522 -0.005000     0.58  1e-6   " + "1e-6" + "  " + "0.011" + "  0.013  0.0  " + str(fwW) + "  " + str(VwW) + "\n"
        list_of_lines[39] = "0.006354 0.003522  0.005000     0.58  1e-6   " + "1e-6" + "  " + "0.011" + "  0.013  0.0  " + str(fwW) + "  " + str(VwW) + "\n"
        list_of_lines[41] = "0.019473 0.010794 -0.005000     0.58  1e-6   " + "1e-6" + "  " + "0.011" + "  0.013  0.0  " + str(fwW) + "  " + str(VwW) + "\n"
        list_of_lines[42] = "0.019473 0.010794  0.005000     0.58  1e-6   " + "1e-6" + "  " + "0.011" + "  0.013  0.0  " + str(fwW) + "  " + str(VwW) + "\n"
        # list_of_lines[41] = "0.019473 0.010794 -0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.011  0.0  " + str(fw) + "  " + str(Vw / 15.) + "\n"
        # list_of_lines[42] = "0.019473 0.010794  0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.011  0.0  " + str(fw) + "  " + str(Vw / 15.) + "\n"
        list_of_lines[44] = "0.021223 0.011764 -0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.011  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[45] = "0.021223 0.011764  0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.011  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[47] = "0.058832 0.032610 -0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.011  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[48] = "0.058832 0.032610  0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.011  0.0  " + str(fw) + "  " + str(Vw) + "\n"


        fricDBw = open("spatialdb/rateStateProps1.spatialdb", 'w')
        fricDBw.writelines(list_of_lines)
        fricDBr.close()
        fricDBw.close()

if __name__ == '__main__':
    fire.Fire(FileModifier)
