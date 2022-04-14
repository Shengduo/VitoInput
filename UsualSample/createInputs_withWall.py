import fire
class FileModifier(object):
    # Define the size of wall
    WallPos1 = " -0.005000"
    WallPos2 = " -0.004000"
    WallPos3 = " -0.003800"
    WallPos4 = "  0.003800"
    WallPos5 = "  0.004000"
    WallPos6 = "  0.005000"

    """ Modifies the file for further simulation """
    def modifyFiles(self, DRS, Load, Vw, fw, theta1, theta2, A, NULoad):
        ## Main CFG file
        fileNamePrefix = "WithWallDRS1.5_" + str(DRS) + "ModA" + str(A) + "Load" + str(Load) + "_Vw" + str(Vw) + "_fw" + str(fw) + "_theta" + str(theta1) + "_" + str(theta2) + "_NULoad2dir" + str(NULoad)
        mainCFGr = open("UsualSampleVSFH_withWall.cfg", 'r')
        list_of_lines = mainCFGr.readlines()

        # Change output file name
        list_of_lines[262] = "writer.filename = output/dumpFiles/" + fileNamePrefix + "-domain.h5\n"
        list_of_lines[277] = "writer.filename = output/frontsurfFiles/" + fileNamePrefix + "-frontsurf.h5\n"
        list_of_lines[290] = "writer.filename = output/faultFiles/" + fileNamePrefix + "-fault.h5\n"

        list_of_lines[302] = "writer.filename = output/dumpFiles/" + fileNamePrefix + "-upper_crust.h5\n"
        list_of_lines[313] = "writer.filename = output/dumpFiles/" + fileNamePrefix + "-lower_crust.h5\n"

        mainCFGw = open("UsualSampleVSFH_withWall.cfg", 'w')
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

        ## Modify rateStateProps
        fricDBr = open("spatialdb/rateStateProps_withWall.spatialdb", 'r')
        list_of_lines = fricDBr.readlines()
        
        list_of_lines[50] = " 0.006354  0.003522 -0.003800     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.003  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[51] = " 0.006354  0.003522  0.003800     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.003  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[59] = " 0.058832  0.032610 -0.003800     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.003  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[60] = " 0.058832  0.032610  0.003800     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.003  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        
        # Modify the locations
        Wallposition = [self.WallPos3, self.WallPos4, self.WallPos2, self.WallPos5, self.WallPos1, self.WallPos6]
        counter = 0;
        for index in range(32, 85):
            if len(list_of_lines[index]) > 29:
                list_of_lines[index] = list_of_lines[index][0:19] + Wallposition[counter % 6] + list_of_lines[index][29:]
                counter = counter + 1
        
        # Write files
        fricDBw = open("spatialdb/rateStateProps_withWall.spatialdb", 'w')
        fricDBw.writelines(list_of_lines)
        fricDBr.close()
        fricDBw.close()

        ## Modify NUload
        NULoadCFGr = open("spatialdb/prescribed_traction_initial_withWall.spatialdb", 'r')
        list_of_lines = NULoadCFGr.readlines()

        # First set all loads to be zero
        for index in range(29, 100):
            if len(list_of_lines[index]) > 29:
                list_of_lines[index] = list_of_lines[index][0:29] + "     " + "0.0" + "  0.0  " + "0.0" + "\n"
                

        # Change initial prescribed perturbed traction
        list_of_lines[53] =  " 0.006354  0.003522 -0.003800     " + str(NULoad * 0.554309051452769) + "  0.0  " + str(NULoad) + "\n"
        list_of_lines[54] =  " 0.006354  0.003522  0.003800     " + str(NULoad * 0.554309051452769) + "  0.0  " + str(NULoad) + "\n"
        
        list_of_lines[62] =  " 0.019473  0.010794 -0.003800     " + str(NULoad * 0.554309051452769) + "  0.0  " + str(NULoad) + "\n"
        list_of_lines[63] =  " 0.019473  0.010794  0.003800     " + str(NULoad * 0.554309051452769) + "  0.0  " + str(NULoad) + "\n"
        
        list_of_lines[71] =  " 0.021223  0.011764 -0.003800     " + str(-NULoad * 0.554309051452769 / 3.) + "  0.0  " + str(-NULoad / 3.) + "\n"
        list_of_lines[72] =  " 0.021223  0.011764  0.003800     " + str(-NULoad * 0.554309051452769 / 3.) + "  0.0  " + str(-NULoad / 3.) + "\n"
        
        list_of_lines[80] =  " 0.058832  0.032610 -0.003800     " + str(-NULoad * 0.554309051452769 / 3.) + "  0.0  " + str(-NULoad / 3.) + "\n"
        list_of_lines[81] =  " 0.058832  0.032610  0.003800     " + str(-NULoad * 0.554309051452769 / 3.) + "  0.0  " + str(-NULoad / 3.) + "\n"

        # Modify the locations
        Wallposition = [self.WallPos1, self.WallPos6, self.WallPos2, self.WallPos5, self.WallPos3, self.WallPos4]
        counter = 0;
        for index in range(29, 100):
            if len(list_of_lines[index]) > 29:
                list_of_lines[index] = list_of_lines[index][0:19] + Wallposition[counter % 6] + list_of_lines[index][29:]
                counter = counter + 1

        # Write files
        NULoadCFGw = open("spatialdb/prescribed_traction_initial_withWall.spatialdb", 'w')
        NULoadCFGw.writelines(list_of_lines)
        # print(fileNamePrefix)
        NULoadCFGr.close()
        NULoadCFGw.close()

        ## Modify state variable
        THETAr = open("spatialdb/stateVariable_withWall.spatialdb")
        list_of_lines = THETAr.readlines()

        # Modify the locations
        Wallposition = [self.WallPos1, self.WallPos6, self.WallPos2, self.WallPos5, self.WallPos3, self.WallPos4]
        counter = 0;
        for index in range(27, 80):
            if len(list_of_lines[index]) > 29:
                list_of_lines[index] = list_of_lines[index][0:19] + Wallposition[counter % 6] + list_of_lines[index][29:]
                counter = counter + 1

        # Change somelines into theta1, some into theta2
        set_of_theta2_lines = [" 0.006354  0.003522" + self.WallPos3, 
                               " 0.006354  0.003522" + self.WallPos4, 
                               " 0.058832  0.032610" + self.WallPos3, 
                               " 0.058832  0.032610" + self.WallPos4]
        for index in range(27, 80):
            if len(list_of_lines[index]) > 29:
                if list_of_lines[index][0:29] in set_of_theta2_lines:
                    list_of_lines[index] = list_of_lines[index][0:29] + "     " + str(theta2) + "\n"
                else:
                    list_of_lines[index] = list_of_lines[index][0:29] + "     " + str(theta1) + "\n"
        

        THETAw = open("spatialdb/stateVariable_withWall.spatialdb", 'w')
        THETAw.writelines(list_of_lines)
        THETAr.close()
        THETAw.close()

    """ Modifies the file for further simulation """
    def modifyFiles_GougeDifferentLoad(self, DRS, Load, Vw, fw, theta1, theta2, A, NULoad):
        

        ## Main CFG file
        fileNamePrefix = "DiffNULoadWithWallDRS1.5_" + str(DRS) + "ModA" + str(A) + "Load" + str(Load) + "_Vw" + str(Vw) + "_fw" + str(fw) + "_theta" + str(theta1) + "_" + str(theta2) + "_NULoad2dir" + str(NULoad)
        mainCFGr = open("UsualSampleVSFH_withWall.cfg", 'r')
        list_of_lines = mainCFGr.readlines()

        # Change output file name
        list_of_lines[262] = "writer.filename = output/dumpFiles/" + fileNamePrefix + "-domain.h5\n"
        list_of_lines[277] = "writer.filename = output/frontsurfFiles/" + fileNamePrefix + "-frontsurf.h5\n"
        list_of_lines[290] = "writer.filename = output/faultFiles/" + fileNamePrefix + "-fault.h5\n"

        list_of_lines[302] = "writer.filename = output/dumpFiles/" + fileNamePrefix + "-upper_crust.h5\n"
        list_of_lines[313] = "writer.filename = output/dumpFiles/" + fileNamePrefix + "-lower_crust.h5\n"

        mainCFGw = open("UsualSampleVSFH_withWall.cfg", 'w')
        mainCFGw.writelines(list_of_lines)
        # print(fileNamePrefix)
        mainCFGr.close()
        mainCFGw.close()

        ## Load .timedb file
        timeDBr = open("spatialdb/perturbation_cycle.timedb", 'r')
        list_of_lines = timeDBr.readlines()

        # Change load magnitude
        list_of_lines[15] = "0.1e-4 " + str(Load / 10.) + "\n"
        list_of_lines[16] = "0.14e-4 " + str(Load / 10.) + "\n"
        list_of_lines[17] = "0.16e-4 " + str(0.0) + "\n"
        timeDBw = open("spatialdb/perturbation_cycle.timedb", 'w')
        timeDBw.writelines(list_of_lines)
        timeDBr.close()
        timeDBw.close()

        ## Modify rateStateProps
        fricDBr = open("spatialdb/rateStateProps_withWall.spatialdb", 'r')
        list_of_lines = fricDBr.readlines()

        list_of_lines[50] = " 0.006354  0.003522 -0.003800     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.003  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[51] = " 0.006354  0.003522  0.003800     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.003  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[59] = " 0.058832  0.032610 -0.003800     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.003  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[60] = " 0.058832  0.032610  0.003800     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.003  0.0  " + str(fw) + "  " + str(Vw) + "\n"

        # Modify the locations
        Wallposition = [self.WallPos3, self.WallPos4, self.WallPos2, self.WallPos5, self.WallPos1, self.WallPos6]
        counter = 0;
        for index in range(32, 85):
            if len(list_of_lines[index]) > 29:
                list_of_lines[index] = list_of_lines[index][0:19] + Wallposition[counter % 6] + list_of_lines[index][29:]
                counter = counter + 1
        
        fricDBw = open("spatialdb/rateStateProps_withWall.spatialdb", 'w')
        fricDBw.writelines(list_of_lines)
        fricDBr.close()
        fricDBw.close()

        ## Modify NUload
        NULoadCFGr = open("spatialdb/prescribed_traction_initial_withWall.spatialdb", 'r')
        set_of_NULoad_lines = [" 0.006354  0.003522" + self.WallPos3, 
                               " 0.006354  0.003522" + self.WallPos4, 
                               " 0.058832  0.032610" + self.WallPos3, 
                               " 0.058832  0.032610" + self.WallPos4, 
                               " 0.019473  0.010794" + self.WallPos3, 
                               " 0.019473  0.010794" + self.WallPos4, 
                               " 0.021223  0.011764" + self.WallPos3, 
                               " 0.021223  0.011764" + self.WallPos4]
                            
        list_of_lines = NULoadCFGr.readlines()
        ratio = 0.2 * 0.01 / (0.0078 * (0.058832 - 0.006354))

        # Modify the locations
        Wallposition = [self.WallPos1, self.WallPos6, self.WallPos2, self.WallPos5, self.WallPos3, self.WallPos4]
        counter = 0;
        for index in range(29, 100):
            if len(list_of_lines[index]) > 29:
                list_of_lines[index] = list_of_lines[index][0:19] + Wallposition[counter % 6] + list_of_lines[index][29:]
                counter = counter + 1
        
        # Change load
        for index in range(29, 100):
            if len(list_of_lines[index]) > 29:
                if list_of_lines[index][0:29] in set_of_NULoad_lines:
                    list_of_lines[index] = list_of_lines[index][0:29] + "     " + str(NULoad * 0.554309051452769) + "  0.0  " + str(NULoad) + "\n"
                else:
                    list_of_lines[index] = list_of_lines[index][0:29] + "     " + str(-NULoad * 0.554309051452769 / ratio) + "  0.0  " + str(-NULoad / ratio) + "\n"

        NULoadCFGw = open("spatialdb/prescribed_traction_initial_withWall.spatialdb", 'w')
        NULoadCFGw.writelines(list_of_lines)
        # print(fileNamePrefix)
        NULoadCFGr.close()
        NULoadCFGw.close()

        ## Modify state variable
        THETAr = open("spatialdb/stateVariable_withWall.spatialdb")
        list_of_lines = THETAr.readlines()

        # Modify the locations
        Wallposition = [self.WallPos1, self.WallPos6, self.WallPos2, self.WallPos5, self.WallPos3, self.WallPos4]
        counter = 0;
        for index in range(27, 80):
            if len(list_of_lines[index]) > 29:
                list_of_lines[index] = list_of_lines[index][0:19] + Wallposition[counter % 6] + list_of_lines[index][29:]
                counter = counter + 1
        
        # Change somelines into theta1, some into theta2
        set_of_theta2_lines = [" 0.006354  0.003522" + self.WallPos3, 
                               " 0.006354  0.003522" + self.WallPos4, 
                               " 0.058832  0.032610" + self.WallPos3, 
                               " 0.058832  0.032610" + self.WallPos4]
        
        for index in range(27, 80):
            if len(list_of_lines[index]) > 29:
                if list_of_lines[index][0:29] in set_of_theta2_lines:
                    list_of_lines[index] = list_of_lines[index][0:29] + "     " + str(theta2) + "\n"
                else:
                    list_of_lines[index] = list_of_lines[index][0:29] + "     " + str(theta1) + "\n"
        
        THETAw = open("spatialdb/stateVariable_withWall.spatialdb", 'w')
        THETAw.writelines(list_of_lines)
        THETAr.close()
        THETAw.close()

if __name__ == '__main__':
    fire.Fire(FileModifier)
