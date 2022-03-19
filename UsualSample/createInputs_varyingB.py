import fire
class FileModifier(object):
    """ Modifies the file for further simulation """
    def modifyFiles(self, DRS, Load, Vw, VwW, Vw1, fw, fwW, theta, A, b_final, b_distance):
        ## Main CFG file
        fileNamePrefix = "VaryingB_DRS1_" + str(DRS) + "A" + str(A) + "B" + str(b_final) + "_" + str(b_distance) + "Load" + str(Load) + "_Vww" + str(Vw1) + "_" + str(VwW) + "_" + str(Vw) + "_fw" + str(fwW) + "_" + str(fw) + "_theta" + str(theta)
        mainCFGr = open("UsualSampleVaryingBVSFH.cfg", 'r')
        list_of_lines = mainCFGr.readlines()
        # Change initial theta
        list_of_lines[204] = "friction.db_initial_state.data = [" + str(theta) + "*s]\n"
        # Change output file name
        list_of_lines[257] = "writer.filename = output/dumpFiles/" + fileNamePrefix + "-domain.h5"
        list_of_lines[272] = "writer.filename = output/frontsurfFiles/" + fileNamePrefix + "-frontsurf.h5\n"
        list_of_lines[285] = "writer.filename = output/faultFiles/" + fileNamePrefix + "-fault.h5\n"
        list_of_lines[297] = "writer.filename = output/dumpFiles/" + fileNamePrefix + "-upper_crust.h5\n"
        list_of_lines[308] = "writer.filename = output/dumpFiles/" + fileNamePrefix + "-lower_crust.h5\n"
        # list_of_lines[297] = "writer.filename = output/upper_crust.h5\n"
        # list_of_lines[308] = "writer.filename = output/lower_crust.h5\n"
        mainCFGw = open("UsualSampleVaryingBVSFH.cfg", 'w')
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
        fricDBr = open("spatialdb/rateStateProps_varyingB.spatialdb", 'r')
        list_of_lines = fricDBr.readlines()
        # list_of_lines[38] = "0.006354 0.003522 -0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  0.0256  0.011  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        # list_of_lines[38] = "0.006354 0.003522 -0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.011  0.0  " + str(fw) + "  " + str(Vw / 10.) + "\n"
        # list_of_lines[39] = "0.006354 0.003522  0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.011  0.0  " + str(fw) + "  " + str(Vw / 10.) + "\n"
        list_of_lines[34] = "-0.100000 -0.055430 -0.005000     0.58  1e-6   1e-6  0.011  0.016  0.016  2e-6  0.0  0.3  " + str(Vw1) + "\n"
        list_of_lines[35] = "-0.100000 -0.055430  0.005000     0.58  1e-6   1e-6  0.011  0.016  0.016  2e-6  0.0  0.3  " + str(Vw1) + "\n"
        list_of_lines[37] = " 0.005480  0.003037 -0.005000     0.58  1e-6   1e-6  0.011  0.016  0.016  2e-6  0.0  0.3  " + str(Vw1) + "\n"
        list_of_lines[38] = " 0.005480  0.003037  0.005000     0.58  1e-6   1e-6  0.011  0.016  0.016  2e-6  0.0  0.3  " + str(Vw1) + "\n"

        list_of_lines[40] = " 0.006354 0.003522 -0.005000     0.58  1e-6   " + "1e-6" + "  " + "0.011" + "  0.013  " + str(b_final) + "  "  + str(b_distance) + " 0.0  " + str(fwW) + "  " + str(VwW) + "\n"
        list_of_lines[41] = " 0.006354 0.003522  0.005000     0.58  1e-6   " + "1e-6" + "  " + "0.011" + "  0.013  " + str(b_final) + "  "  + str(b_distance) + " 0.0  " + str(fwW) + "  " + str(VwW) + "\n"
        list_of_lines[43] = " 0.019473 0.010794 -0.005000     0.58  1e-6   " + "1e-6" + "  " + "0.011" + "  0.013  " + str(b_final) + "  "  + str(b_distance) + " 0.0  " + str(fwW) + "  " + str(VwW) + "\n"
        list_of_lines[44] = " 0.019473 0.010794  0.005000     0.58  1e-6   " + "1e-6" + "  " + "0.011" + "  0.013  " + str(b_final) + "  "  + str(b_distance) + " 0.0  " + str(fwW) + "  " + str(VwW) + "\n"
        # list_of_lines[41] = "0.019473 0.010794 -0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.011  0.011  2e-6  0.0  " + str(fw) + "  " + str(Vw / 15.) + "\n"
        # list_of_lines[42] = "0.019473 0.010794  0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.011  0.011  2e-6  0.0  " + str(fw) + "  " + str(Vw / 15.) + "\n"
        list_of_lines[46] = " 0.021223 0.011764 -0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.011  0.011  2e-6  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[47] = " 0.021223 0.011764  0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.011  0.011  2e-6  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[49] = " 0.058832 0.032610 -0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.011  0.011  2e-6  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[50] = " 0.058832 0.032610  0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.011  0.011  2e-6  0.0  " + str(fw) + "  " + str(Vw) + "\n"

        list_of_lines[52] = "0.059706 0.033095 -0.005000     0.58  1e-6   1e-6  0.011  0.016  0.016 2e-6 0.0  0.3  " + str(Vw1) + "\n"
        list_of_lines[53] = "0.059706 0.033095  0.005000     0.58  1e-6   1e-6  0.011  0.016  0.016 2e-6 0.0  0.3  " + str(Vw1) + "\n"
        list_of_lines[55] = "0.100000 0.055430 -0.005000     0.58  1e-6   1e-6  0.011  0.016  0.016 2e-6 0.0  0.3  " + str(Vw1) + "\n"
        list_of_lines[56] = "0.100000 0.055430  0.005000     0.58  1e-6   1e-6  0.011  0.016  0.016 2e-6 0.0  0.3  " + str(Vw1) + "\n"

        fricDBw = open("spatialdb/rateStateProps_varyingB.spatialdb", 'w')
        fricDBw.writelines(list_of_lines)
        fricDBr.close()
        fricDBw.close()

if __name__ == '__main__':
    fire.Fire(FileModifier)
