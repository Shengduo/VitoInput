# Batch job submission
# This file runs base comparison cases with 
#	1. Only Homalite plates
#   2. VS but no weakening
for drs in 1.5
do
	for load in 5
	do
		for Vw in 0.2
		do
			for fw in 0.33
			do
				for theta1 in 0.036
				do
					for theta2 in 0.036
					do
						for A in 0.003
						do	
							for B in 0.008
							do
								for NULoad in 0
								do
									fileNamePrefix=1WithWallDRS1.5_${drs}ModA_${A}_B${B}_Load${Load}_Vw${Vw}_fw${fw}_theta${theta1}_${theta2}_NULoad2dir${NULoad}
									python3 createInputs_withWall.py modifyFiles --DRS=$drs --Load=$load --Vw=$Vw --fw=$fw --theta1=$theta1 --theta2=$theta2 --A=$A --B=$B --NULoad=$NULoad
									echo "Running case ${fileNamePrefix}"
									# pylith --nodes=16 UsualSampleVSFH_withWall.cfg >& log/${fileNamePrefix}.log
									echo "Finished!"
									echo
								done
							done
						done
					done
				done
			done
		done
	done
done

for drs in 1.5
do
	for load in 5
	do
		for Vw in 2e16
		do
			for fw in 0.58
			do
				for theta1 in 0.036
				do
					for theta2 in 8e15
					do
						for A in 0.008
						do	
							for B in 0.003
							do
								for NULoad in 0
								do
									fileNamePrefix=1WithWallDRS1.5_${drs}ModA_${A}_B${B}_Load${Load}_Vw${Vw}_fw${fw}_theta${theta1}_${theta2}_NULoad2dir${NULoad}
									python3 createInputs_withWall.py modifyFiles --DRS=$drs --Load=$load --Vw=$Vw --fw=$fw --theta1=$theta1 --theta2=$theta2 --A=$A --B=$B --NULoad=$NULoad
									echo "Running case ${fileNamePrefix}"
									pylith --nodes=16 UsualSampleVSFH_withWall.cfg >& log/${fileNamePrefix}.log
									echo "Finished!"
									echo
								done
							done
						done
					done
				done
			done
		done
	done
done