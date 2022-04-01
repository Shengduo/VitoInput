import fire
class FileModifier(object):
    """ Modifies the file for further simulation """
    def modifyFiles(self, DRS, Load, Vw, fw, theta, A, NULoad):
        ## Main CFG file
        fileNamePrefix = "DRS1.5_" + str(DRS) + "ModA" + str(A) + "Load" + str(Load) + "_Vw" + str(Vw) + "_fw" + str(fw) + "_theta" + str(theta) + "_NULoad2dir" + str(NULoad)
        mainCFGr = open("UsualSampleVSFH.cfg", 'r')
        list_of_lines = mainCFGr.readlines()
        # Change initial theta
        list_of_lines[204] = "friction.db_initial_state.data = [" + str(theta) + "*s]\n"
        # Change output file name
        list_of_lines[262] = "writer.filename = output/dumpFiles/" + fileNamePrefix + "-domain.h5\n"
        list_of_lines[277] = "writer.filename = output/frontsurfFiles/" + fileNamePrefix + "-frontsurf.h5\n"
        list_of_lines[290] = "writer.filename = output/faultFiles/" + fileNamePrefix + "-fault.h5\n"

        list_of_lines[302] = "writer.filename = output/dumpFiles/" + fileNamePrefix + "-upper_crust.h5\n"
        list_of_lines[313] = "writer.filename = output/dumpFiles/" + fileNamePrefix + "-lower_crust.h5\n"

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
        
        list_of_lines[32] = "-0.100000 -0.055430 -0.005000     0.58  1e-6   1.5e-6  0.003  0.008  0.0  0.33  0.2" + "\n"
        list_of_lines[33] = "-0.100000 -0.055430  0.005000     0.58  1e-6   1.5e-6  0.003  0.008  0.0  0.33  0.2" + "\n"
        list_of_lines[35] = " 0.005480  0.003037 -0.005000     0.58  1e-6   1.5e-6  0.003  0.008  0.0  0.33  0.2" + "\n"
        list_of_lines[36] = " 0.005480  0.003037  0.005000     0.58  1e-6   1.5e-6  0.003  0.008  0.0  0.33  0.2" + "\n"

        list_of_lines[38] = " 0.006354  0.003522 -0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.003  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[39] = " 0.006354  0.003522  0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.003  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[41] = " 0.019473  0.010794 -0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.003  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[42] = " 0.019473  0.010794  0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.003  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        
        list_of_lines[44] = " 0.021223  0.011764 -0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.003  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[45] = " 0.021223  0.011764  0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.003  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[47] = " 0.058832  0.032610 -0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.003  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[48] = " 0.058832  0.032610  0.005000     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.003  0.0  " + str(fw) + "  " + str(Vw) + "\n"

        list_of_lines[50] = " 0.059706  0.033095 -0.005000     0.58  1e-6   1.5e-6  0.003  0.008  0.0  0.33  0.2" + "\n"
        list_of_lines[51] = " 0.059706  0.033095  0.005000     0.58  1e-6   1.5e-6  0.003  0.008  0.0  0.33  0.2" + "\n"
        list_of_lines[53] = " 0.100000  0.055430 -0.005000     0.58  1e-6   1.5e-6  0.003  0.008  0.0  0.33  0.2" + "\n"
        list_of_lines[54] = " 0.100000  0.055430  0.005000     0.58  1e-6   1.5e-6  0.003  0.008  0.0  0.33  0.2" + "\n"

        fricDBw = open("spatialdb/rateStateProps1.spatialdb", 'w')
        fricDBw.writelines(list_of_lines)
        fricDBr.close()
        fricDBw.close()

        ## Modify NUload
        NULoadCFGr = open("spatialdb/prescribed_traction_initial.spatialdb", 'r')
        list_of_lines = NULoadCFGr.readlines()
        # Change initial prescribed perturbed traction
        list_of_lines[35] =  " 0.006354  0.003522 -0.005000     " + str(NULoad * 0.554309051452769) + "  0.0  " + str(NULoad) + "\n"
        list_of_lines[36] =  " 0.006354  0.003522  0.005000     " + str(NULoad * 0.554309051452769) + "  0.0  " + str(NULoad) + "\n"
        
        list_of_lines[38] =  " 0.019473  0.010794 -0.005000     " + str(NULoad * 0.554309051452769) + "  0.0  " + str(NULoad) + "\n"
        list_of_lines[39] =  " 0.019473  0.010794  0.005000     " + str(NULoad * 0.554309051452769) + "  0.0  " + str(NULoad) + "\n"
        
        list_of_lines[41] =  " 0.021223  0.011764 -0.005000     " + str(-NULoad * 0.554309051452769 / 3.) + "  0.0  " + str(-NULoad / 3.) + "\n"
        list_of_lines[42] =  " 0.021223  0.011764  0.005000     " + str(-NULoad * 0.554309051452769 / 3.) + "  0.0  " + str(-NULoad / 3.) + "\n"
        
        list_of_lines[44] =  " 0.058832  0.032610 -0.005000     " + str(-NULoad * 0.554309051452769 / 3.) + "  0.0  " + str(-NULoad / 3.) + "\n"
        list_of_lines[45] =  " 0.058832  0.032610  0.005000     " + str(-NULoad * 0.554309051452769 / 3.) + "  0.0  " + str(-NULoad / 3.) + "\n"

        NULoadCFGw = open("spatialdb/prescribed_traction_initial.spatialdb", 'w')
        NULoadCFGw.writelines(list_of_lines)
        # print(fileNamePrefix)
        NULoadCFGr.close()
        NULoadCFGw.close()

if __name__ == '__main__':
    fire.Fire(FileModifier)
