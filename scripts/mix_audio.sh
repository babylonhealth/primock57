# Shell script to mix patient & doctor recordings in single audio file
# Uses SoX Audio: http://sox.sourceforge.net/
echo "Making ../output/mixed_audio directory..."
mkdir -p ../output/mixed_audio
echo "Mixing audio..."
for f in ../audio/*doctor.wav
do
  [[ -e "$f" ]] || break
  outputpath="${f/audio/output/mixed_audio}"
  outputpath="${outputpath/_doctor/}"
  sox -m "$f" "${f/doctor/patient}" "$outputpath"
done
echo "Done!"