# Shell script to mix patient & doctor recordings in single audio file
# Uses SoX Audio: http://sox.sourceforge.net/
echo "Making mixed_audio directory..."
mkdir -p output/mixed_audio
echo "Mixing audio..."
for f in audio/*doctor.wav
do
  [[ -e "$f" ]] || break
  sox -m "$f" "${f/doctor/patient}" output/mixed_"${f/_doctor/}"
done
echo "Done!"