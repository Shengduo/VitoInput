# Batch job submission
#cd /home/shengduo/pylith-developer/build/debug/
#source setup.sh
#cd /home/shengduo/pylith-developer/build/debug/pylith-nonRegSlipLaw/examples/3d/Vito/VitoInput/UsualSample
# Fix drs=6 Vw=1.5 fw=0.1 theta=0.036 A=0.016
for drs in 8
do
	for load in 5
	do
		for Vw in 2
		do
			for fw in 0.1
			do
				for theta in 0.036
				do
					for A in 0.016
					do	
						for NULoad in 1.5 1
						do
							python3 createInputs.py modifyFiles --DRS=$drs --Load=$load --Vw=$Vw --fw=$fw --theta=$theta --A=$A --NULoad=$NULoad
							echo "Running case DRS1_${drs}_ModA${A}_Load${load}_fw${fw}_Vw${Vw}_theta${theta}_NULoad${NULoad}"
							pylith --nodes=16 UsualSampleVSFH.cfg >& log/DRS1_${drs}_ModA${A}_Load${load}_fw${fw}_Vw${Vw}_theta${theta}_NULoad${NULoad}.log
							echo "Finished!"
							echo
						done
					done
				done
			done
		done
	done
done
