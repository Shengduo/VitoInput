# A bunch of jobs submission
cd /home/shengduo/pylith-developer/build/debug/
source setup.sh
cd -
for drs in 192
do
	for load in 4.75
	do
		for Vw3 in 4
		do
			for fw3 in 0.2 0.3
			do
				for theta in 9e-2
				do
					for A in 0.024
					do
						for fw2 in 0.1
						do
							for Vw2 in 4
							do
								for Vw1 in 0.1
								do
									for b_initial in 0.013
									do 
										for b_final2 in 0.011
										do
											for b_final3 in 0.009 0.011 0.013
											do
												for b_distance in 8e-6 16e-6 32e-6
												do
													python3 createInputs_varyingB.py modifyFiles --DRS=$drs --Load=$load --Vw1=$Vw1 --Vw2=$Vw2 --Vw3=$Vw3 --fw2=$fw2 --fw3=$fw3 --theta=$theta --A=$A --b_initial=$b_initial --b_final2=$b_final2 --b_final3=$b_final3 --b_distance=$b_distance
													echo "Running case VaryingB_DRS1_${drs}_A${A}_B${b_initial}_${b_final2}_${b_final3}_${b_distance}_Load${load}_fw${fw2}_${fw3}_Vww${Vw1}_${Vw2}_${Vw3}_theta${theta}"
													pylith --nodes=16 UsualSampleVaryingBVSFH.cfg >& log/VaryingB_DRS1_${drs}_A${A}_B${b_initial}_${b_final2}_${b_final3}_${b_distance}_Load${load}_fw${fw2}_${fw3}_Vw${Vw1}_${Vw2}_${Vw3}_theta${theta}.log
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
			done
		done
	done
done
