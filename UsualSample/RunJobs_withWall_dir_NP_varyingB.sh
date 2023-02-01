
# Batch job submission
#cd /home/shengduo/pylith-developer/build/debug/
#source setup.sh
#cd /home/shengduo/pylith-developer/build/debug/pylith-nonRegSlipLaw/examples/3d/Vito/VitoInput/UsualSample
# Fix drs=6 Vw=1.5 fw=0.1 theta=0.036 A=0.016
for drs in 1.5
do
	for load in 5
	do
		for Vw in 2
		do
			for fw in 0.1
			do
				for theta1 in 0.006
				do
					for theta2 in -9
					do
						for A in 0.011
						do
							for AmB in 0.005
							do
								if [[ $(echo "$A<=$AmB" |bc -l) -eq 1 ]]; then
									echo "Shit!"
									continue
								fi
								for NULoad in 0
								do
									for meshFineness in 1
									do
										for duration in 200
										do
											for rest in 0
											do
												for NPOP in 0
												do
													for b_final in 2.0
													do
														for b_distance in 10
														do
															# Start the timer
															start_time=$(date +%s)
															
															fileNamePrefix=NO${NPOP}VaryingBDirWithWallDRS1.5_${drs}ModA_${A}_AmB${AmB}_${b_final}bD${b_distance}_Load${load}_Vw${Vw}_fw${fw}_theta${theta1}_${theta2}_NULoad2dir${NULoad}_duration${duration}_${rest}
															python3 createInputs_withWall_Dirichlet_NP_newload_varyingB.py modifyFiles --DRS=$drs --Load=$load --b_final=${b_final} --Vw=$Vw --fw=$fw --theta1=$theta1 --theta2=$theta2 --A=$A --AmB=$AmB --b_distance=${b_distance} --NULoad=$NULoad --meshFineness=$meshFineness --duration=$duration --rest=$rest --NPOP=$NPOP
															echo "Running case ${fileNamePrefix}"
															# pylith --nodes=16 UsualSampleVSFH_withWall_Dirichlet_varyingB.cfg >& log/${fileNamePrefix}.log

															# End the timer, report time
															end_time=$(date +%s)
															elapsed=$(( end_time - start_time ))
															echo "Finished in ${elapsed} s!"
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
		for Vw in 2
		do
			for fw in 0.1
			do
				for theta1 in 0.005
				do
					for theta2 in -9
					do
						for A in 0.011
						do
							for AmB in 0.005
							do
								if [[ $(echo "$A<=$AmB" |bc -l) -eq 1 ]]; then
									echo "Shit!"
									continue
								fi
								for NULoad in 3
								do
									for meshFineness in 1
									do
										for duration in 200
										do
											for rest in 0
											do
												for NPOP in 0
												do
													for b_final in 2.0 3.0
													do
														for b_distance in 10 20
														do
															# Start the timer
															start_time=$(date +%s)
															
															fileNamePrefix=NO${NPOP}VaryingBDirWithWallDRS1.5_${drs}ModA_${A}_AmB${AmB}_${b_final}bD${b_distance}_Load${load}_Vw${Vw}_fw${fw}_theta${theta1}_${theta2}_NULoad2dir${NULoad}_duration${duration}_${rest}
															python3 createInputs_withWall_Dirichlet_NP_newload_varyingB.py modifyFiles --DRS=$drs --Load=$load --b_final=${b_final} --Vw=$Vw --fw=$fw --theta1=$theta1 --theta2=$theta2 --A=$A --AmB=$AmB --b_distance=${b_distance} --NULoad=$NULoad --meshFineness=$meshFineness --duration=$duration --rest=$rest --NPOP=$NPOP
															echo "Running case ${fileNamePrefix}"
															pylith --nodes=16 UsualSampleVSFH_withWall_Dirichlet_varyingB.cfg >& log/${fileNamePrefix}.log

															# End the timer, report time
															end_time=$(date +%s)
															elapsed=$(( end_time - start_time ))
															echo "Finished in ${elapsed} s!"
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
					done
				done
			done
		done
	done
done


# -- Second case ------
for drs in 1.5
do
	for load in 5
	do
		for Vw in 2
		do
			for fw in 0.1
			do
				for theta1 in 0.0045
				do
					for theta2 in -9
					do
						for A in 0.011
						do
							for AmB in 0.005
							do
								if [[ $(echo "$A<=$AmB" |bc -l) -eq 1 ]]; then
									echo "Shit!"
									continue
								fi
								for NULoad in 1
								do
									for meshFineness in 2
									do
										for duration in 200
										do
											for rest in 0
											do
												for NPOP in 0
												do
													for b_final in 2.0
													do
														for b_distance in 7
														do
															# Start the timer
															start_time=$(date +%s)
															
															fileNamePrefix=NO${NPOP}VaryingBDirWithWallDRS1.5_${drs}ModA_${A}_AmB${AmB}_${b_final}bD${b_distance}_Load${load}_Vw${Vw}_fw${fw}_theta${theta1}_${theta2}_NULoad2dir${NULoad}_duration${duration}_${rest}
															python3 createInputs_withWall_Dirichlet_NP_newload_varyingB.py modifyFiles --DRS=$drs --Load=$load --b_final=${b_final} --Vw=$Vw --fw=$fw --theta1=$theta1 --theta2=$theta2 --A=$A --AmB=$AmB --b_distance=${b_distance} --NULoad=$NULoad --meshFineness=$meshFineness --duration=$duration --rest=$rest --NPOP=$NPOP
															echo "Running case ${fileNamePrefix}"
															# pylith --nodes=16 UsualSampleVSFH_withWall_Dirichlet_varyingB.cfg >& log/${fileNamePrefix}.log

															# End the timer, report time
															end_time=$(date +%s)
															elapsed=$(( end_time - start_time ))
															echo "Finished in ${elapsed} s!"
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
					done
				done
			done
		done
	done
done