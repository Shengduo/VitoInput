
# Batch job submission
#cd /home/shengduo/pylith-developer/build/debug/
#source setup.sh
#cd /home/shengduo/pylith-developer/build/debug/pylith-nonRegSlipLaw/examples/3d/Vito/VitoInput/UsualSample
# Fix drs=6 Vw=1.5 fw=0.1 theta=0.036 A=0.016

# ======== OP Pure Homalite ================================================================================
for drs in 1.5
do
	for load in 5
	do
		for Vw in 0.2
		do
			for fw in 0.33
			do
				for theta1 in 0.006
				do
					for theta2 in 0.006
					do
						for A in 0.011
						do
							for AmB in -0.005
							do
								if [[ $(echo "$A<=$AmB" |bc -l) -eq 1 ]]; then
									echo "Shit!"
									continue
								fi
								for NULoad in 0
								do
									for meshFineness in 2
									do
										for duration in 200
										do
											for rest in 0
											do
												for NPOP in 0
												do
													# Start the timer
													start_time=$(date +%s)
													
													fileNamePrefix=NO${NPOP}DirWithWallDRS1.5_${drs}ModA_${A}_AmB${AmB}_Load${load}_Vw${Vw}_fw${fw}_theta${theta1}_${theta2}_NULoad2dir${NULoad}_duration${duration}_${rest}
													python3 createInputs_withWall_Dirichlet_NP_newload.py modifyFiles --DRS=$drs --Load=$load --Vw=$Vw --fw=$fw --theta1=$theta1 --theta2=$theta2 --A=$A --AmB=$AmB --NULoad=$NULoad --meshFineness=$meshFineness --duration=$duration --rest=$rest --NPOP=$NPOP
													echo "Running case ${fileNamePrefix}"
													# pylith --nodes=16 UsualSampleVSFH_withWall_Dirichlet.cfg >& log/${fileNamePrefix}.log

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


# ======= NP Pure Homalite ===================================================================================
for drs in 1.5
do
	for load in 5
	do
		for Vw in 2000000000000 2
		do
			for fw in 0.1
			do
				for theta1 in 0.00224
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
									for meshFineness in 2
									do
										for duration in 200
										do
											for rest in 0
											do
												for NPOP in 1
												do
													# Start the timer
													start_time=$(date +%s)
													
													fileNamePrefix=NO${NPOP}DirWithWallDRS1.5_${drs}ModA_${A}_AmB${AmB}_Load${load}_Vw${Vw}_fw${fw}_theta${theta1}_${theta2}_NULoad2dir${NULoad}_duration${duration}_${rest}
													python3 createInputs_withWall_Dirichlet_NP_newload.py modifyFiles --DRS=$drs --Load=$load --Vw=$Vw --fw=$fw --theta1=$theta1 --theta2=$theta2 --A=$A --AmB=$AmB --NULoad=$NULoad --meshFineness=$meshFineness --duration=$duration --rest=$rest --NPOP=$NPOP
													echo "Running case ${fileNamePrefix}"
													pylith --nodes=16 UsualSampleVSFH_withWall_Dirichlet.cfg >& log/${fileNamePrefix}.log

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


# ========== OP Vs no flash heating ========================================================================
for drs in 1.5
do
	for load in 5
	do
		for Vw in 2e16
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
									for meshFineness in 2
									do
										for duration in 200
										do
											for rest in 0
											do
												for NPOP in 0
												do
													# Start the timer
													start_time=$(date +%s)
													
													fileNamePrefix=NO${NPOP}DirWithWallDRS1.5_${drs}ModA_${A}_AmB${AmB}_Load${load}_Vw${Vw}_fw${fw}_theta${theta1}_${theta2}_NULoad2dir${NULoad}_duration${duration}_${rest}
													python3 createInputs_withWall_Dirichlet_NP_newload.py modifyFiles --DRS=$drs --Load=$load --Vw=$Vw --fw=$fw --theta1=$theta1 --theta2=$theta2 --A=$A --AmB=$AmB --NULoad=$NULoad --meshFineness=$meshFineness --duration=$duration --rest=$rest --NPOP=$NPOP
													echo "Running case ${fileNamePrefix}"
													# pylith --nodes=16 UsualSampleVSFH_withWall_Dirichlet.cfg >& log/${fileNamePrefix}.log

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


# ========== OP Vs no flash heating ========================================================================
for drs in 1.5
do
	for load in 5
	do
		for Vw in 2e16
		do
			for fw in 0.1
			do
				for theta1 in 0.00224
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
									for meshFineness in 2
									do
										for duration in 200
										do
											for rest in 0
											do
												for NPOP in 1
												do
													# Start the timer
													start_time=$(date +%s)
													
													fileNamePrefix=NO${NPOP}DirWithWallDRS1.5_${drs}ModA_${A}_AmB${AmB}_Load${load}_Vw${Vw}_fw${fw}_theta${theta1}_${theta2}_NULoad2dir${NULoad}_duration${duration}_${rest}
													python3 createInputs_withWall_Dirichlet_NP_newload.py modifyFiles --DRS=$drs --Load=$load --Vw=$Vw --fw=$fw --theta1=$theta1 --theta2=$theta2 --A=$A --AmB=$AmB --NULoad=$NULoad --meshFineness=$meshFineness --duration=$duration --rest=$rest --NPOP=$NPOP
													echo "Running case ${fileNamePrefix}"
													# pylith --nodes=16 UsualSampleVSFH_withWall_Dirichlet.cfg >& log/${fileNamePrefix}.log

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