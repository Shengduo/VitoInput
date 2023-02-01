from curses.ascii import NUL
import fire
import math

from yaml import load
class FileModifier(object):
    # Define the size of wall
    WallPos1 = " -0.005000"
    WallPos2 = " -0.004100"
    WallPos3 = " -0.003900"
    WallPos4 = "  0.004300"
    WallPos5 = "  0.004500"
    WallPos6 = "  0.005000"

    """ Modifies the file for further simulation """
    def modifyFiles(self, DRS, Load, Vw, fw, theta1, theta2, A, AmB, b_final, b_distance, NULoad, meshFineness, duration, rest, NPOP):
        ## If meshFineness is 2
        if meshFineness == 2:
            backgroundCFGr = open("pylithapp.cfg", 'r')
            list_of_lines = backgroundCFGr.readlines()

            # Change the input mesh file to the finer one
            list_of_lines[46] = "filename = mesh/finer_tet.exo\n"
            backgroundCFGw = open("pylithapp.cfg", 'w')
            backgroundCFGw.writelines(list_of_lines)

            # close files
            backgroundCFGr.close()
            backgroundCFGw.close()
        
        elif meshFineness == 3:
            backgroundCFGr = open("pylithapp.cfg", 'r')
            list_of_lines = backgroundCFGr.readlines()

            # Change the input mesh file to the finer one
            list_of_lines[46] = "filename = mesh/finer_tet3.exo\n"
            backgroundCFGw = open("pylithapp.cfg", 'w')
            backgroundCFGw.writelines(list_of_lines)

            # close files
            backgroundCFGr.close()
            backgroundCFGw.close()

        else:
            backgroundCFGr = open("pylithapp.cfg", 'r')
            list_of_lines = backgroundCFGr.readlines()

            # Change the input mesh file to the finer one
            list_of_lines[46] = "filename = mesh/myGeometryTetFiner.exo\n"
            backgroundCFGw = open("pylithapp.cfg", 'w')
            backgroundCFGw.writelines(list_of_lines)

            # close files
            backgroundCFGr.close()
            backgroundCFGw.close()


        ## Main CFG file
        ## Modify rateStateProps
        if NPOP == 0:
            fileNamePrefix = str(meshFineness) + "VaryingBOPDirWithWallDRS1.5_" + str(DRS) + "ModA" + str(A) + "AmB" + str(AmB) + "_" + str(b_final) + "bD" + str(b_distance) + "Load" + str(Load) + "_Vw" + str(Vw) + "_fw" + str(fw) + "_theta" + str(theta1) + "_" + str(theta2) + "_NULoad2dir" + str(NULoad) + "_duration" + str(duration) + "_" + str(rest)
        elif NPOP == 1:
            fileNamePrefix = str(meshFineness) + "VaryingBNPDirWithWallDRS1.5_" + str(DRS) + "ModA" + str(A) + "AmB" + str(AmB) + "_" + str(b_final) + "bD" + str(b_distance) + "Load" + str(Load) + "_Vw" + str(Vw) + "_fw" + str(fw) + "_theta" + str(theta1) + "_" + str(theta2) + "_NULoad2dir" + str(NULoad) + "_duration" + str(duration) + "_" + str(rest)
        
        mainCFGr = open("UsualSampleVSFH_withWall_Dirichlet_varyingB.cfg", 'r')
        list_of_lines = mainCFGr.readlines()
        
        # First deal with theta2, assuming alpha = 29 \deg, tan(alpha) = 0.554309051452769, f_* = 0.58, linear slip rate = 1e-9
        B = A - AmB
        if theta2 < 0.0:
            # Apply V_ini = 10^{\theta_2};
            f = math.tan(29 / 180 * math.pi)
            Vlin = 1.0e-9
            Vini = 10.0**theta2
            if theta2 < - 9:
                temp = f - 0.58 - A * math.log(Vlin / 1e-6) + A * (1 - Vini / Vlin)
                theta2 = math.exp(temp / B) * DRS / 1e-6 
            else:
                temp = f - 0.58 - A * math.log(Vini / 1e-6)
                theta2 = math.exp(temp / B) * DRS / 1e-6 
        print("theta2 =", theta2)

        # Change friction file
        if NPOP == 0:
            list_of_lines[197] = "friction.db_properties.iohandler.filename = spatialdb/rateStateProps_withWall_varyingB.spatialdb\n"
        elif NPOP == 1:
            list_of_lines[197] = "friction.db_properties.iohandler.filename = spatialdb/rateStateProps_withWall_NP_varyingB.spatialdb\n"
        
        # Change the duration of simulation time
        list_of_lines[77] = "total_time = " + str((duration + rest)/ 1.0e6) + "*s\n"
        # Change output file name
        list_of_lines[262] = "writer.filename = output/dumpFiles/" + fileNamePrefix + "-domain.h5\n"
        list_of_lines[277] = "writer.filename = output/frontsurfFiles/" + fileNamePrefix + "-frontsurf.h5\n"
        list_of_lines[290] = "writer.filename = output/faultFiles/" + fileNamePrefix + "-fault.h5\n"

        list_of_lines[302] = "writer.filename = output/dumpFiles/" + fileNamePrefix + "-upper_crust.h5\n"
        list_of_lines[313] = "writer.filename = output/dumpFiles/" + fileNamePrefix + "-lower_crust.h5\n"

        # Change prestress distribution
        if NULoad == 0:
            list_of_lines[212] = "db_initial.filename = spatialdb/prescribed_traction_initial_withWall_newload_grid0.spatialdb\n"
        elif NULoad == 1:
            list_of_lines[212] = "db_initial.filename = spatialdb/prescribed_traction_initial_withWall_newload_grid1.spatialdb\n"
        elif NULoad == 2:
            list_of_lines[212] = "db_initial.filename = spatialdb/prescribed_traction_initial_withWall_newload_grid2.spatialdb\n"
        elif NULoad == 3:
            list_of_lines[212] = "db_initial.filename = spatialdb/prescribed_traction_initial_withWall_newload_grid3.spatialdb\n"
        elif NULoad == 4:
            list_of_lines[212] = "db_initial.filename = spatialdb/prescribed_traction_initial_withWall_newload_grid4.spatialdb\n"
        else:
            print("NUload not available, you're fucked!\n")

        mainCFGw = open("UsualSampleVSFH_withWall_Dirichlet_varyingB.cfg", 'w')
        mainCFGw.writelines(list_of_lines)
        # print(fileNamePrefix)
        mainCFGr.close()
        mainCFGw.close()

        ## Load .timedb file
        timeDBr = open("spatialdb/perturbation_cycle.timedb", 'r')
        list_of_lines = timeDBr.readlines()
        # print(list_of_lines)
        # Change load magnitude
        list_of_lines[14] = str(0.08e-4 + rest / 1.0e6) + "  " + str(0.0) + "\n"
        list_of_lines[15] = str(0.1e-4 + rest / 1.0e6) + "  "  + str(Load / 10.) + "\n"
        list_of_lines[16] = str(0.14e-4 + rest / 1.0e6) + "  " + str(Load / 10.) + "\n"
        list_of_lines[17] = str(0.16e-4 + rest / 1.0e6) + "  " + str(0.0) + "\n"
        list_of_lines[18] = str((duration + rest) / 1.0e6) + "  " + str(0.0) + "\n"
        timeDBw = open("spatialdb/perturbation_cycle.timedb", 'w')
        timeDBw.writelines(list_of_lines)
        timeDBr.close()
        timeDBw.close()

        ## Modify rateStateProps
        if NPOP == 0:
            fricDBr = open("spatialdb/rateStateProps_withWall_varyingB.spatialdb", 'r')
        elif NPOP == 1:
            fricDBr = open("spatialdb/rateStateProps_withWall_NP_varyingB.spatialdb", 'r')
        list_of_lines = fricDBr.readlines()
        
        # list_of_lines[52] = " 0.006354  0.003522 -0.003800     0.58  1e-6   " + str(float(DRS) * 1e-6) + "  " + str(A) + "  " + str(B) + "  " + str(A) + "  " + str(float(b_distance) * 1e-6) + "  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        # list_of_lines[53] = " 0.006354  0.003522  0.003800     0.58  1e-6   " + str(float(DRS) * 1e-6) + "  " + str(A) + "  " + str(B) + "  " + str(A) + "  " + str(float(b_distance) * 1e-6) + "  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        # list_of_lines[61] = " 0.063204  0.035034 -0.003800     0.58  1e-6   " + str(float(DRS) * 1e-6) + "  " + str(A) + "  " + str(B) + "  " + str(A) + "  " + str(float(b_distance) * 1e-6) + "  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        # list_of_lines[62] = " 0.063204  0.035034  0.003800     0.58  1e-6   " + str(float(DRS) * 1e-6) + "  " + str(A) + "  " + str(B) + "  " + str(A) + "  " + str(float(b_distance) * 1e-6) + "  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[82] = " 0.015974  0.008855 -0.002800     0.58  1e-6   " + str(float(DRS) * 1e-6) + "  " + str(A) + "  " + str(B) + "  " + str(b_final) + "  " + str(float(b_distance) * 1e-6) + "  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        # list_of_lines[62] = " 0.015100  0.008370  0.000200     0.58  1e-6   " + str(float(DRS) * 1e-6) + "  " + str(A) + "  " + str(B) + "  " + str(b_final) + "  " + str(float(b_distance) * 1e-6) + "  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[83] = " 0.015974  0.008855  0.003200     0.58  1e-6   " + str(float(DRS) * 1e-6) + "  " + str(A) + "  " + str(B) + "  " + str(b_final) + "  " + str(float(b_distance) * 1e-6) + "  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        
        # list_of_lines[94] = " 0.019473  0.010794 -0.002800     0.58  1e-6   " + str(float(DRS) * 1e-6) + "  " + str(A) + "  " + str(B) + "  " + str(b_final) + "  " + str(float(b_distance) * 1e-6) + "  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        # list_of_lines[75] = " 0.019473  0.010794  0.000200     0.58  1e-6   " + str(float(DRS) * 1e-6) + "  " + str(A) + "  " + str(B) + "  " + str(b_final) + "  " + str(float(b_distance) * 1e-6) + "  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        # list_of_lines[95] = " 0.019473  0.010794  0.003200     0.58  1e-6   " + str(float(DRS) * 1e-6) + "  " + str(A) + "  " + str(B) + "  " + str(b_final) + "  " + str(float(b_distance) * 1e-6) + "  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        
        list_of_lines[106] = " 0.022972  0.012733 -0.002800     0.58  1e-6   " + str(float(DRS) * 1e-6) + "  " + str(A) + "  " + str(B) + "  " + str(b_final) + "  " + str(float(b_distance) * 1e-6) + "  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        # list_of_lines[86] = " 0.023846  0.013218  0.000200     0.58  1e-6   " + str(float(DRS) * 1e-6) + "  " + str(A) + "  " + str(B) + "  " + str(b_final) + "  " + str(float(b_distance) * 1e-6) + "  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[107] = " 0.022972  0.012733  0.003200     0.58  1e-6   " + str(float(DRS) * 1e-6) + "  " + str(A) + "  " + str(B) + "  " + str(b_final) + "  " + str(float(b_distance) * 1e-6) + "  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        
        # Modify the locations
        #Wallposition = [self.WallPos3, self.WallPos4, self.WallPos2, self.WallPos5, self.WallPos1, self.WallPos6]
        #counter = 0;
        #for index in range(34, 87):
        #    if len(list_of_lines[index]) > 29:
        #        list_of_lines[index] = list_of_lines[index][0:19] + Wallposition[counter % 6] + list_of_lines[index][29:]
        #        counter = counter + 1
        
        # Write files
        ## Modify rateStateProps
        if NPOP == 0:
            fricDBw = open("spatialdb/rateStateProps_withWall_varyingB.spatialdb", 'w')
        elif NPOP == 1:
            fricDBw = open("spatialdb/rateStateProps_withWall_NP_varyingB.spatialdb", 'w')

        fricDBw.writelines(list_of_lines)
        fricDBr.close()
        fricDBw.close()

        ## Modify NUload
        """
        NULoadCFGr = open("spatialdb/prescribed_traction_initial_withWall_newload.spatialdb", 'r')
        list_of_lines = NULoadCFGr.readlines()

        # First set all loads to be zero
        for index in range(29, 172):
            if len(list_of_lines[index]) > 29:
                list_of_lines[index] = list_of_lines[index][0:29] + "     " + "0.0" + "  0.0  " + "0.0" + "\n"
                
        # Parameters for calculating stress
        nOfIntpPts = 7
        coefs = []
        for pt in range(nOfIntpPts):
            coefs.append((1 + math.cos(- math.pi + 2 * math.pi * pt / (nOfIntpPts - 1))) / 2.0)
        
        # Modify the load
        for pt in range(nOfIntpPts):
            # list_of_lines[62 + pt * 9][34:] = str(NULoad * 0.554309051452769 * coefs[pt]) + "  0.0  " + str(NULoad * coefs[pt]) + "\n"
            # list_of_lines[63 + pt * 9][34:] = str(NULoad * 0.554309051452769 * coefs[pt]) + "  0.0  " + str(NULoad * coefs[pt]) + "\n"
            
            # list_of_lines[161 + pt * 9][34:] = str(-NULoad * 0.554309051452769 * coefs[pt]) + "  0.0  " + str(-NULoad * coefs[pt]) + "\n"
            # list_of_lines[162 + pt * 9][34:] = str(-NULoad * 0.554309051452769 * coefs[pt]) + "  0.0  " + str(-NULoad * coefs[pt]) + "\n"
            list_of_lines[44 + pt * 9] = list_of_lines[44 + pt * 9][0:34] + str(0.0) + "  0.0  " + str(NULoad * coefs[pt]) + "\n"
            list_of_lines[45 + pt * 9] = list_of_lines[45 + pt * 9][0:34] + str(0.0) + "  0.0  " + str(NULoad * coefs[pt]) + "\n"
            
            list_of_lines[107 + pt * 9] = list_of_lines[107 + pt * 9][0:34] + str(0.0) + "  0.0  " + str(-NULoad * coefs[pt]) + "\n"
            list_of_lines[108 + pt * 9] = list_of_lines[108 + pt * 9][0:34] + str(0.0) + "  0.0  " + str(-NULoad * coefs[pt]) + "\n"

        # Modify the locations
        Wallposition = [self.WallPos1, self.WallPos6, self.WallPos2, self.WallPos5, self.WallPos3, self.WallPos4]
        counter = 0;
        for index in range(29, 172):
            if len(list_of_lines[index]) > 29:
                list_of_lines[index] = list_of_lines[index][0:19] + Wallposition[counter % 6] + list_of_lines[index][29:]
                counter = counter + 1

        # Write files
        NULoadCFGw = open("spatialdb/prescribed_traction_initial_withWall_newload.spatialdb", 'w')
        NULoadCFGw.writelines(list_of_lines)
        # print(fileNamePrefix)
        NULoadCFGr.close()
        NULoadCFGw.close()
        """

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
                               " 0.063204  0.035034" + self.WallPos3, 
                               " 0.063204  0.035034" + self.WallPos4]
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
        fileNamePrefix = "1DiffNULoadWithWallDRS1.5_" + str(DRS) + "ModA" + str(A) + "Load" + str(Load) + "_Vw" + str(Vw) + "_fw" + str(fw) + "_theta" + str(theta1) + "_" + str(theta2) + "_NULoad2dir" + str(NULoad)
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
        list_of_lines[59] = " 0.063204  0.035034 -0.003800     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.003  0.0  " + str(fw) + "  " + str(Vw) + "\n"
        list_of_lines[60] = " 0.063204  0.035034  0.003800     0.58  1e-6   " + str(float(DRS) * 1e-6)+ "  " + str(A) + "  0.003  0.0  " + str(fw) + "  " + str(Vw) + "\n"

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
                               " 0.063204  0.035034" + self.WallPos3, 
                               " 0.063204  0.035034" + self.WallPos4, 
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
                               " 0.063204  0.035034" + self.WallPos3, 
                               " 0.063204  0.035034" + self.WallPos4]
        
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
