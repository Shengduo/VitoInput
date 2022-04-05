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
				for theta1 in 0.036
				do
					for theta2 in 8
					do
						for A in 0.016
						do	
							for NULoad in 1
							do
								fileNamePrefix=DiffNULoadWithWallDRS1.5_${drs}ModA_${A}Load${Load}_Vw${Vw}_fw${fw}_theta${theta1}_${theta2}_NULoad2dir${NULoad}
								python3 createInputs_withWall.py modifyFiles_GougeDifferentLoad --DRS=$drs --Load=$load --Vw=$Vw --fw=$fw --theta1=$theta1 --theta2=$theta2 --A=$A --NULoad=$NULoad
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
