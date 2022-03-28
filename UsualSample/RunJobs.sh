# Batch job submission
#cd /home/shengduo/pylith-developer/build/debug/
#source setup.sh
#cd /home/shengduo/pylith-developer/build/debug/pylith-nonRegSlipLaw/examples/3d/Vito/VitoInput/UsualSample
for drs in 2 4 6 8 
do
	for load in 5
	do
		for Vw in 2
		do
			for fw in 0.1
			do
				for theta in 0.043 0.042
				do
					for A in 0.016
					do	
						python3 createInputs.py modifyFiles --DRS=$drs --Load=$load --Vw=$Vw --fw=$fw --theta=$theta --A=$A
						echo "Running case DRS1_${drs}_ModA${A}_Load${load}_fw${fw}_Vw${Vw}_theta${theta}"
						pylith --nodes=16 UsualSampleVSFH.cfg >& log/DRS1_${drs}_ModA${A}_Load${load}_fw${fw}_Vw${Vw}_theta${theta}.log
						echo "Finished!"
						echo
					done
				done
			done
		done
	done
done
