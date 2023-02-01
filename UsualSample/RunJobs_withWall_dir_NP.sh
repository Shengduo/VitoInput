
# Batch job submission
#cd /home/shengduo/pylith-developer/build/debug/
#source setup.sh
#cd /home/shengduo/pylith-developer/build/debug/pylith-nonRegSlipLaw/examples/3d/Vito/VitoInput/UsualSample
# Fix drs=6 Vw=1.5 fw=0.1 theta=0.036 A=0.016
for drs in 1.5
do
	for load in 5
	# for load in 10
	do
		for Vw in 2
		# for Vw in 0.2
		do
			for fw in 0.1
			# for fw in 0.33
			do
				# for theta1 in 0.006
				# for theta1 in 1.4664 # 10^-7 for a = 0.011, b = 0.016
				for theta1 in 0.1434 # 10^-7 for a = 0.003, b = 0.008
				# for theta1 in 0.3399 # 10^-8
				# for theta1 in 0.8061 # 10^-9
				do
					for theta2 in -7
					# for theta2 in 1.4664
					do
						# for A in 0.016
						for A in 0.016
						do
							# for AmB in -0.005
							for AmB in 0.014
							# for AmB in 0.012
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
											for rest in 8
											do
												for NPOP in 1
												do
													# Start the timer
													start_time=$(date +%s)
													
													fileNamePrefix=W8_4${NPOP}DirWithWallDRS1.5_${drs}ModA_${A}_AmB${AmB}_Load${load}_Vw${Vw}_fw${fw}_theta${theta1}_${theta2}_NULoad2dir${NULoad}_duration${duration}_${rest}
													python3 createInputs_withWall_Dirichlet_NP_newload.py modifyFiles --DRS=$drs --Load=$load --Vw=$Vw --fw=$fw --theta1=$theta1 --theta2=$theta2 --A=$A --AmB=$AmB --NULoad=$NULoad --meshFineness=$meshFineness --duration=$duration --rest=$rest --NPOP=$NPOP
													echo "Running case ${fileNamePrefix}"
													pylith --nodes=8 UsualSampleVSFH_withWall_Dirichlet.cfg >& log/${fileNamePrefix}.log

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