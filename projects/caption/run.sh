python src/srt2single_text.py data/vUOxuMsss5o_label.srt data/vUOxuMsss5o_label.text
python src/srt2single_text.py data/vUOxuMsss5o_whisper.srt data/vUOxuMsss5o_whisper.text
python src/srt2single_text.py data/vUOxuMsss5o_taption.srt data/vUOxuMsss5o_taption.text
python src/srt2single_text.py data/vUOxuMsss5o_yating.srt data/vUOxuMsss5o_yating.text

echo "Whisper CER(%)"
python src/compute-wer.py --char=1 --v=0 data/vUOxuMsss5o_label.text data/vUOxuMsss5o_whisper.text

echo "taption CER(%)"
python src/compute-wer.py --char=1 --v=0 data/vUOxuMsss5o_label.text data/vUOxuMsss5o_taption.text

echo "yating CER(%)"
python src/compute-wer.py --char=1 --v=0 data/vUOxuMsss5o_label.text data/vUOxuMsss5o_yating.text

echo "Done!"