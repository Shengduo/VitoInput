# A bunch of jobs submission
cd /home/shengduo/pylith-developer/build/debug/
source setup.sh
cd /home/shengduo/pylith-developer/build/debug/pylith-nonRegSlipLaw/examples/3d/Vito/VitoInput/UsualSample
for drs in 8
do
	for load in 4.75
	do
		for vw in 2
		do
			for fw in 0.1
			do
				for theta in 8e-2 9e-2
				do
					for A in 0.020
					do
						for fwW in 0.40
						do
							for VwW in 0.2
							do
								for Vw1 in 0.1
								do
									for b_final in 0.016
									do
										for b_distance in 2e-6
										do
											python3 createInputs_varyingB.py modifyFiles --DRS=$drs --Load=$load --Vw=$vw --VwW=$VwW --Vw1=$Vw1 --fw=$fw --fwW=$fwW --theta=$theta --A=$A --b_final=$b_final --b_distance=$b_distance
											echo "Running case VaryingB_DRS1_${drs}_A${A}_B${b_final}_${b_distance}_Load${load}_fw${fwW}_${fw}_Vww${Vw1}_${VwW}_${vw}_theta${theta}"
											pylith --nodes=16 UsualSampleVaryingBVSFH.cfg >& log/VaryingB_DRS1_${drs}_A${A}_B${b_final}_${b_distance}_Load${load}_fw${fwW}_${fw}_Vw${Vw1}_${VwW}_${vw}_theta${theta}.log
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
