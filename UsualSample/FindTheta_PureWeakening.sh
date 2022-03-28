# Batch job submission
#cd /home/shengduo/pylith-developer/build/debug/
#source setup.sh
#cd /home/shengduo/pylith-developer/build/debug/pylith-nonRegSlipLaw/examples/3d/Vito/VitoInput/UsualSample
for theta in 0.042 0.043
do
	python3 FindTheta_PureWeakening.py modifyFiles --theta=$theta
	echo "Running case PureWeakening_theta${theta}"
	pylith --nodes=16 UsualSampleVSFH_pureweakening.cfg >& log/PureWeakening_theta${theta}.log
	echo "Finished!"
	echo
done
