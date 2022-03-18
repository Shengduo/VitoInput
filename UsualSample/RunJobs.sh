# Batch job submission
cd /home/shengduo/pylith-developer/build/debug/
source setup.sh
cd /home/shengduo/pylith-developer/build/debug/pylith-nonRegSlipLaw/examples/3d/Vito/VitoInput/UsualSample
for drs in 8
do
	for load in 4.75
	do
		for vw in 4
		do
			for fw in 0.1
			do
				for theta in 9e-2
				do
					for A in 0.020
					do
						for fwW in 0.35
						do
							for VwW in 1.5
							do
								for Vw1 in 0.1
								do
									python3 createInputs.py modifyFiles --DRS=$drs --Load=$load --Vw=$vw --VwW=$VwW --Vw1=$Vw1 --fw=$fw --fwW=$fwW --theta=$theta --A=$A
									echo "Running case VWFirst_DRS1_${drs}_ModA${A}_Load${load}_fw${fwW}_${fw}_Vww${Vw1}_${VwW}_${vw}_theta${theta}"
									pylith UsualSampleVSFH.cfg >& VWFirst_DRS1_${drs}_ModA${A}_Load${load}_fw${fwW}_${fw}_Vw${Vw1}_${VwW}_${vw}_theta${theta}.log
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
